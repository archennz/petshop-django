import sys
import os
import json
from queue import receive_message


def main():
    # what is the concept of channel in rabbitmq

    def callback(ch, method, properties, body):
        message = json.loads(body.decode())
        order_id = message['data']['order_id']
        print(f" [x] Received {order_id}")
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    receive_message(callback)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)