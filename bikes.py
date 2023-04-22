import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load Data 
ride_data = pd.read_csv("ride_bikes.csv")
print(ride_data.head())

# Group by Member or Casual
print("\nGrouped by either Casual of Member: \n", ride_data.groupby(by="member_casual"))
