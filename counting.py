import numpy as np
import pandas as pd

# Load visits csv
vet_visits = pd.read_csv("vet_visits.csv")

# Load sales csv
sales = pd.read_csv("sales.csv")

# Dropping duplicate names using name & breed columns
unique_dogs = vet_visits.drop_duplicates(subset=["name", "breed"]) 

# count the breed and and return the sorted result in desc
unique_dogs["breed"].value_counts(sort=True)

# use normalize argument to turn the result of count into proportion of the total
unique_dogs["breed"].value_counts(normalize=True)


# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store", "type"])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store", "department"])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales["is_holiday"]==True].drop_duplicates(subset="date")

# Print date col of holiday_dates
print(holiday_dates["date"])

# Counting categorical variables
"""
Counting is a great way to get an overview of your data and to spot curiosities that you might not notice otherwise. In this exercise, we count the number of each type of store and the number of each department number
"""
# Count the number of stores of each type
store_counts = store_types["type"].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types["type"].value_counts(normalize=True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts["department"].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts["department"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)