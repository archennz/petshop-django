import sys
import queue
from cloudevents.http import CloudEvent
from cloudevents.conversion import to_binary, to_structured

attributes = {
    "type": "shipping",
    "source": "post-office.com"
}
data = {"order_id": sys.argv[1], "status": "DELIVERED"}
event = CloudEvent(attributes, data)
headers, body = to_structured(event)
queue.send_message(headers, body)
