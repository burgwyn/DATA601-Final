import unittest
import datetime

from scripts import utils


class TestUtilsMethods(unittest.TestCase):

    def format_date(self):
        expected = datetime.datetime(2018, 8, 25)
        actual = utils.format_date('8/25/2018, 12:00 AM')
        assert actual == expected
