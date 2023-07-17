FROM prefecthq/prefect:2-python3.11
RUN pip install s3fs prefect-aws awswrangler

WORKDIR /usr/app/src
COPY flows/currency_exchange/ /usr/app/src/

CMD [ "python", "/usr/app/src/currency_exchange/flow.py" ]