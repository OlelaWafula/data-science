import numpy as np
import pandas as pd 

# Pivot Tables
"""
Pivot Tables can be used to calculate grouped summary statistics
"""

# Load dogs csv
dogs = pd.read_csv("dogs.csv")

# Load sales csv
sales = pd.read_csv("sales.csv")

#calculate summary stats using pivot tables
#values - column to be summarized, index - column to group by. By default pivot table takes the mean value for each group.
dogs.pivot_table(values="weight_kg", index="color") 

#to get a differnt summary statistiv=c we use the aggfunc argument and pass it a function
dogs.pivot_table(values="weight_kg", index="color", aggfunc=np.median)
dogs.pivot_table(values="weight_kg", index="color", aggfunc=[np.min, np.max, np.mean, np.median])

# Pivot on two variables
#to do this we pass the second variable to columns arguments. But the result has NaN where the group is not applicable 
dogs.pivot_table(values="weight_kg", index="color", columns="breed")

#The missing values in pivot table can be filled using fill_value argument and margins=True to get mean of values excluding 0
dogs.pivot_table(values="weight_kg", index="color", columns="breed", fill_value=0, margins=True)

# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")

# Print mean_sales_by_type
print(mean_sales_by_type)

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=[np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)

# Fill in missing values and sum values with pivot tables
"""
The .pivot_table() method has several useful arguments, including fill_value and margins.

    *fill_value replaces missing values with a real value (known as imputation). What to replace missing values with is a topic big enough to have its own course (Dealing with Missing Data in Python), but the simplest thing to do is to substitute a dummy value.
    
    *margins is a shortcut for when you pivoted by two variables, but also wanted to pivot by each of those variables separately: it gives the row and column totals of the pivot table contents.
"""

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols. 
print(sales.pivot_table(values="weekly_sales", index="department", columns="type",fill_value=0, margins=True))

"""
*Note the subtlety in the value of margins here. The column 'All' returns an overall mean for each department, not (A+B)/2. (A+B)/2 would be a mean of means, rather than an overall mean per department!
"""

# Explicit indexes

"""
*You can move a column from the body of the DataFrame to index i.e. setting an index. 
"""

dogs_ind = dogs.set_index("name")
print(dogs_ind) # This makes the name column to be the index 

# To undo the above i.e. removing an index:
dogs_ind.reset_index()

# Dropping an index
dogs_ind.reset_index(drop=True) # entirely removes the name index from the df

# Indexes make subsetting simpler
dogs[dogs["name"].isin(["Bella", "Stella"])]

# when the names are in index it becomes easier to subset i.e.
dogs_ind.loc[["Bella", "Stella"]]

# Index values don't need to be unique
dogs_ind2 = dogs.set_index("breed") # There are 2 "Labrador" in the index
print(dogs_ind2)

# if you subset on "Labrador" using loc all the "Labrador"s are returned
dogs_ind2.loc["Labrador"]

# Multi-level indexes a.k.a hierarchical indexes 
# parse a list of columns to use as index
dogs_ind3 = dogs.set_index(["breed", "color"]) 
print(dogs_ind3)

# Subset the outer level with a list
#the result contains all from both groups
dogs_ind3.loc[["Labrador", "Chihuahua"]] 

# Subset inner levels with a list of tuples
# The resulting rows has to match all conditions from the two tuple items i.e. Black Labrador is ecluded from result because Brown condition wasn't matched
dogs_ind3.loc[[("Labrador", "Brown"), ("Chihuahua", "Tan")]]

# Sorting by index values
dogs_ind3.sort_index()

# Controlling sort_index - using level and ascending attributes
dogs_ind3.sort_index(level=["color", "breed"], ascending=[True, False])


# EXERCISE

# Load temparatures csv
temperatures = pd.read_csv("temperatures.csv")

# Look at temperatures
print(temperatures)

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind)

# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True))

# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])

# Setting multi-level indexes
"""
*Indexes can also be made out of multiple columns, forming a multi-level index (sometimes called a hierarchical index). There is a trade-off to using these.
*The benefit is that multi-level indexes make it more natural to reason about nested categorical variables. For example, in a clinical trial, you might have control and treatment groups. Then each test subject belongs to one or another group, and we can say that a test subject is nested inside the treatment group. Similarly, in the temperature dataset, the city is located in the country, so we can say a city is nested inside the country.
*The main downside is that the code for manipulating indexes is different from the code for manipulating columns, so you have to learn two syntaxes and keep track of how your data is represented.
"""

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country", "city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])

# Sorting by index values
"""
*Previously, you changed the order of the rows in a DataFrame by calling .sort_values(). It's also useful to be able to sort by elements in the index. For this, you need to use .sort_index().
"""
# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level="city"))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=["country", "city"], ascending=[True, False]))