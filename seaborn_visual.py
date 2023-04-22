import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# Seaborn
"""
*Seaborn is a python data visualization library.
*Developed in order to make it easy to create the most common types of plots.
*Data analysis workflow:

Gather Data ==> Transform & Clean ==> Explore ==> Analyze & Build Models ==> Communicate Results

*Seaborn is useful in the Exploration of data and Communication of Results. 

*Advantages of Seaborn:
    .Make data visualization easy - automatically handles a lot of complexity behind the scene. 
    .Works extremely well with pandas data structures.
    .It is built on top of matplotlib library - seaborn allows the use of matplotlib fliexibility or avoiding the complexity of matplotlib if need be.
"""
# Scatter plot 
height = [62, 64, 69, 75, 66, 68, 65, 71, 76, 73]
weight = [120, 136, 148, 175, 137, 165, 154, 172, 200, 187]

# Visualize 
sns.scatterplot(x=height, y=weight)
fig.savefig("height_weight.png")

# Count plot
gender = ["Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male"]
sns.countplot(x=gender)
plt.show()

# EXERCISE 

# Making a scatter plot with lists
"""
*In this exercise, we'll use a dataset that contains information about 227 countries. This dataset has lots of interesting information on each country, such as the country's birth rates, death rates, and its gross domestic product (GDP). GDP is the value of all the goods and services produced in a year, expressed as dollars per person.

*We've created three lists of data from this dataset to get you started. gdp is a list that contains the value of GDP per country, expressed as dollars per person. phones is a list of the number of mobile phones per 1,000 people in that country. 

*Finally, percent_literate is a list that contains the percent of each country's population that can read and write.
"""
# Data Samples 
gdp = []
phones = []
percent_literate = []
region = []

# Create a scatter plot of GDP (gdp) vs. number of phones per 1000 people (phones).
sns.scatterplot(x=gdp, y=phones)
plt.show()

# Change the scatter plot so it displays the percent of the population that can read and write (percent_literate) on the y-axis.
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()
"""
While this plot does not show a linear relationship between GDP and percent literate, countries with a lower GDP do seem more likely to have a lower percent of the population that can read and write.
"""
# Making a count plot with a list
"""
*n the last exercise, we explored a dataset that contains information about 227 countries. Let's do more exploration of this data - specifically, how many countries are in each region of the world?

*To do this, we'll need to use a count plot. Count plots take in a categorical list and return bars that represent the number of list entries per category. You can create one here using a list of regions for each country, which is a variable named region.
"""
# Use Seaborn to create a count plot with region on the y-axis.
sns.countplot(y=region)
plt.show()
"""
Sub-Saharan Africa contains the most countries in this list. 
"""

