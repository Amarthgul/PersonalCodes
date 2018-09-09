import pandas as pd
import pickle
import os
import io

dataPath = r'C:\Amarth\Documents\OSU Assignments\EDUTL 1902\dataSet.pckl'
xlsPath = r'C:\Amarth\Documents\OSU Assignments\EDUTL 1902\Data.xls'

#upToDate = True
#if upToDate and os.path.exists(dataPath):
#    with open(dataPath) as f:
#        dataSet = pickle.load(f)
#else:
#    dataSet = pd.read_excel(r'C:\Amarth\Documents\OSU Assignments\EDUTL 1902\Data.xlsx')
#    with open(dataPath, 'wb') as f:
#        pickle.dump(dataSet, f)

dataSet = pd.read_excel(xlsPath, encoding = 'utf-8')
print(dataSet)
