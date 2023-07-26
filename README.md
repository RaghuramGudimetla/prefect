### Prefect Overview

 Prefect Version - 2.10.0

 Base Image - prefecthq/prefect:2-python3.10

 AWS Services Required:

    1. EC2 - To run the prefect agent (Or run locally).
    2. ECR - To store each flow code as image.
    3. ECS - To execute flow runs.

Make sure we configure below environment variables
    1. export ecr_image=""
    2. export cluster=""
    3. export execution_role_arn=""
    4. export task_role_arn=""
    5. export work_queue_name=""
    6. export PREFECT_AWS_ACCESS_KEY_ID=""
    7. export PREFECT_AWS_SECRET_ACCESS_KEY=""


### AWS Credentials
We need have a user that has access to push the code as image to ECR

### Infrastructure
We need infrastructure for each flow for its runs. We store it in an image.

### Agent Pool
Make sure the agent pool is created. I actually did it from UI. But can do it from python or command line.
    -- prefect work-pool create --type prefect-agent agent-pool

### Agent
Agent is a server that sends a flow run execution to ECS cluster with provided infrastructure
    -- prefect agent start -p 'agent-pool'

### Flow Deployment
Deploys the flow code and creates a block (Infra) that defines the flow run.


### Deployment steps
1. Make sure the AWS credentials are registered (This should have access to upload).
2. Make sure agent pool is already registered.
3. Start the Agent - (Either on EC2 or your local machine).
4. Build the image with the code and push the image to ECR.
    -- ./deploy_image.sh demo-flow $PREFECT_AWS_ACCESS_KEY_ID $PREFECT_AWS_SECRET_ACCESS_KEY
5. Above step will build a image locally and push it to ECR.
6. run deploy file in the respective flow to deploy the flow.
    python deploy.py


### AWS roles importance

### Execution role
This role is the for creating ECS tasks. This needs access like running tasks, creating task logs.

### Task role
This role is what we need access in our flow code. 
For instance, if we want to upload files to a bucket, read secrets, read SQS queue from flow. Then the task role must have access to do this.

### Notes
Make sure prefect-aws is installed on the machine where we run Agent