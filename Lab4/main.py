import csv
import random
FILENAME = "dataSet.csv" #имя изначального файла с данными
OUTPUTFILE = "newDataSet.csv" #имя преобразованного файла с данными

def newMap(func, startList : list) -> list:
    resultList = list()
    for i in startList:
        resultList.append(func(i))
    return resultList

#переопределённый reduce
def newReduce(func, startList : list):
    index : int = 2
    length : int = len(startList)
    result = func(startList[0], startList[1])
    while(index < length):
        result = func(result, startList[index])
        index += 1
    return result