from tkinter import TOP
from kafka import KafkaConsumer
TOPIC_NAME = 'location'

consumer = KafkaConsumer(TOPIC_NAME)
while True:
    for message in consumer:
         
