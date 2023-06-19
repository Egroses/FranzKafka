FROM python:3.9

WORKDIR /app

RUN pip install --no-cache-dir kafka-python

COPY consumer.py .

CMD ["python", "consumer.py"]
