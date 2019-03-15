import src.max_deviation as part1
import matplotlib.pyplot as plt

data_x = []
data_y = []

trend_x = []
trend_y = []

for p in part1.points:
    data_x.append( p[0] )
    data_y.append( p[1] )

    trend_x.append( p[0] )
    trend_y.append(part1.Values["slope"]*p[0] + part1.Values["intercept"] )

equStr = "y = " + str(part1.Values["slope"]) + "x + " + str(part1.Values["intercept"])

plt.plot(data_x, data_y, 'ro', label="raw data")
plt.plot(trend_x, trend_y, label="linear best fit")
plt.annotate(equStr, xy=(trend_x[3], trend_y[3]), xytext=(trend_x[3]-4, trend_y[3]+4))
plt.legend(loc=0,framealpha=1, fontsize=8)
plt.title("Linear Best Fit Example")
plt.show()
