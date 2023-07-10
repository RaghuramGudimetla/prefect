from prefect.deployments import Deployment
from prefect.filesystems import S3

import os
import sys

f = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Path to import gpnexporter
sys.path.append(str(f))

from flows.currency_exchange import export_nz_exhange
from blocks.flowconfigs import flow_bucket_path

#storage = S3.load("flowconfigs") # load a pre-defined block
flow_name = "currency-exchange"

deployment = Deployment.build_from_flow(
    flow=export_nz_exhange,
    name=flow_name,
    version=1,
    work_queue_name="aws",
    work_pool_name="default-agent-pool",
    storage=flow_bucket_path(flow_name)
)

deployment.apply()
print(deployment)