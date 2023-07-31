from prefect.deployments import Deployment
from prefect.filesystems import GCS
from prefect_gcp.cloud_run import CloudRunJob
from prefect.server.schemas.schedules import CronSchedule
from flow import demo_flow
import os
import sys

# Set absolute path to read other modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from blocks_gcp import flow_infra

def deploy_flow(flow_name: str):
    """
    Deploys the flow
    Args:
        flow_name: flow name 
    Return:
        None
    """
    
    # Sets up the task definition/infra
    infra_block = flow_infra.create_task_definition(flow_name)
    gcp_infra_block = CloudRunJob.load(infra_block)

    # Schedule if required
    flow_schedule = CronSchedule(cron="0 21 * * *", timezone="Pacific/Auckland")

    deployment = Deployment.build_from_flow(
        flow=demo_flow,
        name=f'deploy-{flow_name}',
        schedule=flow_schedule,
        is_schedule_active=False,
        version=1,
        work_queue_name='default',
        work_pool_name="agent-pool",
        infrastructure=gcp_infra_block,
        infra_overrides={
            "env.PREFECT_LOGGING_LEVEL": "DEBUG"
        }
    )
    deployment_id = deployment.apply()
    print(f'Deployment id - {deployment_id}, Flow name {flow_name}')

flow_name = "demo-flow-gcp"
deploy_flow(flow_name=flow_name)