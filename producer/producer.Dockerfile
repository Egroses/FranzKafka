FROM python:3.9

WORKDIR /app

RUN pip install --no-cache-dir kafka-python
RUN pip install --no-cache-dir pymongo

COPY producer.py .

CMD ["python", "producer.py"]