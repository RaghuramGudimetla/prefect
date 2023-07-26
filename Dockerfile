FROM --platform=linux/amd64 prefecthq/prefect:2-python3.10
ARG flow_name

RUN pip install prefect s3fs awswrangler prefect-aws prefect-docker boto3 requests

WORKDIR /usr/app/src
COPY flows/${flow_name}/ /opt/prefect/flows/