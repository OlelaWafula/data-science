import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Plotting Time-Series Data
"""
*Visualization of time series data are excellent tools to detect patterns in the dataset.
*Continuous variables are organized in terms of time or period.
"""
# Load Data
climate_change = pd.read_csv('climate_change', index_col=False)

# Plot time-series 
fig, ax = plt.subplots()
ax.plot(climate_change.index, climate_change['co2'])
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)')
plt.show()

# Zooming in on a decade - data slicing/subsetting
sixties = climate_change["1960-01-01": "1969-12-31"]
ax.plot(sixties.index, sixties['co2'])
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)')
plt.show()

# EXERCISE - Indexing and Plotting

# Read data with a time index
"""
*pandas DataFrame objects can have an index that denotes time. This is useful because Matplotlib recognizes that these measurements represent time and labels the values on the axis accordingly.

In this exercise, you will read data from a CSV file called climate_change.csv that contains measurements of CO2 levels and temperatures made on the 6th of every month from 1958 until 2016. You will use pandas' read_csv function.

To designate the index as a DateTimeIndex, you will use the parse_dates and index_col key-word arguments both to parse this column as a variable that contains dates and also to designate it as the index for this DataFrame.
"""
# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv', parse_dates = ["date"], index_col="date")
print(climate_change.head())

# Plot time-series data
"""
*To plot time-series data, we use the Axes object plot command. The first argument to this method are the values for the x-axis and the second argument are the values for the y-axis.

*In this case, the index of the DataFrame would be used as the x-axis values and we will plot the values stored in the "relative_temp" column as the y-axis values. We will also properly label the x-axis and y-axis.
"""
fig, ax = plt.subplots()

# Add the time-series for "relative_temp" to the plot
ax.plot(climate_change.index, climate_change['relative_temp'])

# Set the x-axis label
ax.set_xlabel("Time")

# Set the y-axis label
ax.set_ylabel("Relative temperature (Celsius)")

# Show the figure
plt.show()

# Using a time index to zoom in
"""
*When a time-series is represented with a time index, we can use this index for the x-axis when plotting. We can also select a range of dates to zoom in on a particular period within the time-series using pandas' indexing facilities. In this exercise, you will select a portion of a time-series dataset and you will plot that period.
"""
# Use plt.subplots to create fig and ax
fig, ax = plt.subplots()

# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change["1970-01-01": "1979-12-31"]

# Add the time-series for "co2" data from seventies to the plot
ax.plot(seventies.index, seventies["co2"])

# Show the figure
plt.show()

# PLOTTING TIME-SERIES WITH DIFFERENT VARIABLES 
"""

"""

# Using twin axes 
fig, ax = plt.subplots()
ax.plot(climate_change.index, climate_change['co2'], color="blue")
ax.set_xlabel("Time")
ax.set_ylabel("CO2 (ppm)", color="blue")
ax.tick_params('y', colors="blue")
ax2 = ax.twinx() # share the same x - axis but the y axes are separated
ax2.plot(climate_change.index, climate_change["relative_temp"],
          color="red")
ax2.set_ylabel("Relative temperature (Celsius)", color="red")
ax2.tick_params('y', colors="red")
plt.show()

# A function to plot time-series 
def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params('y', color=color)

# EXERCISE 

# Plotting two variables
"""
*f you want to plot two time-series variables that were recorded at the same times, you can add both of them to the same subplot.

*If the variables have very different scales, you'll want to make sure that you plot them in different twin Axes objects. These objects can share one axis (for example, the time, or x-axis) while not sharing the other (the y-axis).

*To create a twin Axes object that shares the x-axis, we use the twinx method.
"""
# Initalize a Figure and Axes
fig, ax = plt.subplots()

# Plot the CO2 variable in blue
ax.plot(climate_change.index, climate_change['co2'], color="blue")

# Create a twin Axes that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature in red
ax2.plot(climate_change.index, climate_change['relative_temp'], color="red")

plt.show()

