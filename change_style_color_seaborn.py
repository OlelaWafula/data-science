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
# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower"
g.fig.suptitle("Car Weight vs. Horsepower")
plt.show()
"""
It looks like a car's weight is positively correlated with its horsepower.
"""

# Additing title to AxesSubplot
"""
*To add a title, assign the plot yo a variable and use g.set_title()
"""
g = sns.boxplot(x="Region", y="Birthrate", data=gdp_data)
g.set_title("New Title", y=1.03) # "y" parameter is used to adjust the height of the title

# Titles for subplots
"""
*Let's assume that we have divided countries into two groups - group one and group two, and we have set col="Group" to create a subplot for each group.
*Since g is a FacetGrid object, using g.fig.suptitle() will add a title to the figure as a whole.
*To alter the subplot titles use g.set_titles() to set the titles for each AxesSubplots
"""
g = sns.catplot(x="Region", y="Birthrate", data=gdp_data, kind="bar", col="Group")
g.fig.suptitle("New Title", y=1.03)
g.set_titles("This is {col_name}")

# Adding axis labels
"""
*To add axis labels, assign the plot to a variable and then call the set() function. Set the parameters "x label" and "y label" to set the desired x-axis and y-axis labels respectively. This works with both FacetGrid and AxesSubplot objects. 
"""
g = sns.catplot(x="Region", y="Birthrate", data=gdp_data, kind="box")
g.set(xlabel="New X Label", ylabel="New Y Label")
plt.show()

# Rotating x-axis tick labels 
"""
*Your tick labels may overlap, making it hard to interpret the plot.
*One way to address this is by rotating the tick labels, to do this we don't call a function on the object itself, instead after we create the plot, we call the matplotlib function plt.xticks() and set rotation equal to 90 degrees. This works with both FacetGrid and AxesSubplot objects.
"""
g = sns.catplot(x="Region", y="Birthrate", data=gdp_data, kind="box")
plt.xticks(rotation=90)
plt.show()

# EXERCISE 

# Load dataset
mpg_mean = sns.load_dataset("mpg_mean")

# Adding a title and axis labels
"""
*Let's continue to look at the miles per gallon dataset. This time we'll create a line plot to answer the question: How does the average miles per gallon achieved by cars change over time for each of the three places of origin? To improve the readability of this plot, we'll add a title and more informative axis labels.
*In the code provided, we create the line plot using the lineplot() function. Note that lineplot() does not support the creation of subplots, so it returns an AxesSubplot object instead of an FacetGrid object.
"""
# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")
plt.show()

# Label the x-axis as "Car Model Year" and the y-axis as "Average MPG".

# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels
g.set(xlabel="Car Model Year", ylabel="Average MPG")
plt.show()
"""
The average miles per gallon achieved is increasing over time for all three places of origin, but the USA is always lower than Europe and Japan.
"""

# Rotating x-tick labels
"""
*In this exercise, we'll continue looking at the miles per gallon dataset. In the code provided, we create a point plot that displays the average acceleration for cars in each of the three places of origin. Note that the "acceleration" variable is the time to accelerate from 0 to 60 miles per hour, in seconds. Higher values indicate slower acceleration.
*et's use this plot to practice rotating the x-tick labels. Recall that the function to rotate x-tick labels is a standalone Matplotlib function and not a function applied to the plot object itself.
"""
# Create point plot
sns.catplot(x="origin", 
            y="acceleration", 
            data=mpg, 
            kind="point", 
            join=False, 
            capsize=0.1)

# Rotate x-tick labels
plt.xticks(rotation=90)
plt.show()
"""
Since higher values indicate slower acceleration, it looks like cars from Japan and Europe have significantly slower acceleration compares to the USA.
"""

# Box plot with subgroups
"""
*In this exercise, we'll look at the dataset containing responses from a survey given to young people. One of the questions asked of the young people was: "Are you interested in having pets?" Let's explore whether the distribution of ages of those answering "yes" tends to be higher or lower than those answering "no", controlling for gender.
"""
# Set palette to "Blues"
sns.set_palette("Blues")

# Adjust to add subgroups based on "Interested in Pets"
g = sns.catplot(x="Gender",
                y="Age", data=survey_data, 
                kind="box", hue="Interested in Pets")

# Set title to "Age of Those Interested in Pets vs. Not"
g.fig.suptitle("Age of Those Interested in Pets vs. Not")
plt.show()
"""
After controlling for gender, it looks like the age distributions of people who are interested in pets are similar than those who aren't.
"""

# Bar plot with subgroups and subplots
"""
*In this exercise, we'll return to our young people survey dataset and investigate whether the proportion of people who like techno music ("Likes Techno") varies by their gender ("Gender") or where they live ("Village - town"). This exercise will give us an opportunity to practice the many things we've learned throughout this course!
"""
# Set the figure style to "dark"
sns.set_style("dark")

# Adjust to add subplots per gender
g = sns.catplot(x="Village - town", y="Likes Techno", 
                data=survey_data, kind="bar",
                col="Gender")

# Add title and axis labels
g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel="Location of Residence", 
       ylabel="% Who Like Techno")
plt.show()
