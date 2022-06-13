import time
import grpc
import json
import location_pb2
import location_pb2_grpc
from concurrent import futures
from kafka import KafkaProducer

class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request):
       request_value = {
            "person_id":request.person_id,
            "creation_time":request.creation_time,
            "latitude": str(request.latitude),
            "longitude": str(request.longitude)
        }
       kafka_topic = 'locations'
       kafka_server = '10.42.0.56:9092'
       producer = KafkaProducer(bootstrap_servers=kafka_server)
       producer.send(kafka_topic, json.dumps(request_value).encode())
       producer.flush()
       return location_pb2.LocationMessage(**request_value)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)

print("Server starting on port 5001...")
server.add_insecure_port("[::]:5001")
server.start()

# To keep the thread alive...
try: 
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)