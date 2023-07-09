from prefect import task, flow
from datetime import datetime

@task
def just_return(val: int = 0):
    return f"Succes and value is {val}"

@task
def wait_task():
    return "success"

@flow(flow_run_name=f'task-experiment-{datetime.now().strftime("%m-%d-%Y-%H-%M-%S")}')
def task_experiments():

    multi_call = just_return.map([5, 6])

if __name__ == "__main__":
    task_experiments()