from prefect.filesystems import S3
import os

"""
block = S3(bucket_path="ap-southeast-2-886192468297-prefect/flowconfigs", 
           aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], 
           aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
)
block.save("flowconfigs")
"""

def flow_bucket_path(flow_name: str) -> S3:
    block = S3(bucket_path=f"ap-southeast-2-886192468297-prefect/flowconfigs/{flow_name}", 
                aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], 
                aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
            )
    return block