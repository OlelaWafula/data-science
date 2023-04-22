import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reshaping data with .melt()
"""
*Unpivots a table from wide to long format - data friendly format. 
"""
# Load Data 
social_fin = pd.read_csv('social_fin.csv')

# melt the year columns
# id_vars = ['financial', 'company'] refers to columns in the original dataset that we do not intend to change/unpivot
social_fin_tall = social_fin.melt(id_vars=['financial', 'company'])
print(social_fin_tall.head(10))

# controlling which columns are unpivoted
social_fin_tall = social_fin.melt(id_vars=['financial', 'company'], value_vars=['2018', '2017'])
print(social_fin_tall.head(9))

# Melting with column names 
social_fin_tall = social_fin.melt(id_vars=['financial', 'company'],
                                 value_vars=['2018', '2017'], var_name='year', value_name='dollars')
print(social_fin_tall.head(10))

# Using .melt() to reshape government data
"""
*The US Bureau of Labor Statistics (BLS) often provides data series in an easy-to-read format - it has a separate column for each month, and each year is a different row. 
*Unfortunately, this wide format makes it difficult to plot this information over time. 
*In this exercise, you will reshape a table of US unemployment rate data from the BLS into a form you can plot using .melt(). You will need to add a date column to the table and sort by it to plot the data correctly.
"""
# Load Data 
ur_wide = pd.read_csv('unemployment.csv')

"""
*Use .melt() to unpivot all of the columns of ur_wide except year and ensure that the columns with the months and values are named month and unempl_rate, respectively. Save the result as ur_tall.
*Add a column to ur_tall named date which combines the year and month columns as year-month format into a larger string, and converts it to a date data type.
*Sort ur_tall by date and save as ur_sorted.
*Using ur_sorted, plot unempl_rate on the y-axis and date on the x-axis.
"""
# unpivot everything besides the year column
ur_tall = ur_wide.melt(id_vars='year', var_name='month', value_name='unempl_rate')

# Create a date column using the month and year columns of ur_tall
ur_tall['date'] = pd.to_datetime(ur_tall['year'] + '-' + ur_tall['month'])

# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values(by='date', ascending=True)

# Plot the unempl_rate by date
ur_sorted.plot(x='date', y='unempl_rate')
plt.show()

# Using .melt() for stocks vs bond performance
"""
*It is widespread knowledge that the price of bonds is inversely related to the price of stocks. 
*In this last exercise, you'll review many of the topics in this chapter to confirm this. 
*You have been given a table of percent change of the US 10-year treasury bond price. It is in a wide format where there is a separate column for each year. You will need to use the .melt() method to reshape this table.

*Additionally, you will use the .query() method to filter out unneeded data. You will merge this table with a table of the percent change of the Dow Jones Industrial stock index price. 
*Finally, you will plot data.
"""
# Load Data 
ten_yr = pd.read_csv('ten_yr.csv')
dji = pd.read_csv('dji.csv')

# Use melt on ten_yr, unpivot everything besides the metric column
bond_perc = ten_yr.melt(id_vars='metric', var_name='date', value_name='close')

# Use query on bond_perc to select only the rows where metric=close
bond_perc_close = bond_perc.query("metric == 'close'")

# Merge (ordered) dji and bond_perc_close on date with an inner join
dow_bond = pd.merge_ordered(dji, bond_perc_close, on='date', how='inner', suffixes=('_dow', '_bond'))

# Plot only the close_dow and close_bond columns
dow_bond.plot(y=['close_dow', 'close_bond'], x='date', rot=90)
plt.show()