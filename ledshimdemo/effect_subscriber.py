import zmq


class EffectSubscriber:

    TOPIC = "LEDSHIM-"

    def __init__(self, ip_address: str, port: int) -> None:
        self.ip_address = ip_address
        self.port = port

    def get_effect_options(self) -> str:
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.setsockopt_string(zmq.SUBSCRIBE, self.TOPIC)
        print("Connecting to publisher....")
        socket.connect("tcp://{0}:{1}".format(self.ip_address, self.port))
        try:
            while True:
                print("Waiting for message...")
                message = socket.recv_string()
                if message.startswith(self.TOPIC):
                    print("Message received: {0}".format(message))
                    return message
        finally:
            socket.close()
            context.term()
