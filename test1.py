
# importing the required module
import matplotlib.pyplot as plt
figure, axis = plt.subplots(3,1,figsize=(10,10))
# x axis values
x = [1,2,3,4]
# corresponding y axis values
y = [20,40,10,4]
y1= [20,50,80,6]
y2 =[50,30,60,9]

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