import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import glob

# Read multiple csv files from a folder 
path = "C:/Users/HP/OneDrive/Desktop/Datasets"
csv_files = glob.glob(path + "/*.csv")

# Read each file into DataFrame - This creates a list of DataFrames

df_list = (pd.read_csv(file, parse_dates=["started_at", "ended_at"], dtype={'ride_id':str, 'rideable_type':str, 'start_station_name':str, 'start_station_id':str, 'end_station_name':str, 'end_station_id':str, 'start_lat':np.float64, 'start_lng':np.float64, 'end_lat':np.float64, 'end_lng':np.float64, 'member_casual':str}) for file in csv_files)

# Concat all DatFrames 
bike_data = pd.concat(df_list, ignore_index=True)

"""# View Top Rows
print("\nTop 10 rows: \n", bike_data.head(10))

# Check for missing values 
print("\nMissing Values: \n", bike_data.isnull().sum())
"""
# Save DataFrame to one file 
bike_data.to_csv("ride_bikes.csv", index=False)
