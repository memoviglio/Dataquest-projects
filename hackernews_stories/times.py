import read
df = read.load_data()
#importing parser to apply on timestamp
from dateutil.parser import parse
# function to take hour out of datetime object
def hour(column):
    dt = parse(column)
    return dt.hour
#applying function to time column
hours = df["submission_time"].apply(hour)
print(hours.value_counts())