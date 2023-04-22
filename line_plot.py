import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Line plots
"""
*Types of relational plots in seaborn:
i. Scatter plots - used when each plot point is an independent observation. 

ii. Line plots - used when each plot point represens the same "thing", typically tracked over time. e.g. Tracking the value of company stock over time.
"""
# Load Data
air_df = sns.load_dataset("air_df")
air_df_mean = sns.load_dataset("air_df_mean")
mpg = sns.load_dataset("mpg")

# Plot 
sns.relplot(x="hour", y="NO_2_mean", data=air_df_mean, kind="line", markers=True)
plt.show()

# We can also track subgroups over time with line plots
sns.relplot(x="hour", y="NO_2_mean", data=air_df_mean, kind="line", style="location", hue="location", markers=True, dashes=False)
plt.show()

# Multiple observations per x-value
sns.relplot(x="hour", y="NO_2", data=air_df, kind="line")
"""
.Shaded region is the confidence interval.
.Assume that the dataset is a random sample:
    -Based on our sample we can be 95% confident that the average Nitrogen Dioxide(NO2) level for the whole city is within this range.

.Confidence interval indicates the uncertainity we have in our estimate. 
"""
# Replacing confidence interval with standard deviation
sns.relplot(x="hour", y="NO_2", data=air_df, kind="line", ci="sd")
plt.show()
"""
Setting the ci="None" turns off the confidence interval.
"""
# EXERCISE 

# Interpreting line plots
"""
*In this exercise, we'll continue to explore Seaborn's mpg dataset, which contains one row per car model and includes information such as the year the car was made, its fuel efficiency (measured in "miles per gallon" or "M.P.G"), and its country of origin (USA, Europe, or Japan).

*How has the average miles per gallon achieved by these cars changed over time? Let's use line plots to find out!
"""
# Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "mpg" on the y-axis.
sns.relplot(x="model_year", y="mpg", data=mpg, kind="line")
plt.show()
"""
The shaded region represents a confidence interval for the mean, not the distribution of the observations.
"""
# Visualizing standard deviation with line plots
"""
*In the last exercise, we looked at how the average miles per gallon achieved by cars has changed over time. Now let's use a line plot to visualize how the distribution of miles per gallon has changed over time.
"""
# Change the plot so the shaded area shows the standard deviation instead of the confidence interval for the mean.
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line", ci="sd")
plt.show()
"""
Unlike the plot in the last exercise, this plot shows us the distribution of miles per gallon for all the cars in each year.
"""
# Plotting subgroups in line plots
"""
*Let's continue to look at the mpg dataset. We've seen that the average miles per gallon for cars has increased over time, but how has the average horsepower for cars changed over time? And does this trend differ by country of origin?
"""
# Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "horsepower" on the y-axis. Turn off the confidence intervals on the plot.
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None)
plt.show()

# Create different lines for each country of origin ("origin") that vary in both line style and color.
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", hue="origin")
plt.show()

# Add markers for each data point to the lines. # Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin", markers=True, dashes=False)
plt.show()
"""
Now that we've added subgroups, we can see that this downward trend in horsepower was more pronounced among cars from the USA.
"""
