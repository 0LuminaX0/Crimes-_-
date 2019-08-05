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
for date in dates:
    d = 0
    for crime in dates[date]:
        d += 1
        if d >= 3:
            print("Niko, Date:", date)
            print(dumps(dates[date], indent=4))






