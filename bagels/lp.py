import pulp as pulp



my_lp_problem = pulp.LpProblem("Bagels n Muffins", pulp.LpMaximize)

bagels = pulp.LpVariable('bagels', lowBound=0, cat='Integer')
muffins = pulp.LpVariable('muffins', lowBound=0, cat='Integer')

# x = bagels
# y = Muffins

# Objective function
my_lp_problem += 12 * bagels + 10 * muffins, "profit"

# Constraints
my_lp_problem += 5 * bagels + 4 * muffins  <= 50 # flour
my_lp_problem += 2 * bagels + 4 * muffins <= 30 #eggs
my_lp_problem += 1 * bagels + 2 * muffins <= 20 #sugar


status = my_lp_problem.solve()

print(pulp.LpStatus[my_lp_problem.status])
print(pulp.value(bagels))
print(pulp.value(muffins))
