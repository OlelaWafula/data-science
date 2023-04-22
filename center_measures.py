import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics 

# Measures of Center
"""
    Mean
    Media 
    Mode
"""
# Load mammal sleep data
msleep = pd.read_csv('msleep.csv')

# get the mean
print(np.mean(msleep['sleep_total']))

# median

# sort the data and get the middle one
msleep['sleep_total'].sort_values().iloc[41]

np.median(msleep['sleep_total'])

# mode - the most frequent value in the dataset - used for categorical variables 
statistics.mode(msleep['vore'])

# Skewness 
"""
*Left-skewed data - data piled up on the right with the tail on the left.
*Right-skewed data - data piled up on the left with the tail on the right.

* When data is skewed, the mean and median are different, mean is pulled in the direction of the skew. i.e. mean is higher than the median on the right-skewed data and viceversa.
*Because mean is pulled by skewness it is better to use the median because it is less affected by the outliers. 
"""
# Mean and median
"""
*In this chapter, you'll be working with the 2018 Food Carbon Footprint Index from nu3. 
*The food_consumption dataset contains information about the kilograms of food consumed per person per year in each country in each food category (consumption) as well as information about the carbon footprint of that food category (co2_emissions) measured in kilograms of carbon dioxide, or CO2, per person per year in each country.
*In this exercise, you'll compute measures of center to compare food consumption in the US and Belgium using your pandas and numpy skills.
"""
# Load Data 
food_consumption = pd.read_csv('food_consumption.csv')

# Filter for Belgium
be_consumption = food_consumption.query('country == "Belgium"')

# Filter for USA
usa_consumption = food_consumption.query('country =="USA"')

# Calculate mean and median consumption in Belgium
print(np.mean(be_consumption['consumption']))
print(np.median(be_consumption['consumption']))

# Calculate mean and median consumption in USA
print(np.mean(usa_consumption['consumption']))
print(np.median(usa_consumption['consumption']))

# Subset for Belgium and USA only
be_and_usa = food_consumption[(food_consumption['country'] == 'Belgium') | (food_consumption['country']=='USA')]

# Group by country, select consumption column, and compute mean and median
print(be_and_usa.groupby('country')['consumption'].agg([np.mean, 
                                                        np.median]))

# Mean vs. median
"""
*In the video, you learned that the mean is the sum of all the data points divided by the total number of data points, and the median is the middle value of the dataset where 50% of the data is less than the median, and 50% of the data is greater than the median. In this exercise, you'll compare these two measures of center.
"""
# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category']=='rice']

# Histogram of co2_emission for rice and show plot
rice_consumption['co2_emission'].hist()
plt.show()

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Calculate mean and median of co2_emission with .agg()
print(rice_consumption['co2_emission'].agg([np.mean, np.median]))
