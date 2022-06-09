import json

from kafka import KafkaProducer
from flask import Flask, jsonify, request, g, Response

from .services import retrieve_orders, create_order

app = Flask(__name__)

@app.before_request
def before_request():
    # Set up a Kafka producer
    TOPIC_NAME = 'items'
    KAFKA_SERVER = 'localhost:9092'
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
    # Setting Kafka to g enables us to use this
    # in other parts of our application
    g.kafka_producer = producer