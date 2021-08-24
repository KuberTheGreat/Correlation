import plotly.express as px
import csv

with open('student.csv') as f:
    dataFrame = csv.DictReader(f)
    figure = px.scatter(dataFrame, x = 'Marks', y = 'Presenty', title = 'Marks of students and their presenty')
    figure.show()