import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Automating Figures from Data
"""
* Why automate?
    .Ease and speed
    .Flexibility
    .Robustness
    .Reproducibility
"""
# Load Data
summer_2016_medals = pd.read_csv('summer_olympic_medals.csv', index_col=0)

#Getting unique values of a column
sports = summer_2016_medals["Sport"].unique()
print(sports)

# Bar-chart of heights for all sports
fig, ax = plt.subplots()

for sport in sports:
    sport_df = summer_2016_medals[summer_2016_medals["Sport"] == sport]
    ax.bar(sport, sport_df["Height"].mean(), 
           yerr=sport_df["Height"].std())
    
ax.set_ylabel("Height (cm)")
ax.set_xticklabels(sports, rotation=90)
plt.show()

# EXERCISE 

# Unique values of a column
"""
*One of the main strengths of Matplotlib is that it can be automated to adapt to the data that it receives as input. For example, if you receive data that has an unknown number of categories, you can still create a bar plot that has bars for each category.

*In this exercise and the next, you will be visualizing the weight of athletes in the 2016 summer Olympic Games again, from a dataset that has some unknown number of branches of sports in it. This will be loaded into memory as a pandas DataFrame object called summer_2016_medals, which has a column called "Sport" that tells you to which branch of sport each row corresponds. There is also a "Weight" column that tells you the weight of each athlete.

*In this exercise, we will extract the unique values of the "Sport" column
"""
# Create a variable called sports_column that holds the data from the "Sport" column of the DataFrame object.
sports_column = summer_2016_medals["Sport"]

# Use the unique method of this variable to find all the unique different sports that are present in this data, and assign these values into a new variable called sports.
sports = sports_column.unique()

# Print the sports variable to the console.
print(sports)

# Automate your visualization
"""
*One of the main strengths of Matplotlib is that it can be automated to adapt to the data that it receives as input. For example, if you receive data that has an unknown number of categories, you can still create a bar plot that has bars for each category.

*This is what you will do in this exercise. You will be visualizing data about medal winners in the 2016 summer Olympic Games again, but this time you will have a dataset that has some unknown number of branches of sports in it. This will be loaded into memory as a pandas DataFrame object called summer_2016_medals, which has a column called "Sport" that tells you to which branch of sport each row corresponds. There is also a "Weight" column that tells you the weight of each athlete.
"""
# Iterate over the values of sports setting sport as your loop variable. 
# In each iteration, extract the rows where the "Sport" column is equal to sport. 
# Add a bar to the provided ax object, labeled with the sport name, with the mean of the "Weight" column as its height, and the standard deviation as a y-axis error bar. 
# Save the figure into the file "sports_weights.png".
for sport in sports:
    sport_df = summer_2016_medals[summer_2016_medals["Sport"]== sport]
    ax.bar(sport, sport_df["Weight"].mean(), yerr=sport_df["Weight"].std())
ax.set_ylabel("Weight")
ax.set_xticklabels(sports, rotation=90)
fig.savefig("sports_weights.png")

"""
*Other kinds of visualization possible with matplotlib are available at https://matplotlib.org/stable/gallery/

*To plot animated visualizations you can check resources at https://matplotlib.org/stable/api/animation_api.html

*You can also use seaborn library for visualizations, accessed at https://seaborn.pydata.org/examples/index.html
"""