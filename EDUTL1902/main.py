import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
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

def cleanType(dragonType, showProcess = False):

    dragonType = str(dragonType).lower()
    if showProcess: print(dragonType, end = " ") #====================
    for mainTag in categDict:
        
        for subTag in categDict[mainTag]:
            if subTag in dragonType:
                if showProcess: print("classified as ", mainTag) #====================
                return mainTag
    

def typeWithYear(plot = False, saveFile = False):
    ''' Type of dragon in every year film 
    data structure: {1999:{wyvern:1, europen:2}, 
                     2001:{european:1, asian:1}}
    '''
    relation = {}
    for rowIndex in range(len(dataSet)):
        #print(dataSet["YearReleased"][rowIndex])
        if np.isnan(dataSet["YearReleased"][rowIndex]):
            continue
        currentItemReleaseYear = dataSet["YearReleased"][rowIndex] - dataSet["YearReleased"][rowIndex]%5
        if currentItemReleaseYear not in relation:
            relation[int(currentItemReleaseYear)] = {}
        #print(rowIndex, end = '  ')
        currentDragonType = cleanType(dataSet["DragonType"][rowIndex])
        if currentDragonType not in relation[int(currentItemReleaseYear)]:
            relation[int(currentItemReleaseYear)][currentDragonType] = 1.0
        else:
            relation[int(currentItemReleaseYear)][currentDragonType] += 1.0

    for year in relation: #unify
        for instance in categDict:
            if instance not in relation[year]:
                relation[year][instance] = 0

    df = pd.DataFrame(relation)
    df = df.T
    #print(df)
    
    if plot:
        plt.style.use(u'ggplot')
        df.fillna(df).astype(df.dtypes).plot.bar(stacked=True)
        plt.show()
    if saveFile:
        df.to_excel("dragonTypeWithYear.xls")
    
    return relation 
     
def intelWithYear(plot = False, saveFile = False):
    relation = {}
    for rowIndex in range(len(dataSet)):

        currentWork = dataSet["TitleOfFilm"][rowIndex]
        voiceActor = str(dataSet["VoiceActor"][rowIndex]).lower()
        transform = str(dataSet["TransformsIfSoFromWhat"][rowIndex]).lower()
        currentDragonType = cleanType(dataSet["DragonType"][rowIndex])

        if np.isnan(dataSet["YearReleased"][rowIndex]):
            continue
        currentItemReleaseYear = dataSet["YearReleased"][rowIndex] - dataSet["YearReleased"][rowIndex]%5
      
        if currentItemReleaseYear not in relation:
            relation[int(currentItemReleaseYear)] = {}
        #print(rowIndex, end = '  ') #====================
        
        intelligent = True if ((voiceActor != "nan") or (transform != "no")) else False
        #print(currentWork, ": ", voiceActor, transform, intelligent) #====================

        if intelligent and currentDragonType not in relation[int(currentItemReleaseYear)]:
            relation[int(currentItemReleaseYear)][currentDragonType] = 1
        elif intelligent:
            relation[int(currentItemReleaseYear)][currentDragonType] += 1
        
    for year in relation: #unify
        for instance in categDict:
            if instance not in relation[year]:
                relation[year][instance] = 0

    #print(relation)
    df = pd.DataFrame(relation)
    df = df.T
    #print(df) #====================
    
    if plot:
        plt.style.use(u'ggplot')
        df.fillna(df).astype(df.dtypes).plot.bar(stacked=True)
        plt.show()
    if saveFile:
        df.to_excel("dragonIntelWithYear.xls")

    return relation

def friendlyWithYear(plot = False, countingMix = False, saveFile = False):
    relation = {}
    for rowIndex in range(len(dataSet)):

        currentWork = dataSet["TitleOfFilm"][rowIndex]
        friendly = str(dataSet["HumanFriendly"][rowIndex]).lower()
        currentDragonType = cleanType(dataSet["DragonType"][rowIndex])

        if np.isnan(dataSet["YearReleased"][rowIndex]):
            continue
        currentItemReleaseYear = dataSet["YearReleased"][rowIndex] - dataSet["YearReleased"][rowIndex]%5
        if currentItemReleaseYear not in relation:
            relation[int(currentItemReleaseYear)] = {}
            
        #print(friendly) #====================
        if ((friendly == "yes") and (currentDragonType not in relation[int(currentItemReleaseYear)])):
            relation[int(currentItemReleaseYear)][currentDragonType] = 1.0
        elif friendly == "yes":
            relation[int(currentItemReleaseYear)][currentDragonType] += 1.0
        if countingMix:
            if (friendly == "mixture" and (currentDragonType not in relation[int(currentItemReleaseYear)])):
                relation[int(currentItemReleaseYear)][currentDragonType] = 0.5
            elif friendly == "mixture":  
                relation[int(currentItemReleaseYear)][currentDragonType] += 0.5
        
    for year in relation: #unify
        for instance in categDict:
            if instance not in relation[year]:
                relation[year][instance] = 0

    #print(relation) 
    df = pd.DataFrame(relation) 
    df = df.T 
    #print(df)  #====================
     
    if plot: 
        plt.style.use(u'ggplot')
        df.fillna(df).astype(df.dtypes).plot.bar(stacked=True)
        plt.show()
    if saveFile:
        df.to_excel("dragonFriendlyWithYear.xls")

    return relation

def ratioWithType(plotTitle = "General Friendliness"):
    typeWithY = pd.DataFrame(typeWithYear())
    intelWithY = pd.DataFrame(intelWithYear())
    friendlyWithY = pd.DataFrame(friendlyWithYear())
    yearIndex = np.array(list(typeWithY.columns.values))

    currentByco = friendlyWithY
    ratioTypes = ["wyvern", "european", "asian", "other", "drake"]

    plt.style.use(u'ggplot')
    for type in ratioTypes:
        tar = np.array(list(currentByco.loc[type, :])) / np.array(list(typeWithY.loc[type, :]))
        nanS = np.isnan(tar); tar[nanS] = 0
        p1 = np.poly1d(np.polyfit(yearIndex, tar, 1))
        print(type, tar)
        plt.plot(yearIndex, p1(yearIndex), label = type, linewidth = 3)
        plt.legend(loc = 'best')

    plt.title(plotTitle)
    plt.show()

def main():
    #typeWithYear(saveFile = True, plot = True)
    #intelWithYear(saveFile = True, plot = True)
    #friendlyWithYear(saveFile = True, plot = True)
    ratioWithType()

if __name__ == '__main__':
    main()
