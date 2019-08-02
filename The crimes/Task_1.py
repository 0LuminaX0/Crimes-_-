"""
1. Необходимо сделать отчет по каждому из известнх преступников: Загрузите информацию из файла в следующую структуру:
Словарь, ключами в котором являются имена преступников, каждому из
которых соответствует список со всеми их дениями, каждое из которых является словарем

Далее с помощью модуля json выведите на экран даный словарь

(Деяния неизвестных преступников обьедените в список и поместите в свой словарь с ключом "-")

10 баллов
10 минут
"""
from json import dumps


crimes = {}

with open("Crimes.csv", "rt") as text:
    lines = text.readlines()
first = lines.pop(0).strip().split(",")

for line in lines:
    line = line.strip("\n")
    lin = line.split(",")
    if lin[5] not in crimes:
        crimes[lin[5]] = []
    crimes[lin[5]].append({
        first[0]: int(lin[0]),
        first[1]: lin[1],
        first[6]: lin[6],
        first[7]: True if lin[7] == "True" else False,
        "Date": {
            first[2]: int(lin[2]),
            first[3]: int(lin[3]),
            first[4]: int(lin[4])
        },
        first[8]: lin[8]
        })


print(dumps(crimes, indent=4))
