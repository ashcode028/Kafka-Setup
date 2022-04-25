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
## Producers and Consumers
Producers publish data to the topics of their choice. It is responsible for choosing which record to assign to which partition within the topic. This is usually done in a round-robin fashion or partitioning by a key or value.
Consumer groups can subscribe to one or more topics. Each one of these groups can be configured with multiple consumers.
Every message in a topic is delivered to one of the consumer instances inside the group subscribed to that topic. All messages with the same key arrive at the same consumer.
[Youtube link for better understanding](https://www.youtube.com/watch?v=R873BlNVUB4)
## Basic Setup
- Get the source code and docker images.
```
git clone https://github.com/wurstmeister/kafka-docker.git 
cd kafka-docker/
```
- If you want to run the code above from outside Kafka’s shell (outside a Docker container) , you need to expose docker network and kafka brokers , below is the docker image which allows us to create topics, producers outside kafka shell ,inside your application using APIs.
```
docker-compose -f docker-compose-expose.yml up
```
- To stop the docker
```
docker-compose stop
```
- Create a topic , this image by default creates one topic called 'topic_test'
- In your virtual environment, install kafka-python. Make sure when this is installed package 'kafka' isnt installed
```
pip install kafka-python
```
- In your application, wherever you want a notification , or any message has to passed send you producer instance as its argument and push into the queue. Create producer instance for each repository (if you have many),shown below
```
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
producer.send('<your topic name>', value=data)
```
In the code block above:
- We have created a KafkaProducer object that connects of our local instance of Kafka, this would be defined once for your one microservice.
- We have defined a way to serialize the data we want to send by trasforming it into a json string and then encoding it to UTF-8.
- We send an event  with topic named “topic_test”, this can be used in various parts of your microservice.

- Create another repository(in my opinion) to handle consumer.Otherwise it can be read from same microservice as producer. 
```
from kafka import KafkaConsumer
from json import loads
from time import sleep
# Create consumer instance
consumer = KafkaConsumer(
    'topic_test',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)
for event in consumer:
    event_data = event.value
    # Add your code to process messages in the queue.
    print(event_data)
    sleep(2)
```
In the script above:
- we are defining a KafkaConsumer that contacts the server “localhost:9092 ” and is subscribed to the topic “topic_test”. 
- Since in the producer script the message is jsonfied and encoded, here we decode it by using a lambda function in value_deserializer. In addition,
    - auto_offset_reset is a parameter that sets the policy for resetting offsets on OffsetOutOfRange errors; if we set “earliest” then it will move to the oldest available message, if “latest” is set then it will move to the most recent;
    - enable_auto_commit is a boolean parameter that states whether the offset will be periodically committed in the background;
    - group_id is the name of the consumer group to join.
### References:
https://www.youtube.com/watch?v=R873BlNVUB4
https://docs.confluent.io/platform/current/quickstart/ce-docker-quickstart.html
https://medium.com/big-data-engineering/hello-kafka-world-the-complete-guide-to-kafka-with-docker-and-python-f788e2588cfc
https://stackoverflow.com/questions/65196587/python-threads-and-queue-messages-between-them
https://github.com/dpkp/kafka-python/blob/master/example.py
https://developer.okta.com/blog/2020/01/22/kafka-microservices
https://towardsdatascience.com/kafka-docker-python-408baf0e1088
https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1

