# Pre steps
Store all the environment variables in the virtual environment /Scripts/activate

1. Flow context is also defined here as a function. So, flows are literally functions now

### Cloud login
Can login using the API key
prefect cloud login -k xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-- Authenticated with Prefect Cloud! Using workspace 'raghuramgudimetlatrademeconz/gettingused'. --

### Events
Cloud events can be used for observability. Like an event when we query database, or push to a bucket.

### Flow context
Good to use flow-run-name with something like -- @flow(flow_run_name="{name}-on-{date:%A}")
Separate all the logic into tasks. Never write any logic in the flow function.
Not good to call tasks inside task.
Return multiple states. Always good to return states of each tasks. To make sure how many of them are failed.
Anything else returned is considered as a success.

### Tasks
Main use is that we can make these tasks dependent.
Each task should ideally represent a single logic.
Not a good practice to call a task from another task. But, you can still do it using task_1.fn().
Good to write a description to task.
If we are going to run any costly tasks, better to use caching. Caching is good. But, make sure if we are passing the same parameter values, it always uses cached results.

### Deployment
Each deployment is associated with a single flow, but any given flow can be referenced by multiple deployments.

#### Using CLI
prefect deployment build -n task_experiment -q test task_experiment/task_experiments.py:task_experiments

#### Creating storage blocks
We can create blocks that stored the flow code in S3

#### GCP deployment
https://medium.com/@danilo.drobac/7-a-complete-google-cloud-deployment-of-prefect-2-0-32b8e3c2febe
#### AWS deployment
https://towardsdatascience.com/prefect-aws-ecs-fargate-github-actions-make-serverless-dataflows-as-easy-as-py-f6025335effc
https://github.com/anna-geller/dataflow-ops/tree/main
https://www.youtube.com/watch?v=q-sl6bzi5fw
https://github.com/PrefectHQ/prefect-recipes/blob/main/devops/infrastructure-as-code/aws/tf-prefect2-ecs-agent/main.tf


### Notes to make for success run

1. Make sure we have a work pool created (Keep the queue name as default)
2. Start the agent (Make sure we install prefect-aws from the environment we are running it)
3. Deploy 
    1. AWS Credentials
    2. Storage Block
    3. Infrastructure block (ESCTask)
4. Deploy the flow
5. Make sure the work pool is fine.
6. Run the flow from prefect cloud.