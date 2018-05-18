import json

from kafka import KafkaConsumer
from pymongo import MongoClient


# Setup mongo connection
client = MongoClient()
db = client.metamorphosis
metamorphosis = db.metamorphosis

consumer = KafkaConsumer('metamorphosis')

for msg in consumer:
    msg_json = json.loads(msg.value)
    print(metamorphosis.insert_one(msg_json).inserted_id)
