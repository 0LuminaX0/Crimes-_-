from Task_1 import crimes
items = ["gun", "frisbee", "holder"]
for name in crimes:
    for crime in crimes[name]:
        desc = crime["Description"]
        for el in items:
            if el in desc:
                print(el,name)
