import json
import logging
import time
import zmq


class EffectPublisher:

    TOPIC = "LEDSHIM-"

    def __init__(self, ip_address: str, port: int) -> None:
        self.ip_address = ip_address
        self.port = port

    def _publish_message(self, message: str) -> None:
        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        bind_to = "tcp://{0}:{1}".format(self.ip_address, self.port)
        logging.info("Starting effect publisher on: {0}".format(bind_to))
        socket.bind(bind_to)
        time.sleep(1)  # Sleeping to delay the publisher is not generally considered best practice.
        try:
            logging.info("Publishing: {0}".format(message))
            socket.send_string(message)
        finally:
            socket.close()
            context.term()

    def broadcast_effect_option(self, options: dict):
        message = self.TOPIC + json.dumps(options)
        self._publish_message(message)
