import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Statistical Plotting
"""
*Are set of methods for using visualization to make comparisons:
        i. Adding error bars to bar charts - Additional markers that tell us something about the distribution of data.
"""
# Load Data
mens_rowing = pd.read_csv('mens_rowing.csv', index_col=0)
mens_gymnastics = pd.read_csv('mens_gymnastics.csv', index_col=0)

# Visualize Data
fig, ax = plt.subplots()

ax.bar("Rowing", mens_rowing["Height"].mean(), 
       yerr=mens_rowing["Height"].std())
ax.bar("Gymnastics", mens_gymnastics["Height"].mean(),
       yerr=mens_gymnastics["Height"].std())
ax.set_ylabel("Height (cm)")
plt.show()

# Adding error bars to a line plot

# Load weather data
seattle_weather = pd.read_csv('seattle_weather.csv')
austin_weather = pd.read_csv('seattle_weather.csv')

fig, ax = plt.subplots()

ax.errorbar(seattle_weather["MONTH"], 
            seattle_weather["MLY-TAVG-NORMAL"],
            yerr=seattle_weather["MLY-TAVG-STDDEV"])
ax.errorbar(austin_weather["MONTH"], 
            seattle_weather["MLY-TAVG-NORMAL"],
            yerr=seattle_weather["MLY-TAVG-STDDEV"])
ax.set_ylabel("Temperature (Fahrenheit)")
plt.show()

# Adding Boxplots
fig, ax = plt.subplots()

ax.boxplot([mens_rowing["Height"], mens_gymnastics["Height"]])
ax.set_xticklabels(["Rowing", "Gymnastics"])
ax.set_ylabel("Height (cm)")
plt.show()

# EXERCISE

# Adding error-bars to a bar chart
"""
*Statistical plotting techniques add quantitative information for comparisons into the visualization. For example, in this exercise, we will add error bars that quantify not only the difference in the means of the height of medalists in the 2016 Olympic Games, but also the standard deviation of each of these groups, as a way to assess whether the difference is substantial relative to the variability within each group.

*For the purpose of this exercise, you will have two DataFrames: mens_rowing holds data about the medalists in the rowing events and mens_gymnastics will hold information about the medalists in the gymnastics events.
"""
# Add a bar with size equal to the mean of the "Height" column in the mens_rowing DataFrame and an error-bar of its standard deviation.
fig, ax = plt.subplots()

# Add a bar for the rowing "Height" column mean/std
ax.bar("Rowing", mens_rowing['Height'].mean(), yerr=mens_rowing['Height'].std())

# Add a bar for the gymnastics "Height" column mean/std
ax.bar("Gymnastics", mens_gymnastics['Height'].mean(), yerr=mens_gymnastics['Height'].std())

# Label the y-axis
ax.set_ylabel("Height (cm)")

plt.show()

# Adding error-bars to a plot
"""
*Adding error-bars to a plot is done by using the errorbar method of the Axes object.

*Here, you have two DataFrames loaded: seattle_weather has data about the weather in Seattle and austin_weather has data about the weather in Austin. Each DataFrame has a column "MONTH" that has the names of the months, a column "MLY-TAVG-NORMAL" that has the average temperature in each month and a column "MLY-TAVG-STDDEV" that has the standard deviation of the temperatures across years.

*In the exercise, you will plot the mean temperature across months and add the standard deviation at each point as y errorbars.
"""
# Use the ax.errorbar method to add the Seattle data: the "MONTH" column as x values, the "MLY-TAVG-NORMAL" as y values and "MLY-TAVG-STDDEV" as yerr values.
fig, ax = plt.subplots()

# Add Seattle temperature data in each month with error bars
ax.errorbar(seattle_weather['MONTH'], seattle_weather['MLY-TAVG-NORMAL'], yerr=seattle_weather['MLY-TAVG-STDDEV'])

# Add Austin temperature data in each month with error bars
ax.errorbar(austin_weather['MONTH'], austin_weather['MLY-TAVG-NORMAL'], yerr=austin_weather['MLY-TAVG-STDDEV']) 

# Set the y-axis label
ax.set_ylabel("Temperature (Fahrenheit)")

plt.show()

# Creating boxplots
"""
*Boxplots provide additional information about the distribution of the data that they represent. They tell us what the median of the distribution is, what the inter-quartile range is and also what the expected range of approximately 99% of the data should be. Outliers beyond this range are particularly highlighted.

*In this exercise, you will use the data about medalist heights that you previously visualized as histograms, and as bar charts with error bars, and you will visualize it as boxplots.

*Again, you will have the mens_rowing and mens_gymnastics DataFrames available to you, and both of these DataFrames have columns called "Height" that you will compare.
"""
# Create a boxplot that contains the "Height" column for mens_rowing on the left and mens_gymnastics on the right.
fig, ax = plt.subplots()

# Add a boxplot for the "Height" column in the DataFrames
ax.boxplot([mens_rowing['Height'], mens_gymnastics['Height']])

# Add x-axis tick labels:
ax.set_xticklabels(["Rowing", "Gymnastics"])

# Add a y-axis label
ax.set_ylabel("Height (cm)")

plt.show()