from prefect_aws import ECSTask
import os

prefect_agent = ECSTask(
    cpu=512,
    memory=1024,
    command=["python", "/usr/app/src/currency_exchange/flow.py"],
    image=os.environ['ecr_image'],
    cluster=os.environ['cluster'],
    execution_role_arn=os.environ['execution_role_arn'],
    task_role_arn=os.environ['task_role_arn'],
    launch_type='FARGATE',
    task_start_timeout_seconds=600,
)
prefect_agent.save('prefect-agent', overwrite=True)