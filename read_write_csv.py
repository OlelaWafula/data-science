import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading and Writing CSVs
"""
* CSV - comma-separated values
*Designed to store tabular(DataFrame-like) data
*It is atext file where each row of data has its own line and each value is separated by a comma.
*Most database and spreadsheet programs can use csv or create them. 
"""

# CSV to DataFrame
new_dogs = pd.read_csv("new_dogs.csv")
print(new_dogs)

# DataFrame manipulation
new_dogs["bmi"] = new_dogs["weight_kg"] / (new_dogs["height_cm"] / 100) ** 2
print(new_dogs)

# create an updated csv file i.e. write csv file
new_dogs.to_csv("new_dogs_with_bmi.csv")

# EXERCISE 

# CSV to DataFrame
"""
*You work for an airline, and your manager has asked you to do a competitive analysis and see how often passengers flying on other airlines are involuntarily bumped from their flights. 
*You got a CSV file (airline_bumping.csv) from the Department of Transportation containing data on passengers that were involuntarily denied boarding in 2016 and 2017, but it doesn't have the exact numbers you want. In order to figure this out, you'll need to get the CSV into a pandas DataFrame and do some manipulation!
"""
# Read CSV as DataFrame called airline_bumping
airline_bumping = pd.read_csv("airline_bumping.csv")

# Take a look at the DataFrame
print(airline_bumping.head())

## From previous step
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())

# For each airline, select nb_bumped and total_passengers and sum
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()
print(airline_totals)

# From previous steps
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()

# Create new col, bumps_per_10k: no. of bumps per 10k passengers for each airline
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000
print(airline_totals.head())

# DataFrame to CSV
"""
*To make things easier to read, you'll need to sort the data and export it to CSV so that your colleagues can read it.
"""
# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values("bumps_per_10k", ascending=False)

# Print airline_totals_sorted
print(airline_totals_sorted)

# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv("airline_totals_sorted.csv")