# FranzKafka

Simple CDC Application Development Project with Apache Kafka


## Project Description

Our CDC system is specifically designed to track and capture changes in a database in real-time, ensuring that all data modifications are constantly monitored and replicated across various systems and applications. By processing events related to insertions, updates, and deletions, our CDC solution offers a dependable and efficient method for synchronizing and replicating data, making it easier to integrate and analyze information from different sources.

## Project Functions

The key features of our CDC system include its ability to provide real-time monitoring of changes made to databases, as well as its capacity to capture and process events related to inserting, updating, and deleting data. Our solution also offers efficient and dependable data replication services that allow for seamless integration across multiple systems and support for various databases and data formats. In addition, our CDC system comes equipped with configurable event filtering and transformation capabilities, as well as robust error handling and data consistency mechanisms for enhanced reliability and security.

## Setup

1. Clone repository : "https://github.com/Egroses/FranzKafka.git" 
2. Install docker-desktop.
3. Build docker compose.
```
docker compose build
```
![build picture](https://github.com/Egroses/FranzKafka/blob/main/Images/build.png)

## Usage

1. Run docker compose.
```
docker compose up
```
![run picture](https://github.com/Egroses/FranzKafka/blob/main/Images/run.png)

2. Open second terminal and run:

```
docker compose exec producer python producer.py
```
![producer picture](https://github.com/Egroses/FranzKafka/blob/main/Images/producer%26consumerRun.png)

2. Open thirth terminal and run:
```
docker compose exec consumer python consumer.py
```
![consumer picture](https://github.com/Egroses/FranzKafka/blob/main/Images/producer%26consumerRun.png)

4. Open fourth and last terminal, connect mongo and insert a document:

```
docker-compose exec mongodb mongosh
```
![MongoDB picture](https://github.com/Egroses/FranzKafka/blob/main/Images/mongoBuild.png)
```
use myDatabase
db.myCollection.insertOne({"name": "Emirhan", "surname": "Gül"})
```
![insert picture](https://github.com/Egroses/FranzKafka/blob/main/Images/insert.png)

5. You should see `A new document is :(document)` in thirth terminal and `New document detected: (document)!` in fourth terminal.
![results picture](https://github.com/Egroses/FranzKafka/blob/main/Images/Results.png)
