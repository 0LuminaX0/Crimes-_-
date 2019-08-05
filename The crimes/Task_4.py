from json import loads, dumps
from Task_1 import crimes
with open("4.txt", "wt") as txt:
    txt.write("jk")
    ans = input("Name: ")
    if ans in crimes:
        lst = crimes[ans]
    a = dumps(lst)
    print(a)
    txt.write(a)

