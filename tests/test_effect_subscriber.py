from unittest import TestCase
from testfixtures import LogCapture
import logging
import mock

from effect_subscriber import EffectSubscriber


@mock.patch('ledshimdemo.effect_subscriber.zmq.Context')
class TestEffectSubscriber(TestCase):

    def setUp(self):
        pass

    def test_get_effect_options(self, zmq_mock):
        dummy_return = 'LEDSHIM-{"test_key1": "value1", "test_key2": "value2"}'
        zmq_mock.return_value.socket.return_value.recv_string.return_value = dummy_return
        expected = dict(test_key1="value1", test_key2="value2")
        with LogCapture(level=logging.INFO) as log_out:
            subscriber = EffectSubscriber("127.0.0.1", 5556)
            options = subscriber.get_effect_options()
            self.assertEqual(options, expected)
        log_out.check(('root', 'INFO', 'Connecting to publisher at: tcp://127.0.0.1:5556'),
                      ('root', 'INFO', 'Waiting for effect options from publisher...'),
                      ('root', 'INFO', 'Message received from publisher: ' + dummy_return))
        zmq_mock.assert_called_once()
