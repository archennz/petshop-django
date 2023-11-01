import pika

QUEUE_NAME = 'hello'


def send_message(headers, body):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)

    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=body)
    print(f" [x] Sent {body}")
    connection.close()


def receive_message(callback):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()