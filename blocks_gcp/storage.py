from prefect.filesystems import GCS

with open("../prefect-sa.json") as f:
    service_account = f.read()

block = GCS(
    bucket_path="raghuram-exec-prefect-data/storage/",
    service_account_info=service_account,
    project="raghuram-exec"
)
block.save("gcp-storage", overwrite=True)