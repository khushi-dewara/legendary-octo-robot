#AIM: Write a Python program to plot the function y=x**2 using the pyplot or matplotlib libraries.
# importing the required module

import matplotlib.pyplot as plt

# x axis values

x = [1,2,3]

# corresponding y axis values

y = [1,4,9]   #y=[x*x]

# plotting the points

plt.plot(x, y)

# naming the x axis

plt.xlabel('x - axis')

# naming the y axis

plt.ylabel('y - axis')

# giving a title to my graph

plt.title('My first graph!')

# function to show the plot

plt.show()
