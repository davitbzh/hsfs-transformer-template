from datetime import datetime

def plus_one(value):
    return value + 1

def date_string_to_timestamp(input_date):
    date_format = "%Y%m%d%H%M%S"
    return int(float(datetime.strptime(input_date, date_format).timestamp()) * 1000)

