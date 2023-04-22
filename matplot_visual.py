import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats

# Introducing the pyplot interface

fig, ax = plt.subplots() # figure and axis objects

"""
*The figure (fig) object is the container that holds everything on the page, while axis (ax) is the part of the page that holds data, it is the canvas on which we will draw with our data to visualize it. 
"""
# Load data 
seattle_weather = pd.read_csv('seattle_weather.csv')
austin_weather = pd.read_csv('austin_weather.csv')

# Adding data to axes
ax.plot(seattle_weather['MONTH'], seattle_weather['MLY_TAVG_NORMAL'])
ax.plot(austin_weather['MONTH'], austin_weather['MLY_TAVG_NORMAL'])
plt.show()

# EXERCISE 

# Using the matplotlib.pyplot interface

"""
*There are many ways to use Matplotlib. In this course, we will focus on the pyplot interface, which provides the most flexibility in creating and customizing data visualizations.
"""
# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Call the show function to show the result
plt.show()

# Adding data to an Axes object
"""
*Adding data to a figure is done by calling methods of the Axes object. In this exercise, we will use the plot method to add data about rainfall in two American cities: Seattle, WA and Austin, TX.

*The data are stored in two pandas DataFrame objects: seattle_weather stores information about the weather in Seattle, and austin_weather stores information about the weather in Austin. 

*Each of the DataFrames has a "MONTH" column that stores the three-letter name of the months. Each also has a column named "MLY-PRCP-NORMAL" that stores the average rainfall in each month during a ten-year period.
"""
# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

# Plot MLY-PRCP-NORMAL from austin_weather against MONTH
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Call the show function
plt.show()

# CUSTOMIZING PLOTS

# Adding markers to the plots
ax.plot(seattle_weather['MONTH'], seattle_weather['MLY_TAVG_NORMAL'],
        marker="o") # 0-circle markers

ax.plot(austin_weather['MONTH'], austin_weather['MLY_TAVG_NORMAL'], 
        marker="v") #v-triangle markers
plt.show()
"""
* A list of all matplotlib markers can accessed at https://matplotlib.org/stable/api/markers_api.html
"""

# Setting linestyle 
ax.plot(austin_weather['MONTH'], austin_weather['MLY_TAVG_NORMAL'], 
        marker="v", linestyle='--')
plt.show()
"""
*A list of linestyles is available at https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html#linestyles

*To eliminate the linestyle you pass strine None to linestyle argument. i.e. linestyle='None'.
"""

# Choosing color
ax.plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'], 
        marker='v', linestyle='solid', color='r') # red color for line
plt.show()
"""
*A list of named color can be accessed at https://matplotlib.org/stable/gallery/color/named_colors.html
"""

# Customizing axes labels
"""
*Axis labelling is really important in customization of visuals. 
*In addition to the plot(), the axis object has several methods that start with the word 'set'. These are methods that you can use to change certain properties of the object before calling show() to display it. 
"""
ax.plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'], 
        marker="o", linestyle="dashed", color='g')
ax.set_xlabel("Time (months)")
ax.set_ylabel("Monthly Precipitation")
ax.set_title("Weather in Austin, Texas")
plt.show()

# EXERCISE 

# Customizing data appearance
"""
*We can customize the appearance of data in our plots, while adding the data to the plot, using key-word arguments to the plot command.

*In this exercise, you will customize the appearance of the markers, the linestyle that is used, and the color of the lines and markers for your data.
"""
# Plot Seattle data, setting data appearance
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color='b', marker="o", linestyle="dashed")

# Plot Austin data, setting data appearance
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color='r', marker="v", linestyle="dashed")

# Call show to display the resulting plot
plt.show()

# Customizing axis labels and adding titles
"""
*Customizing the axis labels requires using the set_xlabel and set_ylabel methods of the Axes object. Adding a title uses the set_title method.
"""
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Customize the x-axis label
ax.set_xlabel('Time (months)')

# Customize the y-axis label
ax.set_ylabel('Precipitation (inches)')

# Add the title
ax.set_title('Weather patterns in Austin and Seattle')

# Display the figure
plt.show()