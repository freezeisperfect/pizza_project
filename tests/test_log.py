import unittest
from unittest.mock import patch
from modules.log import log


class TestLog(unittest.TestCase):
    @patch('builtins.print')
    def test_log_decorator_print(self, mock_print):
        @log('Testing log here: {}')
        def test_foo():
            return 'Test foo actions here'

        test_foo()

        self.assertTrue(mock_print.called)

    @patch('builtins.print')
    def test_log_decorator_expected_result(self, mock_print):
        expected_output = 'Test log'

        @log(expected_output)
        def test_foo():
            return 'Test foo actions here'

        test_foo()

        printed_args = [
            call_args[0][0] for call_args in mock_print.call_args_list
        ]
        self.assertEqual(printed_args, [expected_output])


if __name__ == '__main__':
    unittest.main()
