import pulp as pulp
import csv
from math import sin,cos,pi


DayData = []
IndexedData = []

variables=[]

i=0
index=0
with open('./Corvallis.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        if(row[len(row)-2] !=  "average"):
            DayData.append([int(row[len(row)-1]),float(row[len(row)-2])])
            IndexedData.append([index,float(row[len(row)-2])])

            index+=1
    # for row in range(50):
    #     data.append(spamreader[row][len(row)-2]


def decentModel(d,vars):
    twopid=2*pi*d
    solution = vars[0] + vars[1]*d + vars[2]*cos(twopid/365.25) + vars[3]*sin(twopid/365.25) + vars[4]*cos(twopid/(365.25*10.7)) + vars[5]*sin(twopid/(365.25*10.7))
    # solution = x0 + x1*d

    return solution

def solveData(data):

    my_lp_problem = pulp.LpProblem("Points", pulp.LpMinimize)
    vars=[];
    deviation = pulp.LpVariable('deviation', lowBound=0, cat="Continuous")

    vars.append(pulp.LpVariable('x0', lowBound=0, cat='Continuous'))
    vars.append(pulp.LpVariable('x1', lowBound=0, cat='Continuous'))
    vars.append(pulp.LpVariable('x2', lowBound=0, cat='Continuous'))
    vars.append(pulp.LpVariable('x3',  cat='Continuous'))
    vars.append(pulp.LpVariable('x4',  cat='Continuous'))
    vars.append(pulp.LpVariable('x5',  cat='Continuous'))

    my_lp_problem += deviation, "deviation"
    # Objective function
    for point in  data:
    # for index in range(1):
        # # Constraints
        my_lp_problem += decentModel(point[0],vars) - point[1] <= deviation
        my_lp_problem += decentModel(point[0],vars) - point[1] >= -deviation
    status = my_lp_problem.solve()

    print(pulp.LpStatus[my_lp_problem.status])
    vals = {
     "x0": pulp.value(vars[0]),
     "x1": pulp.value(vars[1]),
     "x2": pulp.value(vars[2]),
     "x3": pulp.value(vars[3]),
     "x4": pulp.value(vars[4]),
     "x5": pulp.value(vars[5])
     }
    print(vals)
    return vals

print("\n\tSolution to the problem using the Value in the CSV colomn Day as Day: \n")
DayValues = solveData(DayData);

print("\n\tSolution to the problem using index of the row in csv as Day: \n")
# IndexValues = solveData(IndexedData);
