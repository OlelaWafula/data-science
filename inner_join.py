import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# INNER JOIN - Return rows that have matching values in both tables

"""
Table == DataFrames 
Combining different tables == Merging/Joining
"""
# Load Ward data
wards = pd.read_csv("Ward_Offices.csv")
print(wards.head())
print(wards.shape)

# Load census data
census = pd.read_csv("Ward_Census.csv")
print(census.head())
print(census.shape)

"""
*The above tables are related by the ward column. We can combine them together matching the ward number from wards table to ward number in census table.

*pandas package merge() method to accomplish this:
"""
wards_census = wards.merge(census, on="ward")
print(wards_census.head(4))
print(wards_census.shape)

"""
*Since we listed the wwards table first, its column will appear first, then followed by the census table columns.

*The merged table has colmns with suffixes of '_x' or '_y', this is because both the wards and census table contain the 'address' and 'zipped' columns. To avoid mutliple columns with the same name, they are automatically given a suffix by the merge() method.

*We can use the suffixes argument of the merge method to control this behavior i.e. all of the overllaping columns in the left table are given a suffix '_ward' while those the right table are assigned suffix '_cen'
"""
wards_census = wards.merge(census, on="ward", suffixes=('_ward', '_cen'))
print(wards_census.head())
print(wards_census.shape)

# EXERCISE 
"""
*You have been tasked with figuring out what the most popular types of fuel used in Chicago taxis are. To complete the analysis, you need to merge the taxi_owners and taxi_veh tables together on the vid column. You can then use the merged table along with the .value_counts() method to find the most common fuel_type.
"""
# Load taxi_owners and taxi_veh DataFrames
taxi_owners = pd.read_csv("taxi_owners.csv")
taxi_veh = pd.read_csv("taxi_veh.csv")

# Merge the taxi_owners and taxi_veh tables
taxi_own_veh = taxi_owners.merge(taxi_veh, on="vid")

# Print the column names of the taxi_own_veh
print(taxi_own_veh.columns)

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own', '_veh'))

# Print the column names of taxi_own_veh
print(taxi_own_veh.columns)

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())

# Inner joins and number of rows returned
"""
*It is necessary to understand that inner joins only return the rows with matching values in both tables. You will explore this further by reviewing the merge between the wards and census tables, then comparing it to merges of copies of these tables that are slightly altered, named wards_altered, and census_altered. 
*The first row of the wards column has been changed in the altered tables. You will examine how this affects the merge between them. 
"""
# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on="ward")

# Print the shape of wards_census
print('wards_census table shape:', wards_census.shape)

# Load wards_altered and census_altered DataFrames
wards_altered = pd.read_csv("wards_altered.csv")
census_altered = pd.read_csv("census_altered.csv")

# Print the first few rows of the wards_altered table to view the change 
print(wards_altered[['ward']].head())

# Merge the wards_altered and census tables on the ward column
wards_altered_census = wards_altered.merge(census, on="ward")

# Print the shape of wards_altered_census
print('wards_altered_census table shape:', wards_altered_census.shape)

# Print the first few rows of the census_altered table to view the change 
print(census_altered[['ward']].head())

# Merge the wards and census_altered tables on the ward column
wards_census_altered = wards.merge(census_altered, on="ward")

# Print the shape of wards_census_altered
print('wards_census_altered table shape:', wards_census_altered.shape)