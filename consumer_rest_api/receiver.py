import pika
from django.conf import settings
import threading
from . import models

RABBITMQ_HOST = getattr(settings, "RABBITMQ_HOST", '127.0.0.1')
RABBITMQ_QUEUE = 'rabittmq.test.queue'
connection = None
channel = None

def receive():
    print(' In the section received....')
    global connection,channel
    if connection != None and channel != None:
        return
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=RABBITMQ_HOST))
        channel = connection.channel()

        channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
        channel.basic_consume(on_message_receive, queue=RABBITMQ_QUEUE, no_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
    except:
        print('connection error!!!')
        threading.Timer(15.0, receive).start()
        return

def on_message_receive(ch, method, properties, body):
        models.ConsumerServiceMessages.create(message = body)
        print(" [x] Received %r" % body)
        ch.basic_ack(delivery_tag = method.delivery_tag)

def start():
    receive()