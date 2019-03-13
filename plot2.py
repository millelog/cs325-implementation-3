import imp3 as part2
import matplotlib.pyplot as plt
from math import sin,cos,pi

# print(part2.sol[0])

data_x = []
data_y = []

trend_x = []
trend_y = []

linear_trend_x = []
linear_trend_y = []

x_0 = part2.pulp.value(part2.x0)
x_1 = part2.pulp.value(part2.x1)
x_2 = part2.pulp.value(part2.x2)
x_3 = part2.pulp.value(part2.x3)
x_4 = part2.pulp.value(part2.x4)
x_5 = part2.pulp.value(part2.x5)


def linearModel(d):
    return x_0 + x_1*d

def model(d):
    twopid=2*pi*d
    solution = x_0 + x_1*d + x_2*cos(twopid/365.25) + x_3*sin(twopid/365.25) + x_4*cos(twopid/(365.25*10.7)) + x_5*sin(twopid/(365.25*10.7))
    # solution = x0 + x1*d
    return solution



for point in part2.data:
    data_x.append(point[0])
    data_y.append(point[1])
    trend_y.append(model(point[0]))
    trend_x.append(point[0])
    linear_trend_y.append(linearModel(point[0]))
    linear_trend_x.append(point[0])


#print(trend_x)


plt.plot(data_x, data_y , 'ro', markersize=0.5)
plt.plot(trend_x, trend_y )
plt.plot(linear_trend_x, linear_trend_y)
plt.show()