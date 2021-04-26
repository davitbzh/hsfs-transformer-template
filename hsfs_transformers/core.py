import numpy as np
import pandas as pd
from datetime import datetime

def plus_one(value):
      return value + 1

def get_timestamp_from_date_string(input_date):
      date_format = "%Y%m%d%H%M%S"
      return int(float(datetime.strptime(input_date, date_format).timestamp()) * 1000)


