import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    marks = []
    presenty = []
    with open(data_path) as f:
        dataFrame = csv.DictReader(f)
        
        for row in dataFrame:
            marks.append(float(row['Marks']))
            presenty.append(float(row['Presenty']))

    return{'x': marks, 'y': presenty}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'], datasource['y'])
    print('The correlation of Marks of students and Presenty are: ', correlation[0, 1])

def setup():
    data_path = 'student.csv'

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()