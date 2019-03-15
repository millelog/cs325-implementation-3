import pulp as pulp


points = [(1,3), (2,5), (3,7), (5,11),(7,14),(8,15),(10,19)]

def solveData(data):
    a = pulp.LpVariable('a', lowBound=0, cat='Continuous')
    b = pulp.LpVariable('b', lowBound=0, cat='Continuous')
    z = pulp.LpVariable('z', lowBound=0, cat='Continuous')

    # Objective function
    my_lp_problem = pulp.LpProblem("Points", pulp.LpMinimize)
    my_lp_problem += z, "deviation"

    # Constraints
    for point in points:
        my_lp_problem += a*point[0]+b-point[1] <= z
        my_lp_problem += a*point[0]+b-point[1] >= -z

    status = my_lp_problem.solve()
    print(pulp.LpStatus[my_lp_problem.status])
    print("Y={slope}*x+{intercept}".format(slope=pulp.value(a),intercept=pulp.value(b)))
    print(pulp.value(a))
    print(pulp.value(b))
    print(pulp.value(z))

    return {
     "slope": pulp.value(a),
     "intercept": pulp.value(b)
    }


Values= solveData(points)
