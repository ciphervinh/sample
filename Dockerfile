FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

COPY . /app

CMD uvicorn validate:app --host 0.0.0.0 --port 443 --ssl-keyfile=./webhook.key --ssl-certfile=./webhook.crt