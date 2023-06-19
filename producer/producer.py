from kafka import KafkaProducer
from bson.json_util import dumps
from pymongo import MongoClient

import time
import pymongo
import json

kafka_bootstrap_servers = 'kafka:9092'
mongodb_uri = 'mongodb://mongodb:27017'
mongodb_database = 'myDatabase'
mongodb_collection = 'myCollection'

producer = None
client = None
db = None
collection = None
last_document = None


while True:
   try:
      if producer is None:
         producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers)
         
      if client is None:
         client = MongoClient(mongodb_uri)
         db = client[mongodb_database]
         collection = db[mongodb_collection]
      
      print("New documents waiting...")
      new_document = collection.find_one({}, sort=[('_id', pymongo.DESCENDING)])
      
      if new_document is not None:
         if last_document is None or new_document != last_document:
            message = dumps(new_document).encode('utf-8')
            print(f"A new document is {message} !")
            producer.send("myTopic", value=message)
            last_document = new_document
      
      time.sleep(10)
   except Exception as e:
      print("An error occurred:", str(e))
