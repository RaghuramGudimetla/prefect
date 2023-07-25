from prefect_aws import ECSTask
import os
from prefect_aws import AwsCredentials

aws_creds = AwsCredentials.load("aws-creds")

prefect_agent = ECSTask(
    aws_credentials=aws_creds,
    cpu=512,
    memory=1024,
    image=os.environ['ecr_image'],
    type='ecs-task',
    cluster=os.environ['cluster'],
    execution_role_arn=os.environ['execution_role_arn'],
    task_role_arn=os.environ['task_role_arn'],
    configure_cloudwatch_logs=True,
    task_start_timeout_seconds=600,
    command=["python", "flow.py"]
)
prefect_agent.save('prefect-agent', overwrite=True)