# Defining a function that plots time-series data
"""
*Once you realize that a particular section of code that you have written is useful, it is a good idea to define a function that saves that section of code for you, rather than copying it to other parts of your program where you would like to use this code.

*Here, we will define a function that takes inputs such as a time variable and some other variable and plots them as x and y inputs. Then, it sets the labels on the x- and y-axis and sets the colors of the y-axis label, the y-axis ticks and the tick labels.
"""
# Define a function called plot_tseries
def plot_tseries(axes, x, y, color, xlabel, ylabel):

  # Plot the inputs x,y in the provided color
  axes.plot(x, y, color=color)

  # Set the x-axis label
  axes.set_xlabel(xlabel)

  # Set the y-axis label
  axes.set_ylabel(ylabel, color=color)

  # Set the colors tick params for y-axis
  axes.tick_params('y', colors=color)

  # Using a plotting function
  """
  *Defining functions allows us to reuse the same code without having to repeat all of it. Programmers sometimes say "Don't repeat yourself".
  """
# In the provided ax object, use the function plot_timeseries to plot the "co2" column in blue, with the x-axis label "Time (years)" and y-axis label "CO2 levels".
fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index, climate_change['co2'], "blue", "Time (years)", "CO2 levels")

# Create a twin Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax2, climate_change.index, 
                climate_change['relative_temp'], 
                "red", "Time (years)", "Relative temperature (Celsius)")
plt.show()

# Annotating time-series data
"""
*Annotations enhance the visualizations. These refer to small pieces of text that refer to a particular part of the visualization. 
"""
# Refresher of previous lessons
def plot_series_time(axes, x, y, color, xlabel, ylabel):
   axes.plot(x, y,)
   axes.set_xlabel(xlabel)
   axes.set_ylabel(ylabel, color=color)
   axes.tick_params('y', color=color)

# Draw attention to particular part of visual using annotation i.e. arrow
fig, ax = plt.subplots()
plot_timeseries(ax, climate_change.index, climate_change["co2"], 'blue', 'Time', 'CO2 (ppm)')

ax2 = ax.twinx()
plot_series_time(ax2, climate_change.index, climate_change["relative_temp"], 'red', 'Time', 'Relative temperature (Celsius)')

# Annotate tyhe point at which relative temperature exceeded 
ax2.annotate(">1 degree", xy=(pd.Timestamp("2015-10-06"), 1),
             xytext=(pd.Timestamp("2008-10-06"), -0.2),
             arrowprops={"arrowstyle":"->", "color":"gray"})
plt.show()
"""
*Options for customizing arrow properties (arrowprops) can be accessed at https://matplotlib.org/2.0.2/users/annotations.html
"""

# EXERCISE 

# Annotating a plot of time-series data
"""
*Annotating a plot allows us to highlight interesting information in the plot. For example, in describing the climate change dataset, we might want to point to the date at which the relative temperature first exceeded 1 degree Celsius.

*For this, we will use the annotate method of the Axes object. In this exercise, you will have the DataFrame called climate_change loaded into memory. Using the Axes methods, plot only the relative temperature column as a function of dates, and annotate the data.
"""
# Use the ax.plot method to plot the DataFrame index against the relative_temp column.
fig, ax = plt.subplots()

# Plot the relative temperature data
ax.plot(climate_change.index, climate_change['relative_temp'])

# Annotate the date at which temperatures exceeded 1 degree
ax.annotate(">1 degree", xy=(pd.Timestamp('2015-10-06'), 1))
plt.show()

# Plotting time-series: putting it all together
"""
*In this exercise, you will plot two time-series with different scales on the same Axes, and annotate the data from one of these series.

*The CO2/temperatures data is provided as a DataFrame called climate_change. You should also use the function that we have defined before, called plot_timeseries, which takes an Axes object (as the axes argument) plots a time-series (provided as x and y arguments), sets the labels for the x-axis and y-axis and sets the color for the data, and for the y tick/axis labels:

          plot_timeseries(axes, x, y, color, xlabel, ylabel)

*Then, you will annotate with text an important time-point in the data: on 2015-10-06, when the temperature first rose to above 1 degree over the average.
"""
# Use the plot_timeseries function to plot CO2 levels against time. Set xlabel to "Time (years)" ylabel to "CO2 levels" and color to 'blue'.
fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index, climate_change['co2'], 'blue', 'Time (years)', 'CO2 levels')

# Create an Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], 'red', 'Time (years)', 'Relative temp (Celsius)')

# Annotate point with relative temperature >1 degree
ax2.annotate(">1 degree", xy=(pd.Timestamp('2015-10-06'), 1),  xytext=(pd.Timestamp("2008-10-06"), -0.2), 
arrowprops={"arrowstyle":"->", "color":"gray"})

plt.show()