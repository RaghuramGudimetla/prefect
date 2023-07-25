from prefect.deployments import Deployment
from flow import sample_task
from prefect_aws.ecs import ECSTask
from prefect.filesystems import S3
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from blocks.flowconfigs import create_flow_storage_block

# Deploy and use storage block
def create_flow_storage(flow_name: str) -> bool:
    """
    Deploys the flow
    Args:
        None
    Return:
        None
    """
    block_created = create_flow_storage_block(flow_name=flow_name)
    return block_created


def deploy_flow(flow_name: str):
    """
    Deploys the flow
    Args:
        None
    Return:
        None
    """
    ecs_task_block = ECSTask.load("prefect-agent")
    storage_block = S3.load(f'storage-{flow_name}')
    deployment = Deployment.build_from_flow(
        flow=sample_task,
        name=f'deploy-{flow_name}',
        version=1,
        work_queue_name='default',
        work_pool_name="agent-pool",
        storage=storage_block,
        infrastructure=ecs_task_block,
        ignore_file='.prefectignore',
        path="/",
        infra_overrides={
                "env.EXTRA_PIP_PACKAGES": "prefect-aws s3fs awswrangler",
                "env.PREFECT_LOGGING_LEVEL": "DEBUG"
            }
    )
    deployment.apply()

flow_name = "sample-flow"
create_flow_storage(flow_name=flow_name)
deploy_flow(flow_name=flow_name)