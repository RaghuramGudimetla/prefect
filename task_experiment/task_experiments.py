from prefect import task, flow
from datetime import datetime
from prefect.deployments import Deployment


@task
def just_return(val: int = 0):
    return f"Succes and value is {val}"

@task
def wait_task():
    return "success"

@flow(flow_run_name=f'task-experiment-{datetime.now().strftime("%m-%d-%Y-%H-%M-%S")}')
def task_experiments():

    # Three types we can call a task
    state = just_return(return_state=True)
    future = just_return.submit()
    value = just_return()

    # Wait for a task
    wait_ex = wait_task(wait_for=[value])

if __name__ == "__main__":
    task_experiments()