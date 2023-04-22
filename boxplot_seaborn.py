import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Boxplot
"""
*Shows the distribution of quantitative data.
*The colored box represents the 25th t0 75th percentiles and the line at the middle of the box represents the median.
*The whiskers gives us the sense of distribution and the floating points represents outliers. 
*Boxplots are used to compare the distribution of a quantitative variable across different groups of the categorical variables 
"""
# Load Data 
tips = sns.load_dataset("tips")

# Create a Boxplot in seaborn
g = sns.catplot(x="time", y="total_bill", data=tips, kind="box", order=["Dinner", "Lunch"])
plt.show()

# To ommit outliers from the plot, pass an empty string into sym parameter. sym can also be used to change the appearance of the outliers instead of ommiting them.
h = sns.catplot(x="time", y="total_bill", data=tips, kind="box", order=["Dinner", "Lunch"], sym="")
plt.show()

# Changing the whiskers using 'whis'
"""
*By default, the whiskers extend to 1.5 * the interquartile range (IQR).
*The IQR is the 25th to the 75th percentile of the distribution of data. 
*To change the way the whiskers in a boxplot are defined, use the 'whis' parameter.
*You can change the range of whiskers from 1.5 * IQR which is the default to 2 * IQR by setting whis=2.0.
*Alternatively, you can have the whiskers define specific lower and upper percentiles by passing in a list of the lower and upper values.e.g. whis=[5,95]; lower whisker draw at 5th percentile and the upper whisker drawn at 95th percentile.
*To draw the whiskers at min and max values use, whis=[0, 100].
"""
# Example whis=[0, 100] i.e. whisker set to min and max values
g= sns.catplot(x="time", y="total_bill", data=tips, kind="box", whis=[0, 100])
plt.show()
"""
There are no outliers because the box and whiskers cover the entire range of the data.
"""
# EXERCISE

# Load Data
student_data = sns.load_dataset("student_data")

# Create and interpret a box plot
"""
*Let's continue using the student_data dataset. In an earlier exercise, we explored the relationship between studying and final grade by using a bar plot to compare the average final grade ("G3") among students in different categories of "study_time".
"""
# Use sns.catplot() and the student_data DataFrame to create a box plot with "study_time" on the x-axis and "G3" on the y-axis. Set the ordering of the categories to study_time_order.

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
g = sns.catplot(x="study_time", y="G3", data=student_data, kind="box", order=study_time_order)
plt.show()

# Omitting outliers
"""
*Now let's use the student_data dataset to compare the distribution of final grades ("G3") between students who have internet access at home and those who don't. To do this, we'll use the "internet" variable, which is a binary (yes/no) indicator of whether the student has internet access at home.

*Since internet may be less accessible in rural areas, we'll add subgroups based on where the student lives. For this, we can use the "location" variable, which is an indicator of whether a student lives in an urban ("Urban") or rural ("Rural") location.
"""
# Use sns.catplot() to create a box plot with the student_data DataFrame, putting "internet" on the x-axis and "G3" on the y-axis.
# Create a box plot with subgroups and omit the outliers

g = sns.catplot(x="internet", y="G3", data=student_data, kind="box", hue="location", sym="")
plt.show()
"""
The median grades are quite similar between each group, but the spread of the distribution looks larger among students who have internet access.
"""
# Adjusting the whiskers
"""
*In the lesson we saw that there are multiple ways to define the whiskers in a box plot. In this set of exercises, we'll continue to use the student_data dataset to compare the distribution of final grades ("G3") between students who are in a romantic relationship and those that are not. We'll use the "romantic" variable, which is a yes/no indicator of whether the student is in a romantic relationship.

*Let's create a box plot to look at this relationship and try different ways to define the whiskers.
"""
# Adjust the code to make the box plot whiskers to extend to 0.5 * IQR. Recall: the IQR is the interquartile range.
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box", whis=0.5)

plt.show()

# Change the code to set the whiskers to extend to the 5th and 95th percentiles.
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 95])
plt.show()

# Change the code to set the whiskers to extend to the min and max values.
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 100])
plt.show()
"""
The median grade is the same between these two groups, but the max grade is higher among students who are not in a romantic relationship.
"""