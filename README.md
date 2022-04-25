# Inter APIs communication using Kafka
![](https://github.com/ashcode028/Kafka_setup/blob/2527475449c7a53334c3e982204e6cea4b0d4bb1/kakfa.jpg)

For a complete guide, the [Kafka documentation](https://kafka.apache.org/documentation.html) does an excellent job. Below is just a quick overview.

Also, there is [confluent platform](https://docs.confluent.io/platform/current/quickstart/ce-docker-quickstart.html), which makes your job easier if you want GUI rather than terminal mode.

Here, we talk only about terminal mode where we start kafka using prebuild docker image.

## Pub/Sub system
Apache Kafka is a distributed publish-subscribe messaging system that is designed to be fast, scalable, and durable.
Kafka stores streams of records (messages) in topics. Each record consists of a key, a value, and a timestamp.
Producers write data to topics and consumers read from topics.
## Topics and Logs
A topic is a category to which records are published. It can have zero, one, or many consumers that subscribe to the data written to it.
For each topic, the Kafka cluster maintains a partitioned log. Since Kafka is a distributed system, topics are partitioned and replicated across multiple nodes.
### Producers and Consumers
Producers publish data to the topics of their choice. It is responsible for choosing which record to assign to which partition within the topic. This is usually done in a round-robin fashion or partitioning by a key or value.
Consumer groups can subscribe to one or more topics. Each one of these groups can be configured with multiple consumers.
Every message in a topic is delivered to one of the consumer instances inside the group subscribed to that topic. All messages with the same key arrive at the same consumer.
[Youtube link for better understanding](https://www.youtube.com/watch?v=R873BlNVUB4)
## Basic Setup
- git clone https://github.com/wurstmeister/kafka-docker.git 
- cd kafka-docker/
- docker-compose -f docker-compose-expose.yml up
- docker-compose stop
### References:
- [1](https://stackoverflow.com/questions/65196587/python-threads-and-queue-messages-between-them)
- [2](https://github.com/dpkp/kafka-python/blob/master/example.py)
- [3](https://developer.okta.com/blog/2020/01/22/kafka-microservices)
- [4](https://www.youtube.com/watch?v=R873BlNVUB4)
- [5](https://docs.confluent.io/platform/current/quickstart/ce-docker-quickstart.html)
- [6](https://medium.com/big-data-engineering/hello-kafka-world-the-complete-guide-to-kafka-with-docker-and-python-f788e2588cfc)
- [7](https://towardsdatascience.com/kafka-docker-python-408baf0e1088)
- [8](https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1)
