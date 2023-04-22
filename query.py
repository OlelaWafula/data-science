import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Selecting data with .query()
"""
.query() method 

        .query('SOME SELECTION STATEMENT')

*Accepts an input string
    .input string used to determine what rows are returned
    .input string similar to statement after WHERE clause in SQL statement
"""

# Load Data 
stocks = pd.read_csv('stocks.csv')
stocks_long = pd.read_csv('stocks_long.csv')

# query
stocks.query('nike >= 90')

# querying on a multiple conditions 'and', 'or'
stocks.query('nike >=90 and disney < 140')
stocks.query('nike > 96 or disney < 98')

# using .query() to select data
stocks_long.query('stock=="disney" or (stock == "nike" and close < 90)')

# Subsetting rows with .query()
"""
*In this exercise, you will revisit GDP and population data for Australia and Sweden from the World Bank and expand on it using the .query() method. 
*You'll merge the two tables and compute the GDP per capita. Afterwards, you'll use the .query() method to sub-select the rows and create a plot. *Recall that you will need to merge on multiple columns in the proper order.
"""
# Load Data 
gdp = pd.read_csv('gdp.csv')
pop = pd.read_csv('pop.csv')

# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Pivot data so gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

# Select dates equal to or greater than 1991-01-01
recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')

# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)
plt.show()