import plotly_express as px
import csv
import numpy as np
def plotfigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x ="Days Present" , y = "Marks in Percentage")
        fig.show()

def getDataSource(data_path):
    Marks_in_percentage = []
    roll_no = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks_in_percentage.append(float(row['Days Present']))
            roll_no.append(float(row['Marks in Percentage']))
    return{"x" : Marks_in_percentage, "y" : roll_no}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Days Present vs Marks in Percentage :- \n--->",correlation[0,1])

def setup(): 
    data_path = "Student Marks vs Days Present.csv" 
    datasource = getDataSource(data_path) 
    findCorrelation(datasource) 
    plotfigure(data_path) 

setup()