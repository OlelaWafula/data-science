import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Quantitative Comaprisons - Bar charts

"""# Load Data
medals = pd.read_csv('medals_by_country_2016.csv', index_col=0)

# Visualize data 
fig, ax = plt.subplots()
ax.bar(medals.index, medals['Gold'])
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel("Number of medals")
ax.bar(medals.index, medals['Silver'], bottom=medals['Gold'])
ax.bar(medals.index, medals['bronze'], 
                    bottom=medals['Gold'] + medals['Silver'])

# Add legend
ax.legend()
plt.show()
"""
# EXERCISE - TOKYO OLYPICS 2020

# Load Data for specific columns
tokyo_2020 = pd.read_csv('C:/Users/HP/Data_Science_Python/Tokyo_Medals_2021.csv', 
                         usecols=['Country','Gold Medal', 'Silver Medal', 'Bronze Medal'] , index_col=0)
#Rename column names 
tokyo_2020.rename(columns={'Gold Medal':'Gold', 'Silver Medal':'Silver',
                           'Bronze Medal':'Bronze'}, inplace=True)
print("\nTop Rows of Tokyo 2020 data: \n", tokyo_2020.head())

# Clean data

# check for Missing values values 
print("\nSummary of Missing values: \n", tokyo_2020.isna().sum())

# Summary statics of data 
print("\nTokyo Data Description:\n", tokyo_2020.describe())

# Slice the top ten of data 
tokyo_sliced = tokyo_2020.iloc[0:20, :]
print("\nSliced Tokyo Data: \n", tokyo_sliced)

print(tokyo_sliced)

# Visualize data using stacked barcharts
fig, ax = plt.subplots()
ax.bar(tokyo_sliced.index, tokyo_sliced['Gold'], label='Gold')
ax.bar(tokyo_sliced.index, tokyo_sliced['Silver'], label='Silver',
       bottom=tokyo_sliced['Gold'])
ax.bar(tokyo_sliced.index, tokyo_sliced['Bronze'],  label='Bronze',
       bottom=tokyo_sliced['Gold'] + tokyo_sliced['Silver'])
ax.set_xticklabels(tokyo_sliced.index, rotation=90)
ax.set_ylabel("Number of Medals")
ax.set_title("Tokyo Olympics 2020")
ax.legend()
plt.show()

# Bar chart
"""
*Bar charts visualize data that is organized according to categories as a series of bars, where the height of each bar represents the values of the data in this category.

*For example, in this exercise, you will visualize the number of gold medals won by each country in the provided medals DataFrame. The DataFrame contains the countries as the index, and a column called "Gold" that contains the number of gold medals won by each country, according to their rows.
"""
# Load Data 
medals = pd.read_csv('medals_2016.csv', index_col=0)
fig, ax = plt.subplots()

# Plot a bar-chart of gold medals as a function of country
ax.bar(medals.index, medals['Gold'])

# Set the x-axis tick labels to the country names
ax.set_xticklabels(medals.index, rotation=90)

# Set the y-axis label
ax.set_ylabel("Number of medals")

plt.show()

# Stacked bar chart
"""
*A stacked bar chart contains bars, where the height of each bar represents values. In addition, stacked on top of the first variable may be another variable. The additional height of this bar represents the value of this variable. And you can add more bars on top of that.

In this exercise, you will have access to a DataFrame called medals that contains an index that holds the names of different countries, and three columns: "Gold", "Silver" and "Bronze". You will also have a Figure, fig, and Axes, ax, that you can add data to.

*You will create a stacked bar chart that shows the number of gold, silver, and bronze medals won by each country, and you will add labels and create a legend that indicates which bars represent which medals.
"""
# Add bars for "Gold" with the label "Gold"
ax.bar(medals.index, medals['Gold'], label='Gold')

# Stack bars for "Silver" on top with label "Silver"
ax.bar(medals.index, medals['Silver'], bottom=medals['Gold'], label='Silver')

# Stack bars for "Bronze" on top of that with label "Bronze"
ax.bar(medals.index, medals['Bronze'], bottom=medals['Gold'] + medals['Silver'], label='Bronze')

# Display the legend
ax.legend()

plt.show()