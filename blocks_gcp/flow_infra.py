
from prefect_gcp.cloud_run import CloudRunJob
from prefect_gcp import GcpCredentials
import os

credentials = GcpCredentials.load("gcp-credentials")

def create_task_definition(flow_name: str) -> str:
    """
    Create cloud run job infra for the flow run
    Args:
        flow_name: flow name 
    Return:
        None
    """
    gcp_flow_infra_name = f"{flow_name}-infra"
    block = CloudRunJob(
        credentials=credentials,
        project=f"{os.environ['GCP_PROJECT_ID']}",
        image=f"{os.environ['GCP_ARTIFACT_REPO']}/{flow_name}:latest",
        region=f"{os.environ['GCP_REGION']}"
    )
    block.save(gcp_flow_infra_name, overwrite=True)
    return gcp_flow_infra_name