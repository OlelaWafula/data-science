import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data 
mens_rowing = pd.read_csv('mens_rowing.csv', index_col=0)
mens_gymnastics = pd.read_csv('mens_gymnastics.csv', index_col=0)

# HISTOGRAMS - Shows distribution of values within each variable
fig, ax = plt.subplots()

#Histogram to compare heights
ax.hist(mens_rowing["Height"], label="Rowing", bins=5, alpha=0.5)
ax.hist(mens_gymnastics["Height"], label="Gymnastics", bins=5, alpha=0.5)
ax.set_xlabel("Height (cm)")
ax.set_ylabel("# of observations")
ax.legend()
plt.show()

# instead of using alpha we can specify the type of histogram
"""
ax.hist(mens_rowing["Height"], label="Rowing", bins=5, histtype="step")
ax.hist(mens_gymnastics["Height"], label="Gymnastics", bins=5, histtype="step")
"""
# EXERCISE 

# Creating histograms
"""
*Histograms show the full distribution of a variable. In this exercise, we will display the distribution of weights of medalists in gymnastics and in rowing in the 2016 Olympic games for a comparison between them.

*You will have two DataFrames to use. The first is called mens_rowing and includes information about the medalists in the men's rowing events. The other is called mens_gymnastics and includes information about medalists in all of the Gymnastics events.
"""
fig, ax = plt.subplots()
# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing['Weight'], label="Rowing")

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics['Weight'], label="Gymnastics")

# Set the x-axis label to "Weight (kg)"
ax.set_xlabel("Weight (kg)")

# Set the y-axis label to "# of observations"
ax.set_ylabel("# of observations")

plt.show()

# "Step" histogram
"""
*Histograms allow us to see the distributions of the data in different groups in our data. In this exercise, you will select groups from the Summer 2016 Olympic Games medalist dataset to compare the height of medalist athletes in two different sports.

*The data is stored in a pandas DataFrame object called summer_2016_medals that has a column "Height". In addition, you are provided a pandas GroupBy object that has been grouped by the sport.

*In this exercise, you will visualize and label the histograms of two sports: "Gymnastics" and "Rowing" and see the marked difference between medalists in these two sports.
"""
fig, ax = plt.subplots()

# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing['Weight'], label="Rowing", histtype="step", bins=5)
# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics['Weight'], label="Gymnastics", histtype="step", bins=5)

ax.set_xlabel("Weight (kg)")
ax.set_ylabel("# of observations")

# Add the legend and show the Figure
ax.legend()
plt.show()