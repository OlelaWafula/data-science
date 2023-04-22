import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Count and Bar plots
"""
*Used to visualize categorical variables.
*Categorical plots involves a categorical variable - variable that consists of fixed typically small number of possible values for categories.
*These plots are used when making comparisons between different groups.
"""
# Load Data 
masculinity_data = sns.load_dataset("masculinity_data")

# count plot using catplot()
sns.catplot(x="how_masculine", data=masculinity_data, kind="count")
plt.show()

# Change order of categories create a list of categories in the desired order and use the order parameter of catplot():
category_order = [
    "No Answer",
    "Not at all",
    "Not very",
    "Somewhat",
    "Very"
]
sns.catplot(x="how_masculine", data=masculinity_data, kind="count", order=category_order)
plt.show()

# Bar plots 
"""
*Displays the mean of quantitative variable per category.
"""
# Load Data
tips = sns.load_dataset("tips")
sns.catplot(x="day", y="total_bill", data=tips, kind="bar")
plt.show()
"""
*Seaborn automatically shows the lines indicating the 95% confidence intervals for the mean, showing the level of uncertainity about the estimates. 
*Assuming our data is a random sample, we can be 95% sure that the true population mean in each group rise within the confidence interval shown. 
*To turn the confidence intervals we set the ci parameter to None. i.e. ci=None.
*To change the orientation of bar plot, switch the x and y parameters. However, it is a common practice to place categorical variable on the x - axis.
"""
sns.catplot(y="day", x="total_bill", data=tips, kind="bar", ci=None)
plt.show()

# EXERCISE 

# Count plots
"""
*In this exercise, we'll return to exploring our dataset that contains the responses to a survey sent out to young people. We might suspect that young people spend a lot of time on the internet, but how much do they report using the internet each day? 

*Let's use a count plot to break down the number of survey responses in each category and then explore whether it changes based on age.
"""
# Load Data
survey_data = sns.load_dataset("survey_data")

# Use sns.catplot() to create a count plot using the survey_data DataFrame with "Internet usage" on the x-axis.
sns.catplot(x="Internet usage", data=survey_data, kind="count")
plt.show()

# Make the bars horizontal instead of vertical.
sns.catplot(y="Internet usage", data=survey_data, kind="count")
plt.show()

# Separate this plot into two side-by-side column subplots based on "Age Category", which separates respondents into those that are younger than 21 vs. 21 and older.
sns.catplot(y="Internet usage", data=survey_data,
            kind="count", col="Age Category")
plt.show()
"""
It looks like most young people use the internet for a few hours every day, regardless of their age.
"""
# Bar plots with percentages
"""
*Let's continue exploring the responses to a survey sent out to young people. The variable "Interested in Math" is True if the person reported being interested or very interested in mathematics, and False otherwise. What percentage of young people report being interested in math, and does this vary based on gender? Let's use a bar plot to find out.
"""
# Use the survey_data DataFrame and sns.catplot() to create a bar plot with "Gender" on the x-axis and "Interested in Math" on the y-axis.
sns.catplot(x="Gender", y="Interested in Math", data=survey_data, kind="bar")
plt.show()
"""
When the y-variable is True/False, bar plots will show the percentage of responses reporting True. This plot shows us that males report a much higher interest in math compared to females.
"""
# Customizing bar plots
"""
*In this exercise, we'll explore data from students in secondary school. The "study_time" variable records each student's reported weekly study time as one of the following categories: "<2 hours", "2 to 5 hours", "5 to 10 hours", or ">10 hours". Do students who report higher amounts of studying tend to get better final grades? Let's compare the average final grade among students in each category using a bar plot.
"""
# Load Data
student_data = sns.load_dataset("student_data") 

# Use sns.catplot() to create a bar plot with "study_time" on the x-axis and final grade ("G3") on the y-axis, using the student_data DataFrame.
sns.catplot(x="study_time", y="G3", data=student_data, kind="bar")
plt.show()

# Using the order parameter and the category_order list that is provided, rearrange the bars so that they are in order from lowest study time to highest.
category_order = ["<2 hours", 
                  "2 to 5 hours", 
                  "5 to 10 hours", 
                  ">10 hours"]

# Rearrange the categories
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar", order=category_order)
plt.show()

# Update the plot so that it no longer displays confidence intervals.
category_order = ["<2 hours", 
                  "2 to 5 hours", 
                  "5 to 10 hours", 
                  ">10 hours"]

# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=category_order, ci=None)
plt.show()
"""
Students in our sample who studied more have a slightly higher average grade, but it's not a strong relationship.
"""
