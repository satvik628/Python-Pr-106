# Correlation file marks-attend.csv


# importing modules
import csv
import numpy as np


# gettingDataSource
def getDataSource(data_path):
  marks=[]
  attendance=[]
  with open(data_path) as f:
    csv_reader=csv.DictReader(f)

    for row in csv_reader:
      marks.append(float(row['Marks In Percentage']))
      attendance.append(float(row['Days Present']))
    
  return {"x":marks,"y":attendance}


# finding correlation
def findCorrelation(dataSource):
  correlation=np.corrcoef(dataSource["x"],dataSource["y"])
  print("The correlation between them is --> : "+str(correlation[0,1]))


# setup for running codes 
def setup():
  path='data/marks-attend.csv' 
  dataSource=getDataSource(path)
  findCorrelation(dataSource)

# function call 
setup()


