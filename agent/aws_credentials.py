from prefect_aws import AwsCredentials
import os

AwsCredentials(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], 
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    aws_session_token=None,
    region_name="ap-southeast-2"
).save("aws-creds")