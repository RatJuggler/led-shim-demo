from multiprocessing import Process, Queue
from queue import Empty
import time

from .configure_logging import logging


def check_queue(queue):
    try:
        task = queue.get_nowait()
        return task
    except Empty:
        return "EMPTY"


def publisher(ip_address: str, port: int, queue: Queue) -> None:
    while True:
        message = check_queue(queue)
        if message == "STOP":
            break
        if message == "EMPTY":
            print("Publisher: Idling...")
        else:
            print("Publisher: {0}".format(message))
        time.sleep(0.5)


class EffectPublisher:

    def __init__(self, ip_address: str, port: int) -> None:
        self.ip_address = ip_address
        self.port = port
        self.queue = Queue()
        self.publisher = None

    def start(self):
        logging.info("Starting effect publisher...")
        self.publisher = Process(target=publisher, args=(self.ip_address, self.port, self.queue,))
        self.publisher.start()

    def publish(self, message: str):
        self.queue.put_nowait(message)

    def stop(self):
        logging.info("Waiting for effect publisher to stop...")
        self.queue.put("STOP")
        self.publisher.join()
        logging.info("Effect publisher stopped.")
        self.queue.close()
