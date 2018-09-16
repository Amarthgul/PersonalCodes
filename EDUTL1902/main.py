import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

xlsPath = r'C:\Amarth\Documents\OSU Assignments\EDUTL 1902\Data.xls'
possibleType = ["wyvern", "european", "asian", "multiple", 
                "other", "mixture", "drake", "amphiptere"]
categDict = {"wyvern":      ["wyvern"],
                "european":    ["european"],
                "asian":       ["asian", "serpentine"],
                "other":       ["multiple", "other", "mixture"],
                "drake":       ["drake"],
                "amphiptere" : ["amphiptere"]}
dataSet = pd.read_excel(xlsPath, encoding = "ISO-8859-1")

def cleanType(dragonType, combineMultOth = True):

    dragonType = str(dragonType).lower()
    #print(dragonType, end = " ")
    for mainTag in categDict:
        
        for subTag in categDict[mainTag]:
            if subTag in dragonType:
                #print("classified as ", mainTag)
                return mainTag
    

def typeWithYear():
    ''' Type of dragon in every year film 
    data structure: {1999:{wyvern:1, europen:2}, 
                     2001:{european:1, asian:1}}
    '''
    relation = {}
    for rowIndex in range(len(dataSet)):
        currentItemReleaseYear = dataSet["YearReleased"][rowIndex] - dataSet["YearReleased"][rowIndex]%5
        if np.isnan(currentItemReleaseYear):
            continue
        if currentItemReleaseYear not in relation:
            relation[int(currentItemReleaseYear)] = {}
        #print(rowIndex, end = '  ')
        currentDragonType = cleanType(dataSet["DragonType"][rowIndex])
        if currentDragonType not in relation[int(currentItemReleaseYear)]:
            relation[int(currentItemReleaseYear)][currentDragonType] = 1
        else:
            relation[int(currentItemReleaseYear)][currentDragonType] += 1

    for year in relation: #unify
        for instance in categDict:
            if instance not in relation[year]:
                relation[year][instance] = 0

    
    return relation
def plotTypeWithYear():
    df = pd.DataFrame(typeWithYear())
    df = df.T
    print(df)
    
    plt.style.use(u'ggplot')
    df.fillna(df).astype(df.dtypes).plot.bar(stacked=True)
    plt.show()

    return 0

def plotTypeWithYearMean():
    df = pd.DataFrame(typeWithYear())
    print(df)
    
    plt.style.use(u'ggplot')
    df.fillna(df).astype(df.dtypes).plot.bar(stacked=True)
    plt.show()
    return 0
    

def main():
    plotTypeWithYearMean()

if __name__ == '__main__':
    main()
