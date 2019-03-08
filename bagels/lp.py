import pulp as pulp



my_lp_problem = pulp.LpProblem("Bagels n Muffins", pulp.LpMaximize)

x = pulp.LpVariable('x', lowBound=0, cat='Integer')
y = pulp.LpVariable('y', lowBound=0, cat='Integer')

# x = bagels
# y = Muffins

# Objective function
my_lp_problem += 12 * x + 10 * y, "profit"

# Constraints
my_lp_problem += 5 * x + 4 * y  <= 50 # flour
my_lp_problem += 2 * x + 4 * y <= 30 #eggs
my_lp_problem += 1 * x + 2 * y <= 20 #sugar


status = my_lp_problem.solve()

print(pulp.LpStatus[my_lp_problem.status])
print(pulp.value(x))
print(pulp.value(y))
