from prefect_gcp import GcpCredentials

with open("../prefect-sa.json") as f:
    service_account = f.read()

block = GcpCredentials(
    service_account_info=service_account,
    project="raghuram-exec"
)
block.save("gcp-credentials", overwrite=True)