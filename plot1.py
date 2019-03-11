import max_deviation as part1
import matplotlib.pyplot as plt

data_x = []
data_y = []

trend_x = []
trend_y = []

for p in part1.points:
    data_x.append( p[0] )
    data_y.append( p[1] )

    trend_x.append( p[0] )
    trend_y.append(part1.sol[0]*p[0] + part1.sol[1] )


plt.plot(data_x, data_y, 'ro')
plt.plot(trend_x, trend_y)
plt.show()

