import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


dataPath = r'C:\Amarth\Documents\OSU Assignments\EDUTL 1902\dataSet.pckl'
xlsPath = r'C:\Amarth\Documents\OSU Assignments\EDUTL 1902\Data.xls'
possibleType = ["wyvern", "european", "asian", "multiple", 
                "other", "mixture", "drake", "multi-head"]
dataSet = pd.read_excel(xlsPath, encoding = "ISO-8859-1")

def cleanType(dragonType):
    dragonType = str(dragonType).lower()
    for instance in possibleType:
        if instance in dragonType:
            return instance

def typeWithYear():
    ''' Type of dragon in every year film 
    data structure: {1999:{wyvern:1, europen:2}, 
                     2001:{european:1, asian:1}}
    '''
    relation = {}
    for rowIndex in range(len(dataSet)):
        currentItemReleaseYear = dataSet["YearReleased"][rowIndex]
        if np.isnan(currentItemReleaseYear):
            continue
        if currentItemReleaseYear not in relation:
            relation[int(currentItemReleaseYear)] = {}
        currentDragonType = cleanType(dataSet["DragonType"][rowIndex])
        if currentDragonType not in relation[int(currentItemReleaseYear)]:
            relation[int(currentItemReleaseYear)][currentDragonType] = 1
        else:
            relation[int(currentItemReleaseYear)][currentDragonType] += 1

    for year in relation: #modifi into same dict items
        for instance in possibleType:
            if instance not in relation[year]:
                relation[year][instance] = 0

    print(relation)
    

def main():
    typeWithYear()

if __name__ == '__main__':
    main()
