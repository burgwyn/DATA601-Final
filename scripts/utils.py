from dateutil.parser import parse


def test_format_date(date_str):
    return parse(date_str)
