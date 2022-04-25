from kafka import KafkaConsumer
from time import sleep
from json import loads
consumer = KafkaConsumer(
    'topic_test',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))
for event in consumer:
    event_data = event.value
    # Do whatever you want
    print(event_data)
    sleep(2)