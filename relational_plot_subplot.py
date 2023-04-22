import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Relational plots and subplots
"""
*Creating a separate plot per subgroup using relplot() i.e. relational plot - enables the visualization between two quantitative variables using either scatter plots or line plots. 

*Why use relplot() instead of scatterplot()?
    .relplot() lets you create subplots in a single figure.

"""
# Load Data 
tips = sns.load_dataset("tips")

# Visualize using relplot()
sns.relplot(x="total_bill", y="tip", data=tips, kind="scatter", col="smoker") # col="smoker" enables us to get two subplots of the smoker category i.e. Yes or No. To range subplots in as row we use row="smoker" or use both row and col i.e. col="smoker", col="time"
plt.show()

"""
* we can use col_wrap=2, col_order=["Thu", "Fri", "Sat", "Sun"]
"""

# EXERCISE 

# Creating subplots with col and row
"""
*We've seen in prior exercises that students with more absences ("absences") tend to have lower final grades ("G3"). Does this relationship hold regardless of how much time students study each week?

*To answer this, we'll look at the relationship between the number of absences that a student has in school and their final grade in the course, creating separate subplots based on each student's weekly study time ("study_time").
"""
# Load Data 
student_data = sns.load_dataset('student_data')

# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")

# Show plot
plt.show()

# Creating two-factor subplots
"""
*Let's continue looking at the student_data dataset of students in secondary school. Here, we want to answer the following question: does a student's first semester grade ("G1") tend to correlate with their final grade ("G3")?

*There are many aspects of a student's life that could result in a higher or lower final grade in the class. For example, some students receive extra educational support from their school ("schoolsup") or from their family ("famsup"), which could result in higher grades. Let's try to control for these two factors by creating subplots based on whether the student received extra educational support from their school or family.
"""
# Use relplot() to create a scatter plot with "G1" on the x-axis and "G3" on the y-axis, using the student_data DataFrame.
sns.relplot(x="G1", y="G3", kind="scatter", data=student_data)
plt.show()

# Create column subplots based on whether the student received support from the school ("schoolsup"), ordered so that "yes" comes before "no".
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", col="schoolsup", col_order=["yes", "no"])
plt.show()

# Add row subplots based on whether the student received support from the family ("famsup"), ordered so that "yes" comes before "no". This will result in subplots based on two factors.
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"], row="famsup", row_order=["yes", "no"])
plt.show()
"""
It looks like the first semester grade does correlate with the final grade, regardless of what kind of support the student received.
"""

# Customizing scatter plots

# Subgroups with point size 
sns.relplot(x="total_bill", y="tip", data=tips, kind="scatter", size="size", hue="size")
plt.show()

# Subgroups with point sytle
sns.relplot(x="total_bill", y="tip", data=tips, kind="scatter", hue="smoker", style="smoker")
plt.show()

# Changing Point Transparency
sns.relplot(x="total_bill", y="tip", data=tips, kind="scatter", alpha=0.4)
plt.show()

# EXERCISE 

# Changing the size of scatter plot points

# Load Data 
mpg = sns.load_dataset("mpg")

"""
*In this exercise, we'll explore Seaborn's mpg dataset, which contains one row per car model and includes information such as the year the car was made, the number of miles per gallon ("M.P.G.") it achieves, the power of its engine (measured in "horsepower"), and its country of origin.

*What is the relationship between the power of a car's engine ("horsepower") and its fuel efficiency ("mpg")? And how does this relationship vary by the number of cylinders ("cylinders") the car has? Let's find out.
"""
# Use relplot() and the mpg DataFrame to create a scatter plot with "horsepower" on the x-axis and "mpg" on the y-axis. Vary the size of the points by the number of cylinders in the car ("cylinders").
sns.relplot(x="horsepower", y="mpg", data=mpg, kind="scatter", size="cylinders")
plt.show()

# To make this plot easier to read, use hue to vary the color of the points by the number of cylinders in the car ("cylinders").
sns.relplot(x="horsepower", y="mpg", data=mpg, kind="scatter", size="cylinders", hue="cylinders")
plt.show()
"""
Cars with higher horsepower tend to get a lower number of miles per gallon. They also tend to have a higher number of cylinders.
"""
# Changing the style of scatter plot points
"""
*Let's continue exploring Seaborn's mpg dataset by looking at the relationship between how fast a car can accelerate ("acceleration") and its fuel efficiency ("mpg"). Do these properties vary by country of origin ("origin")?

*Note that the "acceleration" variable is the time to accelerate from 0 to 60 miles per hour, in seconds. Higher values indicate slower acceleration.
"""
# Use relplot() and the mpg DataFrame to create a scatter plot with "acceleration" on the x-axis and "mpg" on the y-axis. Vary the style and color of the plot points by country of origin ("origin").
sns.relplot(x="acceleration", y="mpg", data=mpg, kind="scatter", style="origin", hue="origin")
plt.show()
"""
Cars from the USA tend to accelerate more quickly and get lower miles per gallon compared to cars from Europe and Japan.
"""