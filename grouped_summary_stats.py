import numpy as np
import pandas as pd

# Load dogs csv
dogs = pd.read_csv("dogs.csv")

# Load sales.csv
sales = pd.read_csv("sales.csv")

# Summaries by group - get the mean of each dog color
dogs.groupby("color")["weight_kg"].mean()

# Multiple grouped summaries 
dogs.groupby("color")["weight_kg"].agg([min, max, sum])

#Grouping by multiple variables/columns
dogs.groupby(["color", "breed"])["weight_kg"].mean()

#Many groups, many summaries
dogs.groupby(["color", "breed"])[["weight_kg", "height_cm"]].mean()

# EXERCISE

# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)

# Calculations with .groupby()

# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)

# From previous step
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)

# Import numpy with the alias np
import numpy as np 

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby( "type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])

unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# Print unemp_fuel_stats
print(unemp_fuel_stats)
