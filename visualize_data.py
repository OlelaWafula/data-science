import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# Load dog_pack csv
dog_pack = pd.read_csv("dog_pack.csv")

# Visualizing Data

# Hisrograms - Increasing or decreasing can reveal the distribution picture
dog_pack["height_cm"].hist()
plt.show()

# adjust number of bins 
dog_pack["height_cm"].hist(bins=20)
plt.show()

# Bar Plots - Can reveal relationships btn a categorical & numeric variables
avg_weight_by_breed = dog_pack.groupby("breed")["weight_kg"].mean()
print("\nAverage Weight by Dog Breed: \n", avg_weight_by_breed)
avg_weight_by_breed.plot(kind="bar", title="Mean Weight by Dog Breed")
plt.show()

# Line Plots = Visualizing changes in numeric variables over time

# Load sully csv containing average weight over a certain period
sully = pd.read_csv("sully.csv")
print("\nSully Weight in Kg over the year 2019: \n", sully.head())

sully.plot(x="date", y="weight_kg", kind="line", title="Sully Weight in Kg in 2019", rot=45) # rotate the labels by 45 degrees for easy reading
plt.show()

# Scatter Plots - Visualizing relationships btn 2 numeric variables 
dog_pack.plot(x="height_cm", y="weight_kg", kind="scatter", title="Dog Height(cm) v Weight(kg)")
plt.show()

# Layering Plots - plots can be layered on top of one another
dog_pack[dog_pack["sex"]=="F"]["height_cm"].hist(alpha=0.7)
dog_pack[dog_pack["sex"]=="M"]["height_cm"].hist(alpha=0.7)
plt.legend(["F", "M"])
plt.show()

# VISUALIZATION EXERCISE 

# Load avocados csv file
avocados = pd.read_csv("avocados.csv")

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(x="nb_sold", y="size", kind="bar")

# Show the plot
plt.show()

# Changes in sales over time
"""
*Line plots are designed to visualize the relationship between two numeric variables, where each data values is connected to the next one. They are especially useful for visualizing the change in a number over time since each time point is naturally connected to the next time point. 
*In this exercise, you'll visualize the change in avocado sales over three years.
"""
# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(x="nb_sold", y="date", rot=45, kind="line")

# Show the plot
plt.show()

# Avocado supply and demand
"""
*Scatter plots are ideal for visualizing relationships between numerical variables. In this exercise, you'll compare the number of avocados sold to average price and see if they're at all related. 
*If they're related, you may be able to use one number to predict the other.
"""
# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x="nb_sold", y="avg_price", kind="scatter", title="Number of avocados sold vs. average price")

# Show the plot
plt.show()

# Price of conventional vs. organic avocados
"""
*Creating multiple plots for different subsets of data allows you to compare groups. In this exercise, you'll create multiple histograms to compare the prices of conventional and organic avocados.
"""
# Histogram of conventional avg_price 
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)

# Histogram of organic avg_price
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()