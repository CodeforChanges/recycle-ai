import json
import sys
import traceback
import pika
from recycle_ai.exception.model_runtime_error import ModelRuntimeError


class MessageQueue:
    def __init__(self, url, model):
        print("[INFO] initialize message qeueu")

        # Set member variables
        try:
            self.model = model
            self.conn = pika.BlockingConnection(pika.URLParameters(url))
            self.channel = self.conn.channel()
        except:
            print("[ERROR] cannot connect message queue server (check the URL)")
            traceback.print_exc()
            sys.exit(1)

        # Define queues
        self.channel.queue_declare(queue="garbage_classification_requests")
        self.channel.queue_declare(queue="garbage_classification_results")

        # Set callback method
        self.channel.basic_consume(
            queue="garbage_classification_requests",
            auto_ack=True,
            on_message_callback=self.__garbage_classification_requests__,
        )

    def __del__(self):
        print("[WARN] message queue was destroyed")

        if self.channel:
            self.channel.close()

        if self.conn:
            self.conn.close()

    def start_consuming(self):
        print("[INFO] start consuming ...")
        self.channel.start_consuming()

    def __garbage_classification_requests__(self, channel, method, properties, body):
        print("[INFO] pop request from message queue")

        try:
            body = json.loads(body)
            body["result"] = self.model.expect(body["data"])
        except ModelRuntimeError:
            body["result"] = "ERROR: Model Runtime Error"

            print("[ERROR] model runtime error")
            traceback.print_exc()

        body = json.dumps(body)
        channel.basic_publish(
            exchange="", routing_key="garbage_classification_results", body=body
        )
        print("[INFO] push result to message queue")
