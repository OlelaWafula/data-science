import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Using pandas and Seaborn
"""
*pandas is used for data analysis, it can read datasets from many types of files. 
*Seaborn works with pandas DataFrames if data is tidy i.e. each observation has its own row and each variable has its own column. Thefore data must be clean.
"""
# Load Data 
df = pd.read_csv("masculinity.csv")
print(df.head()) # Top 5 rows

# Using DataFrames with countplot()
sns.countplot(x="how_masculine", data=df) # 'how_masculine' is a column in df DataFrame.
plt.show()

# EXERCISE 

# "Tidy" vs. "untidy" data
"""
*Here, we have a sample dataset from a survey of children about their favorite animals. But can we use this dataset as-is with Seaborn? Let's use pandas to import the csv file with the data collected from the survey and determine whether it is tidy, which is essential to having it work well with Seaborn.

*To get you started, the filepath to the csv file has been assigned to the variable csv_filepath

*Note that because csv_filepath is a Python variable, you will not need to put quotation marks around it when you read the csv.
"""
csv_filepath = "name_and_age.csv"
# Read the csv file located at csv_filepath into a DataFrame named df.
df = pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())
"""
*Always make sure to check if your DataFrame is tidy before using it with Seaborn.
"""
# Always make sure to check if your DataFrame is tidy before using it with Seaborn.
"""
*In this exercise, we'll look at the responses to a survey sent out to young people. Our primary question here is: how many young people surveyed report being scared of spiders? Survey participants were asked to agree or disagree with the statement "I am afraid of spiders". Responses vary from 1 to 5, where 1 is "Strongly disagree" and 5 is "Strongly agree".

*To get you started, the filepath to the csv file with the survey data has been assigned to the variable csv_filepath.

*Note that because csv_filepath is a Python variable, you will not need to put quotation marks around it when you read the csv.
"""
# Use the countplot() function with the x= and data= arguments to create a count plot with the "Spiders" column values on the x-axis.

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x='Spiders', data=df)

# Display the plot
plt.show()
"""
This plot shows us that most young people reported not being afraid of spiders.
"""
# Adding a third variable with hue

# Load dataset using seaborn
tips = sns.load_dataset("tips")
print(tips.head())

# plot a scatter plot of total_bill and tips columns

# customized colors 
hue_colors={"Yes": "#808080", "No":"#00FF00"} 

sns.scatterplot(x="total_bill", y="tips", data=tips, hue="smoker", hue_order=["Yes", "No"], palette=hue_colors) # hue used to categorize
plt.show()

"""
*hue is available in most of the seaborn plot types.
"""
# Using hue on countplot()
sns.countplot(x="smoker", data=tips, hue="sex")
plt.show()

# EXERCISE 

# Hue and scatter plots
"""
*In the prior video, we learned how hue allows us to easily make subgroups within Seaborn plots. Let's try it out by exploring data from students in secondary school. We have a lot of information about each student like their age, where they live, their study habits and their extracurricular activities.

*For now, we'll look at the relationship between the number of absences they have in school and their final grade in the course, segmented by where the student lives (rural vs. urban area).
"""
# Load data 
student_data = sns.load_dataset("student_data")

# Create a scatter plot with "absences" on the x-axis and final grade ("G3") on the y-axis using the DataFrame student_data. Color the plot points based on "location" (urban vs. rural).
sns.scatterplot(x="absences", y="G3", hue="location", data=student_data)
plt.show()

# Make "Rural" appear before "Urban" in the plot legend.
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location", hue_order=["Rural", "Urban"])
plt.show()
"""
*It looks like students with higher absences tend to have lower grades in both rural and urban areas.
"""
# Hue and count plots
"""
*Let's continue exploring our dataset from students in secondary school by looking at a new variable. The "school" column indicates the initials of which school the student attended - either "GP" or "MS".

*In the last exercise, we created a scatter plot where the plot points were colored based on whether the student lived in an urban or rural area. How many students live in urban vs. rural areas, and does this vary based on what school the student attends? Let's make a count plot with subgroups to find out.
"""
# Fill in the palette_colors dictionary to map the "Rural" location value to the color "green" and the "Urban" location value to the color "blue".
#Create a count plot with "school" on the x-axis using the student_data DataFrame.
#Add subgroups to the plot using "location" variable and use the palette_colors dictionary to make the location subgroups green and blue.
palette_colors = {"Rural": "green", "Urban": "blue"}
sns.countplot(x="school", hue="location", palette=palette_colors, data=student_data)
plt.show()
"""
*Students at GP tend to come from an urban location, but students at MS are more evenly split.
"""