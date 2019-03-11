import pulp as pulp



my_lp_problem = pulp.LpProblem("Points", pulp.LpMinimize)

a = pulp.LpVariable('a', lowBound=0, cat='Continuous')
b = pulp.LpVariable('b', lowBound=0, cat='Continuous')
z = pulp.LpVariable('z', lowBound=0, cat='Continuous')

# y = Muffins
# x = bagels

# Objective function
my_lp_problem += z, "deviation"
points = [(1,3), (2,5), (3,7), (5,11),(7,14),(8,15),(10,19)]

for point in points:
    # Constraints
    my_lp_problem += a*point[0]+b-point[1] <= z
    my_lp_problem += a*point[0]+b-point[1] >= -z


status = my_lp_problem.solve()

print(pulp.LpStatus[my_lp_problem.status])
print(pulp.value(a))
print(pulp.value(b))
print(pulp.value(z))
