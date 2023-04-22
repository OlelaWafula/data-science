import numpy as np
import pandas as pd

# Working with pivot tables 

# Load dog_pack csv 
dog_pack = pd.read_csv("dog_pack.csv")

# Pivoting the dog pack 
# uses default aggregation function i.e. mean
dogs_height_by_breed_vs_color = dog_pack.pivot_table(values="height_cm", index="breed", columns="color")
print(dogs_height_by_breed_vs_color)

# .loc[] + slicing is a power combo
dogs_height_by_breed_vs_color.loc["Chow Chow": "Poodle"]

# The axis argument
dogs_height_by_breed_vs_color.mean(axis="index") # calculate row mean

# Calculating summary stats across columns
dogs_height_by_breed_vs_color.mean(axis="columns")

# EXERCISE 

# Pivot temperature by city and year
"""
*It's interesting to see how temperatures for each city change over time—looking at every month results in a big table, which can be tricky to reason about. Instead, let's look at how temperatures change by year.

*You can access the components of a date (year, month and day) using code of the form dataframe["column"].dt.component. For example, the month component is dataframe["column"].dt.month, and the year component is dataframe["column"].dt.year.

*Once you have the year column, you can create a pivot table with the data aggregated by city and year.
"""
# Load temperatures csv 
temperatures = pd.read_csv("temperatures.csv")

# Add a year column to temperatures
temperatures["year"] = temperatures["date"].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(values="avg_temp_c", index=["country", "city"], columns="year")

# See the result
print(temp_by_country_city_vs_year)

# Subsetting pivot tables
"""
*A pivot table is just a DataFrame with sorted indexes, so the technique  the .loc[] + slicing combination is often helpful.
"""
# Subset for Egypt to India
print(temp_by_country_city_vs_year.loc["Egypt": "India"])

# Subset for Egypt, Cairo to India, Delhi
print(temp_by_country_city_vs_year.loc[("Egypt", "Cairo"): ("India", "Delhi")])

# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
print(temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi"), "2005":"2010"])

# Calculating on a pivot table
"""
*Pivot tables are filled with summary statistics, but they are only a first step to finding something insightful. Often you'll need to perform further calculations on them. A common thing to do is to find the rows or columns where the highest or lowest value occurs.
"""
# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])
