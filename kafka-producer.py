from time import sleep
from datetime import datetime
import json

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while 1:
    # kafkaesque is the name of the topic
    message = "Metamorphosis! {}".format(str(datetime.now().time()))
    message_dict = {}
    message_dict['meta_string'] = message
    producer.send('metamorphosis', json.dumps(message_dict).encode('utf-8'))
    sleep(1)
