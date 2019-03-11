from pulp import *
from helpPopulate import *



def read_file():
    #using the help-popylate
    data = pickleIn("./data/translated-exponential.txt")
    return data


def write_exponetial_file():
    #using the help-popylate
    data = populateUsing(translated_exponetial,1000)
    pickleOut(data,"./data/translated-exponential.txt")
    return

def translated_exponetial(x):
    y = 0.5 * ((x) ** 2) + 10 # simple exponential equation
    return y

def translated_model(point,lpVars):
    model = lpVars["slope"] * (point[0]**2) + lpVars["translateY"] - point[1]
    return model

def lp_test(data):
    mylpVars = {}
    my_lp_problem = LpProblem("Exponential - basic", pulp.LpMinimize)

    mylpVars["slope"]= LpVariable('slope', cat='Continuous')
    mylpVars["deviation"]= LpVariable('deviation', upBound=10, cat='Continuous')
    mylpVars["translateX"]= LpVariable('translateX', cat='Continuous')
    mylpVars["translateY"]= LpVariable("translateY", cat='Continuous')

    #objective function
    my_lp_problem += mylpVars["deviation"], "deviation"

    #constraints
    for point in data:
        my_lp_problem += translated_model(point,mylpVars) <= mylpVars["deviation"]
        my_lp_problem += translated_model(point,mylpVars) >= mylpVars["deviation"]

    status = my_lp_problem.solve()
    print("y = {slope}*(x-{xvalue})^2 + {yvalue}".format(
            slope=value(mylpVars["slope"]),xvalue=value(mylpVars["translateX"]),yvalue=value(mylpVars["translateY"])))

def main():
    write_exponetial_file()

    data = read_file()
    lp_test(data)



    return



main()
