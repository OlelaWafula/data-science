import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Using merge_asof()
"""
*merge_asof() is similar to merge_ordered() lef join
    -Has similar features as merge_ordered
*Matches on the nearest key column and not exact matches 
    -Merged "on" columns must be sorted
"""
# Load Data 
visa = pd.read_csv('visa.csv')
ibm = pd.read_csv('ibm.csv')

# Using merge_asof()
pd.merge_asof(visa, ibm, on='date_time', suffixes=('_visa', '_ibm'))

# merge_asof() with direction
pd.merge_asof(visa, ibm, on='date_time', suffixes=('_visa', '_ibm'), direction='forward')

# When to use merge_asof()
"""
*Data sampled from a process
*Developing a training set (no data leakage)
"""

# Using merge_asof() to study stocks
"""
*You have a feed of stock market prices that you record. You attempt to track the price every five minutes. 
*Still, due to some network latency, the prices you record are roughly every 5 minutes. You pull your price logs for three banks, JP Morgan (JPM), Wells Fargo (WFC), and Bank Of America (BAC). 
*You want to know how the price change of the two other banks compare to JP Morgan. Therefore, you will need to merge these three logs into one table. Afterward, you will use the pandas .diff() method to compute the price change over time. 
*Finally, plot the price changes so you can review your analysis.
"""
# Load Data 
jpm = pd.read_csv('jpm.csv')
wells = pd.read_csv('wells.csv')
bac = pd.read_csv('bac.csv')

# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(jpm, wells, on='date_time', direction='nearest', suffixes=('', '_wells'))

# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on='date_time', direction='nearest', suffixes=('_jpm', '_bac'))
# Compute price diff
price_diffs = jpm_wells_bac.diff()

# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm','close_wells', 'close_bac'])
plt.show()

# Using merge_asof() to create dataset
"""
*The merge_asof() function can be used to create datasets where you have a table of start and stop dates, and you want to use them to create a flag in another table. 
*You have been given gdp, which is a table of quarterly GDP values of the US during the 1980s. 
*Additionally, the table recession has been given to you. It holds the starting date of every US recession since 1980, and the date when the recession was declared to be over. 
*Use merge_asof() to merge the tables and create a status flag if a quarter was during a recession. 
*Finally, to check your work, plot the data in a bar chart.
"""
# Load Data
gdp = pd.read_csv('gdp.csv')
recession = pd.read_csv('recession.csv')

# Merge gdp and recession on date using merge_asof()
gdp_recession = pd.merge_asof(gdp, recession, on='date')

# Create a list based on the row value of gdp_recession['econ_status']
is_recession = ['r' if s=='recession' else 'g' for s in gdp_recession['econ_status']]

# Plot a bar chart of gdp_recession
gdp_recession.plot(kind='bar', y='gdp', x='date', color=is_recession, rot=90)
plt.show()
