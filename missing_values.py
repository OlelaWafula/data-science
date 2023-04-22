import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

# MISSING VALUES 

# Load dogs csv
dogs = pd.read_csv("dogs.csv")

"""
* In a pandas DataFrame missinbg values are indicated with NaN - Not a Number. 
*It is a good practice to check if a DataFrame contains missing values
"""
# check for missing values 
print(dogs.isna().any()) # returns True of False for each column name

# counting missing values 
print(dogs.isna().sum())

# plotting missing values 
dogs.isna().sum().plot(kind="bar")
plt.show()

# Removing missing values - Rows
dogs.dropna() # not ideal for a lot of missing data

# Replacing missing values with another value
dogs.fillna(0)

# EXERCISE 

# Finding missing values
"""
*Missing values are everywhere, and you don't want them interfering with your work. Some functions ignore missing data by default, but that's not always the behavior you might want. 
*Some functions can't handle missing values at all, so these values need to be taken care of before you can use them. 
*If you don't know where your missing values are, or if they exist, you could make mistakes in your analysis. 
*In this exercise, you'll determine if there are missing values in the dataset, and if so, how many.
"""
# Load avocados_2016 csv
avocados_2016 = pd.read_csv("avocados_2016.csv")

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind="bar")

# Show plot
plt.show()

# Removing missing values
"""
*Now that you know there are some missing values in your DataFrame, you have a few options to deal with them. 
*One way is to remove them from the dataset completely. 
*In this exercise, you'll remove missing values by removing all rows that contain missing values.
"""
# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())

# Replacing missing values
"""
*Another way of handling missing values is to replace them all with the same value. For numerical variables, one option is to replace values with 0 — you'll do this here. 
*However, when you replace missing values, you make assumptions about what a missing value means. 
*In this case, you will assume that a missing number sold means that no sales for that avocado type were made that week.

*In this exercise, you'll see how replacing missing values can affect the distribution of a variable using histograms. 
*You can plot histograms for multiple variables at a time as follows:

    dogs[["height_cm", "weight_kg"]].hist()

"""
# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()

# Show the plot
plt.show()

# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()