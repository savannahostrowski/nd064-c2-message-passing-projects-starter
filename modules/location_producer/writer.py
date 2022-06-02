import grpc
import location_pb2
import location_pb2_grpc

"""
This is sample code to simulate writing messages to gRPC
"""

print("Sending sample payload")
channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

location = location_pb2.LocationMessage(
    person_id="1",
    latitude= "47.7244653",
    longitude="-122.2248416"
)

response = stub.Create(location)