from databricks.rag_studio.sdk_utils.entities import Deployment
from databricks.rag_studio.sdk_utils.permissions_checker import (
    _check_view_permissions_on_deployment,
)
from databricks.rag_studio.client.rest_client import (
    get_chain_deployments as rest_get_chain_deployments,
)
from typing import List, Optional


def _get_deployments(
    model_name: str, model_version: Optional[int] = None
) -> List[Deployment]:
    deployments = rest_get_chain_deployments(model_name, model_version)
    # TODO(ML-39693): Filter out deleted endpoints
    if len(deployments) > 0:
        _check_view_permissions_on_deployment(deployments[0])
    return deployments
