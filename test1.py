
# importing the required module
import matplotlib.pyplot as plt
 
# x axis values
x = [1,2,3,4]
# corresponding y axis values
y = [2,4,1,4]
 
# plotting the points
plt.plot(x, y, marker='o', markerfacecolor='black', markersize=5)
plt.plot(x, y)
 
# naming the x axis
plt.xlabel('Data')
# naming the y axis
plt.ylabel('Temperature')
 
# giving a title to my graph
plt.title('Weather Station Data!')
plt.savefig('chart.png')
# function to show the plot
plt.show()