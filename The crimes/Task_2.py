from  Task_1 import crimes
ans = int(input("Year: "))
print(ans)
for name in crimes:
    for dat in crimes[name]:
        if ans == dat["Date"]["Year"]:
            print(name)

