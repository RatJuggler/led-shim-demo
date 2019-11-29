from unittest import TestCase
from unittest.mock import patch
from testfixtures import LogCapture
import json
import logging

from ledshimdemo.effect_subscriber import EffectSubscriber


@patch('ledshimdemo.effect_subscriber.zmq.Context')
class TestEffectSubscriber(TestCase):

    def setUp(self):
        pass

    def test_get_effect_options(self, zmq_mock):
        dummy_options = dict(test_key1="value1", test_key2="value2")
        expected = "LEDSHIM-" + json.dumps(dummy_options)
        zmq_mock.return_value.socket.return_value.recv_string.return_value = expected
        with LogCapture(level=logging.INFO) as log_out:
            subscriber = EffectSubscriber("127.0.0.1", 5556)
            options = subscriber.get_effect_options()
            self.assertEqual(options, dummy_options)
        log_out.check(('root', 'INFO', 'Connecting to publisher at: tcp://127.0.0.1:5556'),
                      ('root', 'INFO', 'Waiting for effect options from publisher...'),
                      ('root', 'INFO', 'Message received from publisher: ' + expected))
        zmq_mock.assert_called_once()
