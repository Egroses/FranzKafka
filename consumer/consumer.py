from kafka import KafkaConsumer

for message in KafkaConsumer('myTopic', bootstrap_servers='kafka:9092'):
    print(f"New document detected: {message.value.decode('utf-8')}")
