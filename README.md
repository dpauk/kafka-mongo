# Kafka-Mongo

A very simple project showing the addition of a message to a Kafka topic, the consumption of the same message and the insertion of that message into MongoDB.

Startup:
1. Start mongo: ```mongod```
2. Start the Kafka server: ```kafka-server-start /usr/local/etc/kafka/server.properties```
3. Create the Kafka topic: ```kafka-topics --list --zookeeper localhost --topic metamorphosis```
4. Start the producer: ```python kafka-producer```
5. Start the consumer: ```python kafka-consumer```
