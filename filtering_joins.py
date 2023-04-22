import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Filtering Joins
"""
mutating joins - combines data from two or more tables based on matching observations from all the tables.i.e left, inner, right & outer joins.
filtering joins - filter observations from table based on whether or not they match an observation in another table. i.e. semi, 
"""
# semi joins - filters the left table down to observations that have emerged on the right table. Similar to inner joins, it returns intersections between the tables but only columns from the left table are returned and no duplicate rows from the left table are returned. 

# Load data 
genres = pd.read_csv('genres.csv')
top_tracks = pd.read_csv('top_tracks.csv')
print(genres.head())
print(top_tracks.head())

# semi join
genres_tracks = genres.merge(top_tracks, on='gid') # inner join
top_genres = genres[genres['gid'].isin(genres_tracks['gid'])]
print(genres_tracks.head())
print(top_genres.head())

# anti join - returns observation in the left table, excluding the intersection. Returns only columns from the left table and not the right table

# get genres not in top_tracks
# indicator=True adds another column '_merge' indicating the source of each row i.e. either 'both' or 'left_only'
genres_tracks = genres.merge(top_tracks, on='gid', how='left',
                              indicator=True)
print(genres_tracks.head())
gid_list = genres_tracks.loc[genres_tracks['_merge']=='left_only', 'gid']
print(gid_list.head())
non_top_genres = genres[genres['gid'].isin(gid_list)]
print(non_top_genres.head()) 

# EXERCISE 

# steps of a semi join
"""
1. Merge the left and right tables on key columns using an inner join.
2. Search if the key column in the left table is in the merged tables using the .isin() method creating a Bolean Series.
3. Subset the rows of the left table.
"""

# Performing an anti join
"""
*In our music streaming company dataset, each customer is assigned an employee representative to assist them. In this exercise, filter the employee table by a table of top customers, returning only those employees who are not assigned to a customer. 

*The results should resemble the results of an anti join. The company's leadership will assign these employees additional training so that they can work with high valued customers.
"""

# Load data
top_cust = pd.read_csv('top_cust.csv')
employees = pd.read_csv('employees.csv')

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', 
                                 how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])

# Performing a semi join
"""
*Some of the tracks that have generated the most significant amount of revenue are from TV-shows or are other non-musical audio. 

*You have been given a table of invoices that include top revenue-generating items. Additionally, you have a table of non-musical tracks from the streaming service. 

*In this exercise, you'll use a semi join to find the top revenue-generating non-musical tracks.
"""
# Load data
non_mus_tcks = pd.read_csv('non_mus_tcks.csv')
top_invoices = pd.read_csv('top_invoices.csv')
genres = pd.read_csv('genres.csv')

# Merge the non_mus_tck and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid', how='inner')
print(tracks_invoices.head())

# Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres, on='gid'))
