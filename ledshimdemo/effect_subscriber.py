import json
import zmq


class EffectSubscriber:

    TOPIC = "LEDSHIM-"

    def __init__(self, ip_address: str, port: int) -> None:
        self.ip_address = ip_address
        self.port = port

    def _wait_for_message(self, topic) -> str:
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.setsockopt_string(zmq.SUBSCRIBE, topic)
        print("Connecting to publisher....")
        socket.connect("tcp://{0}:{1}".format(self.ip_address, self.port))
        try:
            while True:
                print("Waiting for message...")
                message = socket.recv_string()
                if message.startswith(topic):
                    print("Message received: {0}".format(message))
                    return message
        finally:
            socket.close()
            context.term()

    def get_effect_options(self) -> dict:
        message = self._wait_for_message(self.TOPIC)
        return json.loads(message[len(self.TOPIC):])
