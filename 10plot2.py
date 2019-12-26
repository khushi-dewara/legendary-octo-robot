#AIM: Write a Python program to plot the function y=x**2 using the pyplot or matplotlib libraries.
import matplotlib.pyplot as plt

import numpy as np

x = np.arange( -10 , 10 )

y = np.square( x )

plt.plot( x , y )

plt.show()

