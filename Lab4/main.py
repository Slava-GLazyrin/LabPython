import csv
import random
FILENAME = "dataSet.csv" #имя изначального файла с данными
OUTPUTFILE = "newDataSet.csv" #имя преобразованного файла с данными

def newMap(func, startList : list) -> list:
    resultList = list()
    for i in startList:
        resultList.append(func(i))
    return resultList

def newReduce(func, startList : list):
    index : int = 2
    length : int = len(startList)
    result = func(startList[0], startList[1])
    while(index < length):
        result = func(result, startList[index])
        index += 1
    return result


#Генерация списка списков с ФИО и количеством часов работы
def GenerateDataSet() -> list:
    Surnames : list = ["Возисов", "Глазырин", "Дмитриенко", "Бочкарёв"]
    Names : list = ["Максим", "Вячеслав", "Андрей", "Макар"]
    Patronymics : list = ["Петрович", "Вячеславович", "Викторович", "Владиславович"]
    Persons = list()
    i : int = 0
    count : int = 100
    Persons.append(["ФИО", "Часы работы"])
    while i < count:
        randomFullName = Surnames[random.choice(Surnames)] + " " + Names[random.choice(Names)] + " "  + Patronymics[random.choice(Patronymics)]
        Persons.append([randomFullName, random.randint(10, 350)])
        i += 1
    return Persons

#Запись в .csv из списка списков
def WriteInCSVFromList(dataSet : list, fileName : str):
     with open(fileName, "w", newline="") as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(dataSet)

#Запись в .csv из списка словарей        
def WriteInCSVFromDict(dataSet : list, fileName : str):
    with open(fileName, "w", newline="") as file:
        columns = list(dataSet[0].keys())
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=',')
        writer.writeheader()
        writer.writerows(dataSet)








