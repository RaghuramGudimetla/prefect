from prefect import task, flow, get_run_logger
from datetime import datetime
import requests
import json
import pytz
import boto3
# logger = get_run_logger()

def read_response_json_data(url: str) -> dict:
    """
    Read the raw data as json in requests
    Args:
        url (str): API url to get data
    """
    response_json = {}
    response_data = requests.get(url)
    response_json = json.loads(response_data.text)
    return response_json


@task
def export_exhange_rates():

    bucket_name = 'ap-southeast-2-886192468297-prefect'
    bucket_filename = datetime.now(pytz.timezone("Pacific/Auckland")).strftime('%Y%m%d') + '-nzd-currency.json'
    local_file_name = 'sample.json'

    s3 = boto3.resource("s3")
    bucket = s3.Bucket(bucket_name)

    nzd_currency_api = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/nzd.json"
    print(f"URL: {nzd_currency_api}")
    json_response = read_response_json_data(nzd_currency_api)
    nzd_conversion = json_response['nzd']

    with open(local_file_name, 'w') as f:
        json.dump(nzd_conversion, f)

    bucket.upload_file(local_file_name, f'currency_exchange/{bucket_filename}')
    print(f"File uploaded to S3 to {bucket_filename}")


@flow(
        flow_run_name=f'currency-exchange-{datetime.now().strftime("%m%d%Y")}',
        log_prints=True
    )
def export_nz_exhange():

    # Calling the task
    export_exhange_rates(return_state=True)

if __name__ == "__main__":
    export_nz_exhange()