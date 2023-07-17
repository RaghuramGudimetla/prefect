from prefect.deployments import Deployment
from flow import export_nz_exhange
from prefect_aws.ecs import ECSTask
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../..')) )
from blocks.flowconfigs import flow_bucket_path

ecs_task_block = ECSTask.load("prefect-agent")

#storage = S3.load("flowconfigs") # load a pre-defined block
flow_name = "currency-exchange"

deployment = Deployment.build_from_flow(
    flow=export_nz_exhange,
    name=f'deploy-{flow_name}',
    version=1,
    work_queue_name=os.environ['work_queue_name'],
    work_pool_name="default-agent-pool",
    storage=flow_bucket_path(flow_name),
    infrastructure=ecs_task_block,
    ignore_file='.prefectignore'
)

deployment.apply()