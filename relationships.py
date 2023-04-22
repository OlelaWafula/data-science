import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# One-to-many relationships
"""
1:1 - Every row in the left table is related to only one row in the 
right table.
"""

# EXERCISE 

# One-to-many merge
"""
*A business may have one or multiple owners. In this exercise, you will 
continue to gain experience with one-to-many merges by merging a 
table of business owners, called biz_owners, to the licenses table. 

*Recall from the video lesson, with a one-to-many relationship, a row in 
the left table may be repeated if it is related to multiple rows in the 
right table. 

*In this lesson, you will explore this further by finding out what 
is the most common business owner title. (i.e., secretary, CEO, or vice 
president)
"""
# Load DataFrames licenses and biz_owners 
licenses = pd.read_csv("lincenses.csv")
biz_owners = pd.read_csv("biz_owners.csv")

# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on="account")

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby("title").agg({'account':'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values(by="account", ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())

# Merging Mutilple DataFrames
"""
*we use python's backslash (\) line continuation method to to add the
second merge.
"""
# Load DataFrames 
wards = pd.read_csv("wards.csv")
grants = pd.read_csv("small_business_grants.csv")

# Mutliple Merge 
grants_licenses_wards = grants.merge(licenses, on=['addres','zipp'])\
                              .merge(wards, on='ward', 
                                     suffixes=('_bus','_ward'))
print(grants_licenses_wards.head())

# plot
grants_licenses_wards.groupby('ward').agg('sum').plot(kind='bar', 
                                                      y='grant')
# Merging Four tables 
"""
df1.merge(df2, on='col')\
   .merge(df3, on='col')\
   .merge(df4, on='col')
"""

# EXERCISE 

# Total riders in a month
"""
*our goal is to find the total number of rides provided to passengers 
passing through the Wilson station (station_name == 'Wilson') when riding 
Chicago's public transportation system on weekdays (day_type == 'Weekday')
 in July (month == 7). 
*Luckily, Chicago provides this detailed data, but  it is in three 
different tables. You will work on merging these tables  together to 
answer the question. This data is different from the business  related
data you have seen so far, but all the information you need to  answer 
the question is provided.
"""
# Load DataFrames 
ridership = pd.read_csv('ridership.csv')
cal = pd.read_csv('cal.csv')
stations = pd.read_csv('stations.csv')

# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
							.merge(stations, on='station_id')

# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7) 
                   & (ridership_cal_stations['day_type'] == 'Weekday') 
                   & (ridership_cal_stations['station_name'] == 'Wilson'))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())

# Three table merge
"""
*To solidify the concept of a three DataFrame merge, practice another 
exercise. A reasonable extension of our review of Chicago business data 
would include looking at demographics information about the neighborhoods
where the businesses are. 
*A table with the median income by zip code has been provided to you. You 
will merge the licenses and wards tables with this new income-by-zip-code 
table called zip_demo.
"""

# Load DataFrames 
zip_demo = pd.read_csv('zip_demo.csv')

# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo, on='zip') \
            			    .merge(wards, on='ward')

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))

# One-to-many merge with multiple tables
"""
*In this exercise, assume that you are looking to start a business in 
the city of Chicago. 
*Your perfect idea is to start a company that uses goats to mow the 
lawn for other businesses. However, you have to choose a location in 
the city to put your goat farm. You need a location with a great deal 
of space and relatively few businesses and people around to avoid 
complaints about the smell. 
*You will need to merge three tables to help you choose your location. 
The land_use table has info on the percentage of vacant land by city 
ward. The census table has population by ward, and the licenses table
lists businesses by ward.
"""
# Load data
land_use = pd.read_csv('land_use.csv')
census = pd.read_csv('census.csv')

# Merge land_use and census and merge result with licenses including 
# suffixes
land_cen_lic = land_use.merge(census, on='ward') \
                    .merge(licenses, on='ward', 
                           suffixes=('_cen','_lic'))

# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward','pop_2010','vacant'], 
                                   as_index=False).agg({'account':'count'})

# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(['vacant','account',
                                              'pop_2010'], 
                                             ascending=[False, True, True])

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())