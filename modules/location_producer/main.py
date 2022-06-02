import json
import time
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc

from kafka import KafkaProducer



class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        request_value = {
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude
        }
        print(request_value)
        kafka_topic = 'locations'
        kafka_server = 'localhost:9892'
        producer = KafkaProducer(bootstrap_servers=kafka_server)
        producer.send(kafka_topic, json.dumps(request_value).encode())
        producer.flush()
        return location_pb2.LocationMessage(**request_value)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)

print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()

# To keep the thread alive...
try: 
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)