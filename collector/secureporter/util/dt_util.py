from datetime import datetime, timedelta

def datetime_parse(start, end):
    if start is not None:
        datetime_start = datetime.strptime(start, '%Y-%m-%d')
    else:
        datetime_start = set_to_midnight(datetime.today())
    if end is not None:
        datetime_end = datetime.strptime(end, '%Y-%m-%d')
    else:
        datetime_end = datetime_start + timedelta(days=1)

    return datetime_start, datetime_end

def set_to_midnight(dt):
    return dt.replace(hour=0, minute=0, second=0, microsecond=0)

def set_precision_to_second(dt):
    return dt.replace(microsecond=0)
