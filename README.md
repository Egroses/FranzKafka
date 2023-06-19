# CDC with Apache Kafka and Mongo

Change Data Capture with Apache Kafka and Mongo using docker containers.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Description

This project is a Change Data Capture (CDC) system designed to capture and track real-time data changes in a database. It provides a reliable and efficient way to monitor and replicate data changes across multiple systems or applications. By capturing and processing database events such as inserts, updates, and deletes, our CDC system enables seamless data synchronization and replication, facilitating data integration and analysis.

## Features

- Real-time monitoring of database changes.
- Capturing and processing of insert, update, and delete events.
- Efficient and reliable data replication between different systems.
- Support for various databases and data formats.
- Configurable event filtering and transformation capabilities.
- Robust error handling and data consistency mechanisms.

## Installation

1. Install docker-desktop.
2. Clone repository.

```
git clone https://github.com/hukumrat/cdc.git
```

3. Move to cdc folder.

```
cd cdc
```

3. Run docker compose.

```
docker-compose up
```

4. When you see `Kafka Server started` on terminal it's done!

## Usage

1. Open a terminal in cdc folder and run docker compose.

```
docker-compose up
```

2. Open second terminal in cdc folder and run:

```
docker-compose exec producer python producer.py
```

```
docker-compose exec consumer python consumer.py
```

4. Open fourth and last terminal, connect mongo and insert a document:

```
docker-compose exec mongodb mongosh
use myDatabase
db.myCollection.insertOne({"name": "Emirhan", "surname": "Gül"})
```

5. When new document inserted, you should see `A new document has been sent to kafka!` in second terminal and `A new document has been received!` in thirth terminal.

## Contributing

Thank you for considering contributing to this project! Contributions are welcome and appreciated. To contribute, please follow these guidelines:

1. Fork the repository and clone it to your local machine.
2. Create a new branch for your feature or bug fix: git checkout -b feature/your-feature or git checkout -b bugfix/your-bugfix.
3. Make your changes and ensure that your code follows the project's coding style and guidelines.
4. Commit your changes with a descriptive commit message: git commit -m "Add feature: your feature description" or git commit -m "Fix: description of the bug fix".
5. Push your branch to your forked repository: git push origin feature/your-feature or git push origin bugfix/your-bugfix.
6. Open a pull request against the main branch of the original repository.
7. Provide a clear description of the changes you have made in the pull request.
8. Be responsive to any feedback or suggestions for improvements.

Please note that all contributions are subject to review and may require some changes or improvements before being merged into the main project.

By contributing to this project, you agree to license your contributions under the project's chosen license.

Thank you for your valuable contributions!

Feel free to customize these guidelines based on your specific project requirements or workflow.

## License

This project is licensed under the license found in the LICENSE file in the root directory of this source tree.

## Contact

For help or issues using the pre-trained models, please submit a GitHub issue.

For other communications, please contact [Hükümdar](hkmdrfrtt@gmail.com).
