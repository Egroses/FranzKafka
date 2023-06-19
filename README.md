# FranzKafka

Simple CDC Application Development Project with Apache Kafka


## Project Description

Our CDC system is specifically designed to track and capture changes in a database in real-time, ensuring that all data modifications are constantly monitored and replicated across various systems and applications. By processing events related to insertions, updates, and deletions, our CDC solution offers a dependable and efficient method for synchronizing and replicating data, making it easier to integrate and analyze information from different sources.

## Project Functions

The key features of our CDC system include its ability to provide real-time monitoring of changes made to databases, as well as its capacity to capture and process events related to inserting, updating, and deleting data. Our solution also offers efficient and dependable data replication services that allow for seamless integration across multiple systems and support for various databases and data formats. In addition, our CDC system comes equipped with configurable event filtering and transformation capabilities, as well as robust error handling and data consistency mechanisms for enhanced reliability and security.

## Setup

1. Clone repository : "https://github.com/Egroses/FranzKafka.git" .
2. Install docker-desktop.
3. Build docker compose.
```
docker compose build
![start picture](https://github.com/Egroses/NinjaNindo/blob/main/Images/Start.png)
```

## Usage

1. Run docker compose.
```
docker compose up
![start picture](https://github.com/Egroses/NinjaNindo/blob/main/Images/Start.png)
```

2. Open second terminal and run:

```
docker compose exec producer python producer.py
![start picture](https://github.com/Egroses/NinjaNindo/blob/main/Images/Start.png)
```

2. Open third terminal and run:
```
docker compose exec consumer python consumer.py
![start picture](https://github.com/Egroses/NinjaNindo/blob/main/Images/Start.png)
```

4. Open fourth and last terminal, connect mongo and insert a document:

```
docker-compose exec mongodb mongosh
![start picture](https://github.com/Egroses/NinjaNindo/blob/main/Images/Start.png)
use myDatabase
![start picture](https://github.com/Egroses/NinjaNindo/blob/main/Images/Start.png)
db.myCollection.insertOne({"name": "Emirhan", "surname": "Gül"})
![start picture](https://github.com/Egroses/NinjaNindo/blob/main/Images/Start.png)
```

5. When new document inserted, you should see `A new document has been sent to kafka!` in second terminal and `A new document has been received!` in thirth terminal.
![results picture]([https://github.com/Egroses/NinjaNindo/blob/main/Images/Start.png](https://github.com/Egroses/FranzKafka/blob/main/Images/Results.png)https://github.com/Egroses/FranzKafka/blob/main/Images/Results.png)
