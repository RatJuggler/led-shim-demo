from unittest import TestCase
from testfixtures import LogCapture
import logging
import mock

from effect_publisher import EffectPublisher


@mock.patch('ledshimdemo.effect_subscriber.zmq.Context')
class TestEffectPublisher(TestCase):

    def setUp(self):
        pass

    def test_broadcast_effect_options(self, zmq_mock):
        dummy_options = dict(test_key1="value1", test_key2="value2")
        expected = 'LEDSHIM-{"test_key1": "value1", "test_key2": "value2"}'
        with LogCapture(level=logging.INFO) as log_out:
            publisher = EffectPublisher("127.0.0.1", 5556)
            publisher.broadcast_effect_option(dummy_options)
        log_out.check(('root', 'INFO', 'Starting effect publisher on: tcp://127.0.0.1:5556'),
                      ('root', 'INFO', 'Publishing: LEDSHIM-{"test_key1": "value1", "test_key2": "value2"}'))
        zmq_mock.return_value.socket.return_value.send_string.assert_called_once_with(expected)
