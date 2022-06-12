import location_pb2 
from kafka import KafkaConsumer
from app import db
from geoalchemy2.functions import ST_Point

from modules.location_consumer.app.udaconnect.models import Location

TOPIC_NAME = 'location'
KAFKA_SERVER = 'kafka.default.svc.cluster.local'
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)

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
