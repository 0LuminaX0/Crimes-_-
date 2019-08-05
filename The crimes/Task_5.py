from json import dumps
from Task_1 import crimes
dates = {}
for name in crimes:
    if name == "-":
        for crime in crimes[name]:
            if crime["Date"]["Day"] in dates:
                dates[crime["Date"]["Day"]].append(crime)
            else:
                dates[crime["Date"]["Day"]] = [crime]
print(dumps(dates, indent=4))




