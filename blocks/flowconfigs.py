from prefect.filesystems import S3
import os

"""
This is block
block = S3(bucket_path="ap-southeast-2-886192468297-prefect/flowconfigs", 
           aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], 
           aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
)
block.save("flowconfigs")
"""

def flow_bucket_path(flow_name: str) -> S3:
    """
    Function to return the block name to do a flow deployment
    Args:
        flow_name (str): flow name to create a subfolder for the source code
    Return:
        S3 object
    """
    block = S3(bucket_path=f"ap-southeast-2-886192468297-prefect/flowconfigs/{flow_name}", 
                aws_access_key_id=os.environ['PREFECT_AWS_ACCESS_KEY_ID'], 
                aws_secret_access_key=os.environ['PREFECT_AWS_SECRET_ACCESS_KEY']
            )
    return block


def create_flow_storage_block(flow_name: str) -> bool:
    """
    Function to create a storage block for the flow run
    Args:
        flow_name (str): flow name to create a storage block for
    """
    block = S3(
           bucket_path=f"ap-southeast-2-886192468297-prefect/flowconfigs/{flow_name}", 
           aws_access_key_id=os.environ['PREFECT_AWS_ACCESS_KEY_ID'], 
           aws_secret_access_key=os.environ['PREFECT_AWS_SECRET_ACCESS_KEY']
    )
    block.save(f"storage-{flow_name}", overwrite=True)
    return True