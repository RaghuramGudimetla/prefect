from prefect_aws import ECSTask
import os
from prefect_aws import AwsCredentials

def create_task_definition(flow_name: str):
    """
    Create task definition for the flow run
    Args:
        flow_name: flow name 
    Return:
        None
    """
    aws_creds = AwsCredentials.load("aws-creds")
    task_definition_block_name = f'{flow_name}-infra'
    prefect_agent = ECSTask(
        aws_credentials=aws_creds,
        cpu=512,
        memory=1024,
        image=f"886192468297.dkr.ecr.ap-southeast-2.amazonaws.com/{flow_name}:latest",
        type='ecs-task',
        cluster=os.environ['cluster'],
        execution_role_arn=os.environ['execution_role_arn'],
        task_role_arn=os.environ['task_role_arn'],
        configure_cloudwatch_logs=True,
        task_start_timeout_seconds=600
    )
    prefect_agent.save(f'{task_definition_block_name}', overwrite=True)
    return task_definition_block_name