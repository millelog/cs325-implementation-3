import pulp as pulp
import "./helpers.py" as h



my_lp_problem = pulp.LpProblem("Points", pulp.LpMinimize)

slope = pulp.LpVariable('slope', lowBound=0, cat='Continuous')
intercept = pulp.LpVariable('intercept', lowBound=0, cat='Continuous')
z = pulp.LpVariable('z', lowBound=0, cat='Continuous')

# y = Muffins
# x = bagels

# Objective function
my_lp_problem += z, "deviation"
points = [(1,3), (2,5), (3,7), (5,11),(7,14),(8,15),(10,19)]

for point in points:
    # Constraints
    my_lp_problem += slope*point[0]+intercept-point[1] <= z
    my_lp_problem += slope*point[0]+intercept-point[1] >= -z


status = my_lp_problem.solve()

print(pulp.LpStatus[my_lp_problem.status])
print(pulp.value(slope))
print(pulp.value(intercept))
