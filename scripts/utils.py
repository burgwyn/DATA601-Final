from dateutil.parser import parse


def format_date(date_str):
    return parse(date_str)


def format_time(time_str):
    return parse(time_str).time()

def display_scores(name, scores):
    print(name)
    print('Mean:', scores.mean())
    print('Standard deviation:', scores.std())
