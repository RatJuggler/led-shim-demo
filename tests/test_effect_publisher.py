from unittest import TestCase
from unittest.mock import patch
from testfixtures import LogCapture
import json
import logging

from ledshimdemo.effect_publisher import EffectPublisher


@patch('ledshimdemo.effect_subscriber.zmq.Context')
class TestEffectPublisher(TestCase):

    def setUp(self):
        pass

    def test_broadcast_effect_options(self, zmq_mock):
        dummy_options = dict(test_key1="value1", test_key2="value2")
        expected = "LEDSHIM-" + json.dumps(dummy_options)
        with LogCapture(level=logging.INFO) as log_out:
            publisher = EffectPublisher("127.0.0.1", 5556)
            publisher.broadcast_effect_option(dummy_options)
        log_out.check(('root', 'INFO', 'Starting effect publisher on: tcp://127.0.0.1:5556'),
                      ('root', 'INFO', 'Publishing: ' + expected))
        zmq_mock.return_value.socket.return_value.send_string.assert_called_once_with(expected)
