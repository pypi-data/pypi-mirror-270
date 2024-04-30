from .constants import IndexTypes, EmbeddingTypes
from .utils import CallbackContext, tool_ui_callback
from azureml.rag.utils.connections import connection_to_credential
from promptflow.connections import AzureOpenAIConnection
from typing import Dict, List


def SentenceTransformerIsInstalled() -> bool:
    try:
        from sentence_transformers import SentenceTransformer  # noqa: F401
    except ImportError:
        return False

    return True


@tool_ui_callback
def list_available_embedding_types(context: CallbackContext, index_type: str) -> List[Dict[str, str]]:
    connections = context.ml_client.connections._operation.list(
        workspace_name=context.workspace_name,
        cls=lambda objs: objs,
        category=None,
        **context.ml_client.connections._scope_kwargs)

    workspace_contains_aoai_connection = False
    workspace_contains_oai_connection = False
    workspace_contains_serverless_connection = False
    for connection in connections:
        if connection.properties.category == 'AzureOpenAI':
            workspace_contains_aoai_connection = True

        if connection.properties.category == 'Serverless':
            if workspace_contains_serverless_connection:
                continue

            (_, info) = _resolve_serverless_connection(context, connection)
            if info.get('model_type') == 'embedding':
                workspace_contains_serverless_connection = True

        if workspace_contains_aoai_connection and \
                workspace_contains_oai_connection and \
                workspace_contains_serverless_connection:
            break

    workspace_contains_serverless_deployment = False
    try:
        auth_header = f'Bearer {context.credential.get_token("https://management.azure.com/.default").token}'
        response = context.http.get(f'https://management.azure.com{context.arm_id}'
                                    '/serverlessEndpoints?api-version=2024-01-01-preview',
                                    headers={'Authorization': auth_header})
        response.raise_for_status()
        deployments = response.json()

        for deployment in deployments.get('value', []):
            (_, info) = _resolve_serverless_deployment(context, deployment)
            if info.get('model_type') == 'embedding':
                workspace_contains_serverless_deployment = True
                break
    except Exception:
        # Ignore forbidden exceptions - the user may not have access to list deployments.
        if response.status_code != 403:
            raise

    embedding_types = []

    # This should be the set of index backends that support embedding-less querying (eg, Keyword).
    # At present, this includes only Azure Cog Search.
    if index_type in {IndexTypes.AzureCognitiveSearch}:
        embedding_types.append({'value': EmbeddingTypes.NoEmbedding, 'displayValue': EmbeddingTypes.NoEmbedding})

    if workspace_contains_aoai_connection:
        embedding_types.append({'value': EmbeddingTypes.AzureOpenAI, 'displayValue': EmbeddingTypes.AzureOpenAI})

    if workspace_contains_oai_connection:
        embedding_types.append({'value': EmbeddingTypes.OpenAI, 'displayValue': EmbeddingTypes.OpenAI})

    if workspace_contains_serverless_connection or workspace_contains_serverless_deployment:
        embedding_types.append(
            {'value': EmbeddingTypes.ServerlessDeployment, 'displayValue': EmbeddingTypes.ServerlessDeployment})

    if SentenceTransformerIsInstalled():
        embedding_types.append({'value': EmbeddingTypes.HuggingFace, 'displayValue': EmbeddingTypes.HuggingFace})

    return embedding_types


@tool_ui_callback
def list_embedding_models(context: CallbackContext, embedding_type: str) -> List[Dict[str, str]]:
    if embedding_type == EmbeddingTypes.OpenAI:
        return [{'value': 'text-embedding-ada-002', 'display_value': 'text-embedding-ada-002'}]

    if embedding_type == EmbeddingTypes.HuggingFace:
        return [{
            'value': 'sentence-transformers/all-mpnet-base-v2',
            'display_value': 'sentence-transformers/all-mpnet-base-v2'}]

    raise ValueError(f'Unsupported embedding type: {embedding_type}.')


@tool_ui_callback
def list_aoai_embedding_deployments(
        context: CallbackContext,
        aoai_connection: AzureOpenAIConnection
) -> List[Dict[str, str]]:
    selected_connection = context.ml_client.connections._operation.get(
        workspace_name=context.workspace_name,
        connection_name=aoai_connection,
        **context.ml_client.connections._scope_kwargs)

    deployments_url = f'https://management.azure.com{selected_connection.properties.metadata.get("ResourceId")}' +\
        '/deployments?api-version=2023-05-01'
    models_url = f'https://management.azure.com{selected_connection.properties.metadata.get("ResourceId")}' +\
        '/models?api-version=2023-05-01'
    auth_header = f'Bearer {context.credential.get_token("https://management.azure.com/.default").token}'

    deployments_response = context.http.get(deployments_url, headers={'Authorization': auth_header}).json()
    models_response = context.http.get(models_url, headers={'Authorization': auth_header}).json()

    embedding_models =\
        set([f'{mdl.get("name")}:{mdl.get("version")}'
             for mdl in models_response.get('value')
             if mdl.get('capabilities', dict()).get('embeddings', 'false').lower() == 'true'])

    embedding_deployments =\
        [depl
         for depl in deployments_response.get('value')
         if f'{depl.get("properties", dict()).get("model", dict()).get("name")}:'
            f'{depl.get("properties", dict()).get("model", dict()).get("version")}'
         in embedding_models]

    return [{
        'value': depl.get('name'),
        'display_value': depl.get('name'),
    } for depl in embedding_deployments]


