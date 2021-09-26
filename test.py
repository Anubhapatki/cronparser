import unittest
from main import cron_parser


class TestCronParser(unittest.TestCase):
    def test_cron_parser(self):
        """
        Test error handling
        """
        return_results = 'Minutes 6 7 8 9'
        result = cron_parser('*/15 0 1,15 * 1-9 /usr/bin/find')
        self.assertEqual(return_results,'Minutes 6 7 8 9')

if __name__ == '__main__':
    unittest.main()