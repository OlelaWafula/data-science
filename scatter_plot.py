import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Scatter Plot 
"""
*Shows the values of different variables across observations - Sometimes called the Bivariate Comparison because it involves the values of two different variables. 
"""
# Load Data
climate_change = pd.read_csv('climate_change.csv', index_col=0)

# visualize Data
fig, ax = plt.subplots()

ax.scatter(climate_change['co2'], climate_change['relative_temp'])
ax.set_xlabel("C02 (ppm)")
ax.set_ylabel("Relative temperature (Celsius)")
plt.show()

# Customizing scatter plots - Bivariate Comparison
eighties = climate_change["1980-01-01":"1989-12-31"]
nineties = climate_change["1990-01-01":"1999-12-31"]

fig, ax = plt.subplots()
ax.scatter(eighties['co2'], eighties['relative_temp'], label='eighties',
            color='blue')
ax.scatter(nineties['co2'], nineties['relative_temp'], label='nineties',
            color='red')
ax.legend()
ax.set_xlabel('C02 (ppm)')
ax.set_ylabel('Relative temperature (Celsius)')
plt.show()

# Encoding a time variable by color
fig, ax = plt.subplots()

ax.scatter(climate_change['co2'], climate_change['relative_temp'], 
           c=climate_change.index)
ax.set_xlabel('CO2 (ppm)')
ax.set_ylabel('Relative temperature (Celsius)')
plt.show()

# EXERCISE 

# Simple scatter plot
"""
*Scatter are a bi-variate visualization technique. They plot each record in the data as a point. The location of each point is determined by the value of two variables: the first variable determines the distance along the x-axis and the second variable determines the height along the y-axis.

*In this exercise, you will create a scatter plot of the climate_change data. This DataFrame, which is already loaded, has a column "co2" that indicates the measurements of carbon dioxide every month and another column, "relative_temp" that indicates the temperature measured at the same time.
"""
# Using the ax.scatter method, add the data to the plot: "co2" on the x-axis and "relative_temp" on the y-axis.
fig, ax = plt.subplots()

# Add data: "co2" on x-axis, "relative_temp" on y-axis
ax.scatter(climate_change['co2'], climate_change['relative_temp'])

# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel('CO2 (ppm)')

# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel('Relative temperature (C)')

plt.show()

# Encoding time by color
"""
*The screen only has two dimensions, but we can encode another dimension in the scatter plot using color. 

*Here, we will visualize the climate_change dataset, plotting a scatter plot of the "co2" column, on the x-axis, against the "relative_temp" column, on the y-axis. 

*We will encode time using the color dimension, with earlier times appearing as darker shades of blue and later times appearing as brighter shades of yellow.
"""
# Using the ax.scatter method add a scatter plot of the "co2" column (x-axis) against the "relative_temp" column.
fig, ax = plt.subplots()

# Add data: "co2", "relative_temp" as x-y, index as color
ax.scatter(climate_change["co2"], climate_change["relative_temp"], c=climate_change.index)

# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel("CO2 (ppm)")

# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel("Relative temperature (C)")

plt.show()