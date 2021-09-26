import unittest
from parser import parse_string

class TestCronParser(unittest.TestCase):
    def test_cron_parser_interval(self):
        """
        Test 
        """
        result = parse_string('*/15', 'minute')
        self.assertEqual(result,'0 15 30 45')
    def test_cron_parser_all(self):
        """
        Test 
        """
        result = parse_string('*', 'hour')
        self.assertEqual(result,'0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23')

if __name__ == '__main__':
    unittest.main()