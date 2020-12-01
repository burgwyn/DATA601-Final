from dateutil.parser import *


def test_format_date(date_str):
    return parse(date_str)
