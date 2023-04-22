import numpy as np
import pandas as pd

# Slicing and subsetting with .loc and .iloc

#slicing lists
breeds = ["Labrador", "Poodle",
          "Chow Chow", "Schnauzer",
          "Labrador", "Chihuahua",
          "St. Bernard"]

print(breeds)
print("Sliced breeds[2:5]: \n", breeds[2:5])

# Load dogs csv
dogs = pd.read_csv("dogs.csv")

# sort the index before slicing
dogs_srt = dogs.set_index(["breed", "color"]).sort_index()
print(dogs_srt)

# slicing the outer index level
#The final value - Poodle- is included in the result
dogs_srt.loc["Chow Chow": "Poodle"] 

#Slicing the inner index leveles correctly
dogs_srt.loc[
    ("Labrador", "Brown"): ("Schnauzer", "Grey")
]

# slicing columns
dogs_srt.loc[:, "name":"height_cm"]

# slice twice = rows & columns at the same time
dogs_srt.loc[
    ("Labrador", "Brown"):("Schnauzer", "Grey"),
    "name":"height_cm"]

# set dob colun as index
dogs = dogs.set_index("date_of_birth").sort_index()

# slicing by dates - get dogs with dob between 2014-08-25 and 2016-09-16
dogs.loc["2014-08-25 ": "2016-09-16"]

# slice by partial dates-get dogs with dob between 2014-01-01 and 2016-12-31
dogs.loc["2014":"2016"]

# subsetting by row/column number
print(dogs.iloc[2:5, 1:4]) #rows 2 - 5 & columns 1 - 4

# Slicing index values
"""
*Slicing lets you select consecutive elements of an object using first:last syntax. DataFrames can be sliced by index values or by row/column number.
*Compared to slicing lists, there are a few things to remember:
-You can only slice an index if the index is sorted (using .sort_index()).
=To slice at the outer level, first and last can be strings.
=To slice at inner levels, first and last should be tuples.
=If you pass a single slice to .loc[], it will slice the rows.
"""
# Load temperatures_ind csv
temperatures_ind = pd.read_csv("temperatures_ind.csv")

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan": "Russia"])

# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc["Lahore": "Moscow"])

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[("Pakistan", "Lahore"): ("Russia", "Moscow")])

# Slicing in both directions
"""
*You've seen slicing DataFrames by rows and by columns, but since DataFrames are two-dimensional objects, it is often natural to slice both dimensions at once. That is, by passing two arguments to .loc[], you can subset by rows and columns in one go.
"""
# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, "date":"avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad"), "date":"avg_temp_c"])

# Slicing Tme Series
"""
*Slicing is particularly useful for time series since it's a common thing to want to filter for data within a date range. Add the date column to the index, then use .loc[] to perform the subsetting. 
*The important thing to remember is to keep your dates in ISO 8601 format, that is, "yyyy-mm-dd" for year-month-day, "yyyy-mm" for year-month, and "yyyy" for year.
"""
# Load temperatures csv
temperatures = pd.read_csv("temperatures.csv")
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08":"2011-02"])

# Subsetting by row/column number
"""
*This is done using .iloc[], and like .loc[], it can take two arguments to let you subset by rows and columns.
"""
# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22, 1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:, 2:4])

# Use slicing in both directions at once
print(temperatures.iloc[:5, 2:4])
