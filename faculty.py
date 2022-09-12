from pprint import pprint

import pandas as pd

df = pd.read_csv("faculty.csv")
column_names = [col for col in df.columns]
item = (df["Monday Morning"][0])
location = item.split("-")[0].strip()
faculty = item.split("-")[1].strip()
# print(faculty, location)

days = {}
doctors = {}
for name in column_names:
    days[name] = []
    for row in df[name].dropna():
        item = row.split("-")
        location = item[0].strip()
        faculty = item[1].strip()
        days[name].append((location, faculty))

pprint(days["Monday Morning"])


def get_faculty_on_day(day_of_week):
    return days[day_of_week]


def get_location_of_faculty(faculty_name):
    return


def get_faculty_today():
    return  # list of faculty today


def get_faculty_location_today(f):
    return  # faculty location today
