from  Task_1 import crimes
ans = int(input("Year: "))
print(ans)
for name in crimes:
    for data in crimes[name]:
        if ans == [data]["Date"]["Year"]:
            print(name)

