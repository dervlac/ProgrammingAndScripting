# IPython log file - original source
# Dervla Candon
# Week 8 Task - Plots
# No user input required

import numpy as nm
import matplotlib.pyplot as plt

x = nm.arange(0,4.1,0.1)    #upper bound isnt included, so 4.1 used to ensure the value 4 is captured
f_x = x
g_x = x**2
h_x = x**3
plt.plot(x,f_x, label = "f(x)=x")   
plt.plot(x,g_x, label = "g(x)=x^2")
plt.plot(x,h_x, label = "h(x)=x^3")
plt.legend()    #adds legend to plot for colour coding
plt.title("f(x), g(x) and h(x)")    #add title
plt.show()  #enures that the plot is shown, if it does not automatically appear

