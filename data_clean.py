import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load Data 
feb_2022 = pd.read_csv('E:/Datasets/202202.csv', index_col='ride_id',
                        parse_dates=["started_at", "ended_at"])
march_2022 = pd.read_csv('E:/Datasets/202203.csv', index_col='ride_id',
                        parse_dates=["started_at", "ended_at"])

print("\nFebruary Data: \n", feb_2022.head())
print("\nMarch Data: \n", march_2022.head())

# Fill missing station name 
feb_cleaned_start_station = feb_2022.fillna(
    {'start_station_name': 'n/a', 'start_station_id': 0, 'end_station_name': 'n/a', 'end_station_id': 0})

mar_cleaned_start_station = march_2022.fillna(
    {'start_station_name': 'n/a', 'start_station_id': 0, 'end_station_name': 'n/a', 'end_station_id': 0})

# drop rows with NaN latititudes
cleaned_feb_22 = feb_cleaned_start_station.dropna()
cleaned_mar_22 = mar_cleaned_start_station.dropna()

# Concate feb and march data
feb_march = pd.concat([cleaned_feb_22, cleaned_mar_22])

print("\nFebruary Columns: \n", cleaned_feb_22.columns)
print("\nMarch Columns: \n", cleaned_mar_22.columns)

# Add another column 
cleaned_feb_22['ride_length'] = (cleaned_feb_22['ended_at'] - cleaned_feb_22['started_at']).dt.total_seconds() / 60

print("\nFeb Data with New Column: \n", cleaned_feb_22.head())

print("\nNumber of rides where duration is between 4 and 10 Minutes:\n",
      cleaned_feb_22.groupby('rideable_type')['ride_length'].agg(np.mean))

# Query Feb data where ride length is between 4 and 10 minutes
print(cleaned_feb_22.columns)

"""
# Mission values 
print(feb_march.isna().sum())
print(feb_march.describe())

# Shape 
print("\nFeb shape: \n", cleaned_feb_22.shape)
print("\nMarch shape: \n", cleaned_mar_22.shape)
print(feb_march.shape)
"""