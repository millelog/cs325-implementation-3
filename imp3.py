import pulp as pulp
import csv
from math import sin,cos,pi


data = []

variables=[]

i=0
with open('./Corvallis.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        data.append(row[len(row)-2])
    # for row in range(50):
    #     data.append(spamreader[row][len(row)-2])







my_lp_problem = pulp.LpProblem("Points", pulp.LpMinimize)

x0 = pulp.LpVariable('x0', lowBound=0, cat='Continuous')
x1 = pulp.LpVariable('x1', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Continuous')
x3 = pulp.LpVariable('x3', lowBound=0, cat='Continuous')
x4 = pulp.LpVariable('x4', lowBound=0, cat='Continuous')
x5 = pulp.LpVariable('x5', lowBound=0, cat='Continuous')
deviation = pulp.LpVariable('deviation', lowBound=0, cat="Continuous")



def decentModel(d):
    twopid=2*pi*d
    solution = x0 + x1*d + x2*cos(twopid/365.25) + x3*sin(twopid/365.25) + x4*cos(twopid/(365.25*10.7)) + x5*sin(twopid/(365.25*10.7))
    return solution



# Objective function
my_lp_problem += deviation, "deviation"

# for index,point in  enumerate(data):
for index in range(5):
    # Constraints
    # twopid=2*pi*index
    # my_lp_problem += x0 + x1*index + x2*cos(twopid/365.25) + x3*sin(twopid/365.25) + x4*cos(twopid/(365.25*10.7)) + x5*sin(twopid/(365.25*10.7)) - point <= deviation
    # my_lp_problem +=  x0 + x1*index + x2*cos(twopid/365.25) + x3*sin(twopid/365.25) + x4*cos(twopid/(365.25*10.7)) + x5*sin(twopid/(365.25*10.7)) - point >= -deviation
    my_lp_problem += decentModel(index) - data[index] <= deviation
    my_lp_problem += decentModel(index) - data[index] >= -deviation
status = my_lp_problem.solve()

print(pulp.LpStatus[my_lp_problem.status])
print(pulp.value(x0))
print(pulp.value(x1))
print(pulp.value(x2))
print(pulp.value(x3))
print(pulp.value(x4))
print(pulp.value(x5))

print(pulp.value(deviation))
