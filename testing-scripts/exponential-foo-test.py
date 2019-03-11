from pulp import *
from helpPopulate import *



def read_file():
    #using the help-popylate
    data = pickleIn("./data/reg-exponential.txt")
    return data


def write_exponetial_file():
    #using the help-popylate
    data = populateUsing(non_translated_exponetial,1000)
    pickleOut(data,"./data/reg-exponential.txt")
    return

def non_translated_exponetial(x):
    y = 0.5 * (x ** 2) # simple exponential equation
    return y


def lp_test(data):
    my_lp_problem = LpProblem("Exponential - basic", pulp.LpMinimize)
    slope = LpVariable('slope', cat='Continuous')
    deviation = LpVariable('deviation', lowBound=0, cat='Continuous')

    #objective function
    my_lp_problem += deviation, "deviation"

    #constraints
    for point in data:
        my_lp_problem += slope * (point[0]**2) - point[1] <= deviation
        my_lp_problem += slope * (point[0]**2) - point[1] >= deviation

    status = my_lp_problem.solve()
    print("y = {slope}*x^2 + 0".format(slope=value(slope)))

def main():
    write_exponetial_file()

    data = read_file()
    lp_test(data)



    return



main()
