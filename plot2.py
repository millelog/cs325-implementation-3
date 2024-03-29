import src.warming_up as part2
import matplotlib.pyplot as plt
from math import sin,cos,pi

# print(part2.sol[0])

data_x = []
data_y = []

trend_x = []
trend_y = []

linear_trend_x = []
linear_trend_y = []


# indexed was the LP solving it based on the index
# day was the LP using the csv "day" colomn, which wasnt quite the index

indexed_variables= [None]*6
day_variables = [None]*6


for index in range(6):
    indexed_variables[index]=part2.IndexValues["x"+str(index)]

for index in range(6):
    day_variables[index]=part2.DayValues["x"+str(index)]


def linearModel(d,vals):
    return vals[0] + vals[1]*d

def model(d,vals):
    twopid=2*pi*d
    solution = vals[0] + vals[1]*d + vals[2]*cos(twopid/365.25) + vals[3]*sin(twopid/365.25) + vals[4]*cos(twopid/(365.25*10.7)) + vals[5]*sin(twopid/(365.25*10.7))
    # solution = x0 + x1*d
    return solution

data2_x = []
data2_y = []
trend2_y = []
trend2_x = []
linear_trend2_x=[]
linear_trend2_y=[]

for point in part2.DayData:
    data_x.append(point[0])
    data_y.append(point[1])
    trend_y.append(model(point[0],day_variables))
    trend_x.append(point[0])
    linear_trend_y.append(linearModel(point[0],day_variables))
    linear_trend_x.append(point[0])

for point in part2.IndexedData:
    data2_x.append(point[0])
    data2_y.append(point[1])
    trend2_y.append(model(point[0],indexed_variables))
    trend2_x.append(point[0])
    linear_trend2_y.append(linearModel(point[0],indexed_variables))
    linear_trend2_x.append(point[0])
#print(trend_x)

linear_eq_str = "y = " + str(day_variables[0]) + "x + " + str(day_variables[1])
linear_eq_str2 = "y = " + str(indexed_variables[0]) + "x + " + str(indexed_variables[1])

plt.subplot(2, 1, 1)
plt.plot(data_x, data_y , 'ro', markersize=0.25, label="raw temperature data")
plt.plot(trend_x, trend_y,  label="temperature model by value" )
plt.plot(linear_trend_x, linear_trend_y, label="warming model")

plt.legend(loc=0,framealpha=1, fontsize=8)
plt.xlabel("Days [d]")
plt.ylabel("Temperature [C]")
plt.title("Temperature Model of Corvallis, OR \n where [d]=value['day'] of CSV")
##annotate with a phase shift in position
#plt.annotate(linear_eq_str, xy=(linear_trend_x[5000], linear_trend_y[5000]),
#                xytext=(linear_trend_x[5000] - 50, linear_trend_y[5000] - 15))
#
plt.show()
plt.subplot(2, 1, 2)
plt.plot(data2_x, data2_y , 'ro', markersize=0.25, label="raw temperature data")
plt.plot(trend2_x, trend2_y,  label="temperature model by index" )
plt.plot(linear_trend2_x, linear_trend2_y, label="warming model")

plt.legend(loc=0,framealpha=1, fontsize=8)
plt.xlabel("Days [d]");
plt.ylabel("Temperature [C]")
plt.title("p2: Temperature Model of Corvallis, OR \n where [d]=row# of CSV")
#plt.annotate(linear_eq_str2, xy=(linear_trend_x[5000], linear_trend_y[5000]),
#                xytext=
plt.show()
