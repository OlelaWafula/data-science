import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data 
seattle_weather = pd.read_csv('seattle_weather.csv')
austin_weather = pd.read_csv('austin_weather.csv')

# Small Multiples 
"""
*These are multiple small plots that show similar data across different conditions. e.g. Precipitation data across different cities.
*In matplotlib small multiples are called subplots. That is also the reason that the functionthat creates figure and axis objects is called subplots().

*Calling subplots() with no inputs creates one subplot.
"""
# Create a figure object with three rows of subplots and 2 columns 
fig, ax = plt.subplots(3, 2)
plt.show()

"""
*We get an array of axes with ax.shape of 3, 2.
*To add data we will have to index into this object and call the plot() on an element of the array. 
"""
ax[0, 0].plot(seattle_weather['MONTH'], 
              seattle_weather['MLY-PRCP-NORMAL'], color='b')
plt.show()

"""
*There is a special case when you only have one row or column of plots. In this case the resulting array will be one dimensional, will only need to provide one index to access the element of this array.
"""
# Subplots with one row or column
fig, ax = plt.subplots(2, 1)
ax[0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-NORMAL'],
            color='b')
ax[0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-25PCTL'],
           linestyle="dashed", color='b')
ax[0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-75PCTL'],
           linestyle="dotted", color='g')

ax[1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'],
            color='b')
ax[1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-25PCTL'],
           linestyle="dashed", color='b')
ax[1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-75PCTL'],
           linestyle="dotted", color='g')

ax[0].set_ylabel("Precipitation (inches)")
ax[1].set_ylabel("Precipitation (inches)")
ax[1].set_xlabel("Time (months)")
plt.show()

# Sharing the y - axis range
"""
*To make sure that all the subplots have same range of y - axis values, we initialize the figure and its subplots with the keyword argument 'sharey' set to 'True'.
"""
fig, ax = plt.subplots(2, 1, sharey=True)

# EXERCISE 

# Creating small multiples with plt.subplots
"""
*Small multiples are used to plot several datasets side-by-side. In Matplotlib, small multiples can be created using the plt.subplots() function. The first argument is the number of rows in the array of Axes objects generate and the second argument is the number of columns. In this exercise, you will use the Austin and Seattle data to practice creating and populating an array of subplots.
"""
# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2, 2)

# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
ax[0, 0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-NORMAL'])

# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(seattle_weather['MONTH'], seattle_weather['MLY-TAVG-NORMAL'])

# In the bottom left (1, 0) plot month and Austin precipitations
ax[1, 0].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'])

# In the bottom right (1, 1) plot month and Austin temperatures
ax[1, 1].plot(austin_weather['MONTH'], austin_weather['MLY-TAVG-NORMAL'])
plt.show()

# Small multiples with shared y axis
"""
*When creating small multiples, it is often preferable to make sure that the different plots are displayed with the same scale used on the y-axis. This can be configured by setting the sharey key-word to True.
"""
# Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation data in the top axes
ax[0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-NORMAL'], linestyle="-", color = 'b')
ax[0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-25PCTL'], linestyle="--", color = 'b')
ax[0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-75PCTL'], linestyle="--", color = 'b')

# Plot Austin precipitation data in the bottom axes
ax[1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'], linestyle="-", color = 'r')
ax[1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-25PCTL'], linestyle="--", color = 'r')
ax[1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-75PCTL'], linestyle="--", color = 'r')

plt.show()