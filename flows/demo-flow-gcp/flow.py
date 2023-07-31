from prefect import task, flow

@task()
def demo_task():
    print("This is running fine")


@flow(log_prints=True)
def demo_flow():
    # Calling the task
    demo_task(return_state=True)

if __name__ == "__main__":
    demo_flow()