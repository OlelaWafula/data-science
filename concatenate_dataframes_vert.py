import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# Concatenate DataFrames Vertically
"""
*pandas .concat() method can concatenate both vertical and horizontal .
"""
# Load data
inv_jan = pd.read_csv('inv_jan.csv')
inv_feb = pd.read_csv('inv_feb.csv')
inv_mar = pd.read_csv('inv_mar.csv')

# Concatenate
jan_feb_mar = pd.concat([inv_jan, inv_feb, inv_mar], axis=0,
                        ignore_index=True) # vertically
print(jan_feb_mar.head())

# setting labels to original tables 
jan_feb_mar = pd.concat([inv_jan, inv_feb, inv_mar], ignore_index=False, 
                        keys=['jan', 'feb', 'mar']) # key names for each table
print(jan_feb_mar.head())

# Concatenate tables with different column names
jan_feb = pd.concat([inv_jan, inv_feb], sort=True) # inv_feb has a new column named bill_ctry. The resulting table has this column but for jan data it is NaN while feb has values filled under this column.
jan_feb = pd.concat([inv_jan, inv_feb], join='inner') # get only matching columns between jan and feb tables. 

# EXERCISE 

# Concatenation basics
"""
*You have been given a few tables of data with musical track info for different albums from the metal band, Metallica. 

*The track info comes from their Ride The Lightning, Master Of Puppets, and St. Anger albums. Try various features of the .concat() method by concatenating the tables vertically together in different ways.
"""
# Load Data
tracks_master = pd.read_csv('tracks_master.csv', index_col=['tid'])
tracks_ride = pd.read_clipboard('tracks_ride.csv', index_col=['tid'])
tracks_st = pd.read_csv('tracks_st.csv', index_col=['tid'])

# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               sort=True)
print(tracks_from_albums)

# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               ignore_index=True,
                               sort=True)
print(tracks_from_albums)

# Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               join='inner',
                               sort=True)
print(tracks_from_albums)

# Concatenating with keys
"""
*The leadership of the music streaming company has come to you and asked you for assistance in analyzing sales for a recent business quarter. 

*They would like to know which month in the quarter saw the highest average invoice total. You have been given three tables with invoice data named inv_jul, inv_aug, and inv_sep. 

*Concatenate these tables into one to create a graph of the average monthly invoice total.
"""
# Load Data 
inv_jul = pd.read_csv('inv_jul.csv')
inv_aug = pd.read_csv('inv_aug.csv')
inv_sep = pd.read_csv('inv_sep.csv')

# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep], 
                            keys=['7Jul', '8Aug', '9Sep'])

# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind='bar')
plt.show()


