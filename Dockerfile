FROM python:3.8

ENV RECYCLE_AI_MQ_URL amqp://guest:guest@rabbitmq:5672/

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install -e .

ENTRYPOINT ["reai"]
