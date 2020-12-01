import unittest
import datetime

from scripts import utils


class TestUtilsMethods(unittest.TestCase):

    def test_format_date(self):
        expected = datetime.datetime(2018, 8, 25)
        actual = utils.format_date('8/25/2018, 12:00 AM')
        assert actual == expected

    def test_format_time(self):
        expected = datetime.time(19, 55)
        actual = utils.format_time('07:55 PM')
        assert actual == expected
