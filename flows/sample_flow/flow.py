from prefect import task, flow

@task(log_prints=True)
def sample_task():
    print("This is running fine")


@flow(
        flow_run_name=f'just-run-mate',
        log_prints=True
    )
def sample_flow():

    # Calling the task
    sample_task(return_state=True)

if __name__ == "__main__":
    sample_task()