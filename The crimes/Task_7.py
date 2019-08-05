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
for year in dates:
    pass
print(dumps(dates, indent=4))



