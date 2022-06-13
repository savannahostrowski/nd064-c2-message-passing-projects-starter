import location_pb2 
from kafka import KafkaConsumer
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2.functions import ST_Point
from models import Location
import logging

logging.basicConfig(level=logging.DEBUG)
TOPIC_NAME = 'location'
KAFKA_SERVER = '10.42.0.56:9092'
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[KAFKA_SERVER])

db = SQLAlchemy()
while True:
    try:
        for message in consumer:
            location = location_pb2.LocationMessage()
            location.ParseFromString(message.value)
            new_location = Location()
            new_location.person_id = location["person_id"]
            new_location.creation_time = location["creation_time"]
            new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
            db.session.add(new_location)
            db.session.commit()
 
    except:
        print("")
    finally:
        consumer.close()