@tool_ui_callback
def list_serverless_embedding_connections(context: CallbackContext) -> List[Dict[str, str]]:
    connections = context.ml_client.connections._operation.list(
        workspace_name=context.workspace_name,
        cls=lambda objs: objs,
        category='Serverless',
        **context.ml_client.connections._scope_kwargs)

    options = []

    # Populate serverless connection dropdown options
    for connection in connections:
        (_, info) = _resolve_serverless_connection(context, connection)
        if info.get('model_type') == 'embedding':
            model_provider = info.get('provider_name')
            model_name = info.get('model_name')

            if model_provider and model_name:
                model_description = f'the {model_provider} "{model_name}"'
            elif model_provider:
                model_description = f'an unknown {model_provider}'
            elif model_name:
                model_description = f'the "{model_name}"'
            else:
                model_description = 'an unknown'

            options.append({
                'value': f'connection:{connection.name}',
                'display_value': f'connection:{connection.name}',
                'description': f'A connection to a serverless deployment instance of {model_description} embedding model.',  # noqa: E501
            })

    # Populate serverless deployment dropdown options
    try:
        auth_header = f'Bearer {context.credential.get_token("https://management.azure.com/.default").token}'
        response = context.http.get(f'https://management.azure.com{context.arm_id}'
                                    '/serverlessEndpoints?api-version=2024-01-01-preview',
                                    headers={'Authorization': auth_header})
        response.raise_for_status()
        deployments = response.json()

        for deployment in deployments.get('value', []):
            (_, info) = _get_serverless_deployment_info(context, deployment)
            if info.get('model_type') == 'embedding':
                model_provider = info.get('provider_name')
                model_name = info.get('model_name')

                if model_provider and model_name:
                    model_description = f'the {model_provider} "{model_name}"'
                elif model_provider:
                    model_description = f'an unknown {model_provider}'
                elif model_name:
                    model_description = f'the "{model_name}"'
                else:
                    model_description = 'an unknown'

                options.append({
                    'value': f'deployment:{deployment.get("name")}',
                    'display_value': f'deployment:{deployment.get("name")}',
                    'description': f'A connection to a serverless deployment instance of {model_description} embedding model.',  # noqa: E501
                })
    except Exception:
        # Ignore forbidden exceptions - the user may not have access to list deployments.
        if response.status_code != 403:
            raise

    return options


def _resolve_serverless_connection(context, connection):
    connection_info = {
        'model_type': connection.properties.metadata.get('served_model_type')
        or connection.properties.metadata.get('model_type'),
        'model_name': connection.properties.metadata.get('model_name')
        or connection.properties.metadata.get('served_model_name'),
        'provider_name': connection.properties.metadata.get('model_provider_name'),
    }

    api_base = connection.properties.target

    if any([value is None for value in connection_info.values()]):
        auth_header = f'Bearer {context.credential.get_token("https://management.azure.com/.default").token}'
        list_secrets_response = context.http.post(
            f'https://management.azure.com{connection.id}/listSecrets?api-version=2024-01-01-preview',
            headers={'Authorization': auth_header}
        )
        api_key = connection_to_credential(list_secrets_response.json()).key
        info = _get_serverless_deployment_info(context, api_base, api_key)
        return (api_base, ({key: connection_info.get(key) or info.get(key) for key in connection_info}))
    else:
        return (api_base, connection_info)


def _resolve_serverless_deployment(context, deployment):
    auth_header = f'Bearer {context.credential.get_token("https://management.azure.com/.default").token}'
    api_base = deployment.get('properties', {}).get('inferenceEndpoint', {}).get('uri')
    api_key = context.http.post(
        f'https://management.azure.com{deployment.get("id")}/listKeys?api-version=2024-01-01-preview',
        headers={'Authorization': auth_header},
    ).json().get('primaryKey')

    info = _get_serverless_deployment_info(context, api_base, api_key)
    return (api_base, info)


def _get_serverless_deployment_info(context, api_base, api_key):
    try:
        info_response = context.http.get(f'{api_base}/info', headers={'Authorization': f'Bearer {api_key}'})
        info_response.raise_for_status()
        info_json = info_response.json()
    except Exception:
        info_json = dict()

    return {
        'model_type': info_json.get('served_model_type') or info_json.get('model_type'),
        'model_name': info_json.get('served_model_name') or info_json.get('model_name'),
        'provider_name': info_json.get('model_provider_name'),
    }
