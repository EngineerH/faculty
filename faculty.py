import pandas as pd

df = pd.read_csv("faculty.csv",na_values="missing")
column_names = [col for col in df.columns]
item = (df["Monday Morning"][0])
location = item.split("-")[0].strip()
faculty = item.split("-")[1].strip()
print(faculty,location)

for name in column_names:
    for row in df[name]:
        item = row.split("-")
        location = item[0].strip()
        faculty = item[1].strip()
        print(f"On {name} Dr.{faculty} is in {location}")
# print(df.head())
