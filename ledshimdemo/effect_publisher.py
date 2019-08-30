import json
from multiprocessing import Process, Queue
from queue import Empty
import time
import zmq

from .configure_logging import logging


def check_queue(queue) -> str:
    try:
        task = queue.get_nowait()
        return task
    except Empty:
        return None


def publisher(ip_address: str, port: int, queue: Queue) -> None:
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    bind_to = "tcp://{0}:{1}".format(ip_address, port)
    logging.info("Starting effect publisher on: {0}".format(bind_to))
    socket.bind(bind_to)
    try:
        publish_message = None
        while True:
            message = check_queue(queue)
            if message == "STOP":
                break
            if message:
                publish_message = message
            if publish_message:
                logging.info("Publishing: {0}".format(publish_message))
                socket.send_string(publish_message)
            time.sleep(1)
    finally:
        socket.close()
        context.term()


class EffectPublisher:

    TOPIC = "LEDSHIM-"

    def __init__(self, ip_address: str, port: int) -> None:
        self.ip_address = ip_address
        self.port = port
        self.queue = Queue()
        self.publisher = None

    def start(self) -> None:
        self.publisher = Process(target=publisher, args=(self.ip_address, self.port, self.queue,))
        self.publisher.start()

    def publish(self, message: dict) -> None:
        string = self.TOPIC + json.dumps(message)
        self.queue.put_nowait(string)

    def stop(self) -> None:
        logging.info("Waiting for effect publisher to stop...")
        self.queue.put("STOP")
        self.publisher.join()
        logging.info("Effect publisher stopped.")
        self.queue.close()

    def _publish_message(self, message: str) -> None:
        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        bind_to = "tcp://{0}:{1}".format(self.ip_address, self.port)
        logging.info("Starting effect publisher on: {0}".format(bind_to))
        socket.bind(bind_to)
        time.sleep(1)
        try:
            logging.info("Publishing: {0}".format(message))
            socket.send_string(message)
        finally:
            socket.close()
            context.term()

    def broadcast_effect_option(self, options: dict):
        message = self.TOPIC + json.dumps(options)
        self._publish_message(message)
