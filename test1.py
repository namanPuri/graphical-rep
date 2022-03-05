
# importing the required module
import matplotlib.pyplot as plt
figure, axis = plt.subplots(3,1)
# x axis values
x = [1,2,3,4]
# corresponding y axis values
y = [2,4,1,4]
y1= [2,5,8,6]
y2 =[5,3,6,9]

axis[0].plot(x, y, color = 'r', marker='o', markerfacecolor='black', markersize=5)
axis[0].set_title("Temperature Data")

axis[1].plot(x, y1, color = 'g', marker='o', markerfacecolor='black', markersize=5)
axis[1].set_title("Pressure Data")

axis[2].plot(x, y2, color = 'b', marker='o', markerfacecolor='black', markersize=5)
axis[2].set_title("Humidity Data")
# function to show the plot
figure.tight_layout()
plt.savefig('chart.png')
plt.show()