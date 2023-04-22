import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
survey_data = sns.load_dataset("survey_data")

# Changing plot style and color
"""
*Seaborn has preset figure style options: white, dark, whitegrid, darkgrid and ticks. To set one of this as the global style use sns.set_style("dark")
*Changing palette use sns.palette("RdBu")
*custom_palette = ["red", "green", "yellow"]
        
        sns.set_palette(custom_palette)

*Change scale of the plot using sns.set_context() scale from smallest to largest: paper, notebook, talk and poster. Default context is paper.
"""
# EXERCISE 

# Changing style and palette
"""
*Let's return to our dataset containing the results of a survey given to young people about their habits and preferences. We've provided the code to create a count plot of their responses to the question "How often do you listen to your parents' advice?". Now let's change the style and palette to make this plot easier to interpret.
"""
# Set the style to "whitegrid" to help the audience determine the number of responses in each category.

# Set the style to "whitegrid"
sns.set_style("whitegrid")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", "Often", "Always"]

sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)

# Show plot
plt.show()

# Set the color palette to the sequential palette named "Purples".
sns.set_style("whitegrid")
sns.set_palette("Purples")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", "Often", "Always"]

sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)

# Show plot
plt.show()

# Change the color palette to the diverging palette named "RdBu".
sns.set_style("whitegrid")
sns.set_palette("RdBu")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", "Often", "Always"]

sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)

# Show plot
plt.show()
"""
This style and diverging color palette best highlights the difference between the number of young people who usually listen to their parents' advice versus those who don't.
"""

# Changing the scale
"""
In this exercise, we'll continue to look at the dataset containing responses from a survey of young people. Does the percentage of people reporting that they feel lonely vary depending on how many siblings they have? Let's find out using a bar plot, while also exploring Seaborn's four different plot scales ("contexts").
"""
# Set the scale ("context") to "paper", which is the smallest of the scale options.
sns.set_context("paper")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely", data=survey_data, kind="bar")

# Show plot
plt.show()

# Change the context to "notebook" to increase the scale.
sns.set_context("notebook")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely", data=survey_data, kind="bar")

# Show plot
plt.show()

# Change the context to "talk" to increase the scale.
sns.set_context("talk")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely", data=survey_data, kind="bar")

# Show plot
plt.show()

# Change the context to "poster", which is the largest scale available.
sns.set_context("poster")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely", data=survey_data, kind="bar")

# Show plot
plt.show()

"""
Each context name gives Seaborn's suggestion on when to use a given plot scale (in a paper, in an iPython notebook, in a talk/presentation, or in a poster session).
"""
# Using a custom palette
"""
*So far, we've looked at several things in the dataset of survey responses from young people, including their internet usage, how often they listen to their parents, and how many of them report feeling lonely. However, one thing we haven't done is a basic summary of the type of people answering this survey, including their age and gender. Providing these basic summaries is always a good practice when dealing with an unfamiliar dataset.
"""
# Set the style to "darkgrid"
sns.set_style("darkgrid")

# Set a custom color palette
custom_color = ["#39A7D0", "#36ADA4"]
sns.set_palette(custom_color)

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", 
            data=survey_data, kind="box")

# Show plot
plt.show()
"""
It looks like the median age is the same for males and females, but distribution of females skews younger than the males.
"""
# Load Dataset
df = sns.load_dataset("df")

# Adding Titles and Labels
"""
FacetGrid v. AxesSubplot objects

Object Type             Plot Types                      Characteristics
FacetGrid               relplot(), catplot()            Can create subplots
AxesSubplot             scatterplot(), countplot()      only creates a single plot
"""
g = sns.scatterplot(x="height", y="weight", data=df)
print(type(g)) # matplotlib.axes._subplots.AxesSubplot

# Load Dataset
gdp_data = sns.load_dataset("gdp_data")

# Adding a title to FacetGrid
g = sns.catplot(x="Region", y="Birthrate", data=gdp_data, kind="box")
g.fig.suptitle("New Title", y=1.03)
plt.show()

# FacetGrids vs. AxesSubplots 
"""
*In the recent lesson, we learned that Seaborn plot functions create two different types of objects: FacetGrid objects and AxesSubplot objects. The method for adding a title to your plot will differ depending on the type of object it is.
*In the code provided, we've used relplot() with the miles per gallon dataset to create a scatter plot showing the relationship between a car's weight and its horsepower. This scatter plot is assigned to the variable name g. Let's identify which type of object it is.
"""
# Load Dataset
mpg = sns.load_dataset("mpg")

# Identify what type of object plot g is and assign it to the variable type_of_g.
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Identify plot type
type_of_g = type(g)

# Print type
print(type_of_g)

# Adding a title to a FacetGrid object
"""
*In the previous exercise, we used relplot() with the miles per gallon dataset to create a scatter plot showing the relationship between a car's weight and its horsepower. This created a FacetGrid object. Now that we know what type of object it is, let's add a title to this plot.
"""