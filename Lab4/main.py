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
        randomFullName = Surnames[random.randint(0 , len(Surnames) - 1)] + " " + Names[random.randint(0 , len(Names) - 1)] + " "  + Patronymics[random.randint(0 , len(Patronymics) - 1)]
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

#Чтение из .csv в виде списка словарей
def ReadFromCSV(fileName : str) -> list:
    with open(fileName, "r", newline="") as file:
        reader = csv.DictReader(file)
        resultListDict = list()
        for dict in reader:
            resultListDict.append(dict);        
    return resultListDict

def SplitFullNameFromDict(startList : dict) -> dict:
    resultDict = dict()
    strs = startList["ФИО"].split(' ')
    resultDict["Фамилия"] = strs[0]
    resultDict["Имя"] = strs[1]
    resultDict["Отчество"] = strs[2]
    resultDict["Часы работы"] = startList["Часы работы"]
    return resultDict

def GetSumFromDict(startList1 : dict, startList2 : dict) -> dict:
    resultDict = dict()
    resultDict["Часы работы"] = int(startList2["Часы работы"]) + int(startList1["Часы работы"]) 
    return resultDict

#Генерация изначального файла .csv
WriteInCSVFromList(GenerateDataSet(), FILENAME)

#ЗАДАЧА 1, разрезать столбец ФИО на отдельные столбцы с помощью map и записать в новый файл .csv
dataSet : list = ReadFromCSV(FILENAME)
newDataSet : list = newMap(SplitFullNameFromDict, dataSet)
WriteInCSVFromDict(newDataSet, OUTPUTFILE)

#ЗАДАЧА 2, подсчёт суммы с помощью reduce
salarySumHoursWork = newReduce(GetSumFromDict, dataSet)["Часы работы"]
print("Суммарное количество часов работы в файле: " + str(salarySumHoursWork))




