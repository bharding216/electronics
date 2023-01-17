import pandas as pd
import numpy as np

sales = pd.read_csv('kz.csv')

event_date = pd.to_datetime(sales['event_time']).dt.date
#event_time = pd.to_datetime(sales['event_time']).dt.time

event_date.head()