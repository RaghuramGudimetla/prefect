FROM --platform=linux/amd64 prefecthq/prefect:2-python3.10
ARG flow_name

RUN pip install prefect prefect-gcp

COPY /flows/${flow_name}/ /opt/prefect/flows/