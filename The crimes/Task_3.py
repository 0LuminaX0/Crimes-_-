from Task_1 import crimes
with open("task_3_add", "rt") as data:
    text = data.read()
first = text.strip().split(",")
print(first)
for name in crimes:
    for data in name:
        for el in range(len(text)):
            if el == data["Type"]:
                print(name)


