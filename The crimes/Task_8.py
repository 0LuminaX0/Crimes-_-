from Task_1 import crimes
people = {}
from json import dumps
for name in crimes:
    if name != "-":
        for crime in crimes[name]:
            if name not in people:
                people[name] = 0
            if crime["Arrest"] == True:
                people[name] += 1
            if crime["Arrest"] == False:
                people[name] -= 1

print("Noobs\n")
for pupil in people:
    if people[pupil] < 0:
        print(pupil)
print("\n\n")
print("Pros\n")
for pupil in people:
    if people[pupil] > 0:
        print(pupil)



