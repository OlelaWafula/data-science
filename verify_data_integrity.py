import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Verifying Data Integrity 
"""
*When merging two tables you might expect to have 0ne-to-one or one-to-many relationships. However one of the columns we are merging on may have a duplicated value  which may alter the intended relationship. 
"""
# Merge method integrity verification
"""
# validating merge:
.merge(validate=None)

#checks if merge is of specified type otherwise an error is returned.
        *'one_to_one'
        *'one_to_many'
        *'many_to_one'
        *'many_to_many'
"""
# Load Data 
tracks = pd.read_csv('tracks.csv')
specs = pd.read_csv('specs.csv')
albums = pd.read_csv('albums.csv')

# merge validate: one_to_one
tracks.merge(specs, on='tid', validate='one_to_one') # returns an error because specs has rows with duplicate 'tid'

# Merge validate: one_to_many
albums.merge(tracks, on='aid', validate='one_to_many') # no error raised

# Verifying concatenations
"""
.concat(verify_integrity=False)

*checks whether the new concatenated index contains duplicates
*Default value is False, However if set to True it checks if duplicates exists and raises an error if they are. 
*Only checks the index values and not the columns
"""
# Load Data 
inv_mar = pd.read_csv('inv_mar.csv')
inv_feb = pd.read_csv('inv_feb.csv')
inv_jan = pd.read_csv('inv_jan.csv')

# concat() Verify
pd.concat([inv_feb, inv_mar], verify_integrity=True) # Raises an error because both tables have invoice id 'iid'=9
pd.concat([inv_feb, inv_mar], verify_integrity=False) # Returns combined table with invoice id 9 repeated twice without an error. This is not clean data. 

# EXERCISE 

# Concatenate and merge to find common songs
"""
*The senior leadership of the streaming service is requesting your help again. You are given the historical files for a popular playlist in the classical music genre in 2018 and 2019. 
*Additionally, you are given a similar set of files for the most popular pop music genre playlist on the streaming service in 2018 and 2019. 
*Your goal is to concatenate the respective files to make a large classical playlist table and overall popular music table. 
*Then filter the classical music table using a semi join to return only the most popular classical music tracks.
"""
# Load Data
classic_18 = pd.read_csv('classic_18.csv')
classic_19 = pd.read_csv('classic_19.csv')
pop_18 = pd.read_csv('pop_18.csv')
pop_19 = pd.read_csv('pop_19.csv')

# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19, on='tid', how='inner')

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# Print popular chart
print(popular_classic)