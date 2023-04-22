import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Using merge_ordered()
"""
# Method comparison 

.merge()                            .merge_ordered()
-columns to join on are:            -columns to join on are:
    on, left_on, right_on               on, left_on, right_on

-Type of join                       -Type of join
    how(left, inner, right, outer)      how(left, inner, right, outer)
    default: inner                      default: outer

-overlapping column names           -overlapping column names
    suffixes                            suffixes

-calling the method                 -calling the method
    df1.merge(df2)                      pd.merge_ordered(df1, df2)
"""
# Load Data 
appl = pd.read_csv('apple.csv')
mcd = pd.read_csv('mcdonalds.csv')

# Merging stock data
# ffill - forward fill
pd.merge_ordered(appl, mcd, on='date', 
                 suffixes=('_aapl', '_mcd'), fill_method='ffill')

# When to use merge_ordered()
"""
*when working with ordered or time series data
*Filling in missing values 
"""

# EXERCISE 

# Correlation between GDP and S&P500
"""
*In this exercise, you want to analyze stock returns from the S&P 500. You believe there may be a relationship between the returns of the S&P 500 and the GDP of the US. Merge the different datasets together to compute the correlation.
"""
# Load Data
sp500 = pd.read_csv('sp500.csv')
gdp = pd.read_csv('us_gdp.csv')

# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left')

# Print gdp_sp500
print(gdp_sp500)

"""
Use merge_ordered(), again similar to before, to merge gdp and sp500 use the function's ability to interpolate missing data to forward fill the missing value for returns, assigning this table to the variable gdp_sp500.
"""
# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left',  fill_method='ffill')

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['gdp', 'returns']]

# Print gdp_returns correlation
print (gdp_returns.corr())

# Phillips curve using merge_ordered()
"""
*There is an economic theory developed by A. W. Phillips which states that inflation and unemployment have an inverse relationship. The theory claims that with economic growth comes inflation, which in turn should lead to more jobs and less unemployment.

*You will take two tables of data from the U.S. Bureau of Labor Statistics, containing unemployment and inflation data over different periods, and create a Phillips curve. The tables have different frequencies. One table has a data entry every six months, while the other has a data entry every month. You will need to use the entries where you have data within both tables.
"""
# Load Data 
unemployment = pd.read_csv('unemployment.csv')
inflation = pd.read_csv('inflation.csv')

# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(inflation, unemployment, how='inner', on='date')

# Print inflation_unemploy 
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(kind='scatter', x='unemployment_rate', y='cpi')
plt.show()

# merge_ordered() caution, multiple columns
"""
*When using merge_ordered() to merge on multiple columns, the order is important when you combine it with the forward fill feature. The function sorts the merge on columns in the order provided. 
*In this exercise, we will merge GDP and population data from the World Bank for the Australia and Sweden, reversing the order of the merge on columns. 
*The frequency of the series are different, the GDP values are quarterly, and the population is yearly. Use the forward fill feature to fill in the missing data. Depending on the order provided, the fill forward will use unintended data to fill in the missing values.
"""
# Load Data 
gdp = pd.read_csv('gdp.csv')
pop = pd.read_csv('pop.csv')

# Merge gdp and pop on date and country with fill and notice rows 2 and 3
ctry_date = pd.merge_ordered(gdp,pop, on=('date', 'country'), 
                             fill_method='ffill')

# Print ctry_date
print(ctry_date)

"""
Perform the same merge of gdp and pop, but join on country and date (reverse of step 1) with the fill feature, saving this as date_ctry.
"""
# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp, pop, on=('country', 'date'), fill_method='ffill')

# Print date_ctry
print(date_ctry)