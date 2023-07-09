##

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

prefect deployment build -n flow_experiment -q test flow_exp/flow_experiment.py:always_succeeds_flow -
