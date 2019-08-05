from Task_1 import crimes
with open("task_3_add", "rt") as data:
    text = data.read()
first = text.strip().split(",")
print(first)
for name in crimes:
    for data in crimes[name]:
        for el in first:
            if el == data["Type"]:
                print(name)


