from Task_1 import crimes
from json import dumps
dates = {}
for name in crimes:
    for crime in crimes[name]:
        ten = crime["Date"]["Year"]
        if ten // 10 in dates:
            if crime["Type"] in dates[ten // 10]:
                dates[ten // 10][crime["Type"]] += 1
            else:
                dates[ten // 10][crime["Type"]] = 1

        else:
            dates[ten // 10] = {
                crime["Type"] : 1
            }
print(dumps(dates, indent=4))
for year in dates:
    crime = 0
    for crime_ in dates[year]:
        crime += dates[year][crime_]
    print(year, crime, "crimes")

for year in dates:
    crime = [[], 0]
    for crime_ in dates[year]:
        if dates[year][crime_] > crime[1]:
            crime[1] = dates[year][crime_]
            crime[0].append(crime_)
        elif dates[year][crime_] == crime[1]:
            crime[0].append(crime_)
    print(year, crime)






