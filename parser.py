import csv
import shutil
import os

os.path.expanduser('~')

file_csv = "input.csv"
file_full = "full.fis"
file_short = "short.fis"


mode = int(input("Choose mode:\n0 for full\n1 for short\n: "))

data = []


class Full:
    def __init__(self):
        self.one = ['Мало', 'Маленькая', 'Низкая', 'Раннее утро']
        self.two = ['Ниже среднего', 'Ниже средней', 'Утро']
        self.three = ['Среднее', 'Средняя', 'День']
        self.four = ['Выше среднего', 'Выше средней', 'Вечер']
        self.five = ['Много', 'Большая', 'Высокая', 'Ночь']


class Short:
    def __init__(self):
        self.one = ['Мало', 'Маленькая', 'Низкая', 'Утро']
        self.two = ['Среднее', 'Средняя', 'День']
        self.three = ['Много', 'Большая', 'Высокая', 'Высокое', 'Вечер']


fulln = Full()
shortn = Short()

try:
    with open(file_csv, "r") as file:
        reader = csv.reader(file, delimiter=';')
        for line in reader:
            tmp = []
            for inf in line:
                tmp.append(inf)
            data.append(tmp)
except IOError:
    print("Error occurred while opening the csv input file!")

data = data[2:]

for line in data:
    for i in range(1, len(line), 2):
        if line[i] == "":
            line[i] = 0
        if mode == 0:
            if any(num == line[i] for num in fulln.one):
                line[i] = 1
            elif any(num == line[i] for num in fulln.two):
                line[i] = 2
            elif any(num == line[i] for num in fulln.three):
                line[i] = 3
            elif any(num == line[i] for num in fulln.four):
                line[i] = 4
            elif any(num == line[i] for num in fulln.five):
                line[i] = 5
        elif mode == 1:
            if any(num == line[i] for num in shortn.one):
                line[i] = 1
            if any(num == line[i] for num in shortn.two):
                line[i] = 2
            if any(num == line[i] for num in shortn.three):
                line[i] = 3
        if line[i-1] == "+":
            line[i] *= -1

output = []
for line in data:
    tmp = ""
    for i in range (1, len(line), 2):
        tmp += str(line[i])
        if i == 1 + 2 * 4:
            tmp += ","
        tmp += " "
    tmp += "(1) : 1"
    output.append(tmp)



# print(data)

if mode == 0:
    shutil.copy2("full.fis", "output.fis")
elif mode == 1:
    shutil.copy2("short.fis", "output.fis")

try:
    with open("output.fis", 'a') as file:
        for line in output:
            file.write(line + "\n")
            print(line)
    shutil.copy2("output.fis", "/Users/dmitry/Documents/MATLAB/output.fis")
except IOError:
    print("Error occurred while oppening the file output.fis")