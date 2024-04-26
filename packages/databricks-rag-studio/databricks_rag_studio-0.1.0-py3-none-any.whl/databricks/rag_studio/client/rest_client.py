from typing import List, Optional
from databricks.rag_studio.utils.rest_utils import call_endpoint
from databricks.rag_studio.sdk_utils.entities import Deployment, Artifacts, Instructions


def _construct_chain_deployment(chain_deployment: dict) -> Deployment:
    # ToDo (ML-39446): Use automatic proto to py object conversion
    # Do not surface error to user if the backend return missing fields
    return Deployment(
        model_name=chain_deployment.get("model_name", None),
        model_version=chain_deployment.get("model_version", None),
        endpoint_name=chain_deployment.get("endpoint_name", None),
        served_entity_name=chain_deployment.get("served_entity_name", None),
        query_endpoint=chain_deployment.get("query_endpoint", None),
        rag_app_url=chain_deployment.get("rag_app_url", None),
    )


def _parse_deploy_chain_response(response: dict) -> Deployment:
    # ToDo (ML-39446): Use automatic proto to py object conversion
    # Do not surface error to user if the backend return missing fields
    deployed_chain = response.get("deployed_chain", None)
    return _construct_chain_deployment(deployed_chain) if deployed_chain else None


def _parse_get_chain_deployments_response(response: dict) -> List[Deployment]:
    # ToDo (ML-39446): Use automatic proto to py object conversion
    # Do not surface error to user if the backend return missing fields
    chain_deployments = response.get("chain_deployments", [])
    return [_construct_chain_deployment(x) for x in chain_deployments]


def _parse_list_chain_deployments_response(response: dict) -> List[Deployment]:
    # ToDo (ML-39446): Use automatic proto to py object conversion
    # Do not surface error to user if the backend return missing fields
    chain_deployments = response.get("chain_deployments", [])
    return [_construct_chain_deployment(x) for x in chain_deployments]


def deploy_chain(
    model_name: str,
    model_version: str,
    query_endpoint: str,
    endpoint_name: str,
    served_entity_name: str,
    workspace_url: str,
) -> Deployment:
    request_body = {
        "model_name": model_name,
        "model_version": model_version,
        "query_endpoint": query_endpoint,
        "endpoint_name": endpoint_name,
        "served_entity_name": served_entity_name,
        "workspace_url": workspace_url,
    }
    response = call_endpoint(
        method="POST",
        route="chains",
        json_body=request_body,
    )

    return _parse_deploy_chain_response(response)


# TODO: add back in params once we've added pagination
# https://github.com/databricks/universe/pull/514434#discussion_r1518324393
def list_chain_deployments():
    response = call_endpoint(
        method="GET",
        route="chains",
    )

    return _parse_list_chain_deployments_response(response)


def get_chain_deployments(model_name: str, model_version: Optional[str] = None):
    request_body = {"model_name": model_name}
    route = f"chains/{model_name}"
    if model_version:
        route = f"{route}/versions/{model_version}"
        request_body |= {"model_version": model_version}

    response = call_endpoint(
        method="GET",
        route=route,
        json_body=request_body,
    )
    return _parse_get_chain_deployments_response(response)


def create_review_artifacts(model_name: str, artifacts: List[str]):
    request_body = {
        "model_name": model_name,
        "artifacts": artifacts,
    }
    call_endpoint(
        method="POST",
        route=f"chains/{model_name}/artifacts",
        json_body=request_body,
    )


def get_review_artifacts(model_name: str):
    request_body = {"model_name": model_name}

    response = call_endpoint(
        method="GET",
        route=f"chains/{model_name}/artifacts",
        json_body=request_body,
    )
    if "artifacts" not in response:
        return Artifacts(artifact_uris=[])
    return Artifacts(artifact_uris=response["artifacts"])


def set_review_instructions(model_name: str, instructions: str):
    request_body = {
        "model_name": model_name,
        "instructions": instructions,
    }
    call_endpoint(
        method="POST",
        route=f"chains/{model_name}/instructions",
        json_body=request_body,
    )


def get_review_instructions(model_name: str) -> Instructions:
    request_body = {"model_name": model_name}
    response = call_endpoint(
        method="GET",
        route=f"chains/{model_name}/instructions",
        json_body=request_body,
    )
    if "instructions" not in response:
        return Instructions(None)
    return Instructions(response["instructions"])
