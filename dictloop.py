import numpy as np
import pandas as pd

world = {
    "afghanistan": 30.55,
    "albania": 2.77,
    "algeria": 39.21
}

for key, value in world.items():
    print(key + " -- " + str(value))
    

#2D Numpy array print each element
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.6, 68.7])
meas = np.array([np_height, np_weight])
for val in np.nditer(meas):
    print(val)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for country, capital in europe.items():
    print("the capital of " +country+ " is " +capital)

#iterrows
brics = pd.read_csv("brics.csv", index_col=0)
for lab, row in brics.iterrows():
    #create series on every iteration
    brics.loc[lab, "name_length"] = len(row["country"])
print(brics)

#apply - used for DataFrame column
brics["name_length"] = brics["country"].apply(len)
print(brics)

#Use .apply(str.upper)
cars = pd.read_csv('cars.csv', index_col = 0)
for lab, row in cars.iterrows() :
    cars["COUNTRY"] = cars["country"].apply(str.upper)