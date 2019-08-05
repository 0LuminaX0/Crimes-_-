from json import loads, dumps
from Task_1 import crimes
with open("4.txt", "wt") as txt:
    ans = input("Name: ")
    if ans in crimes:
        lst = crimes[ans]
    for crime in lst:
        crime = list(crime.values())
        for i in range(len(crime)):
            crime[i] = str(crime[i])
        txt.write(";".join(crime) + "\n")


