import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Dictionaries - holds a set of key-value pairs
my_dict = {
    "key1": "value1", 
    "key2": "value2", 
    "key3": "value3", 
}
# dictionary on book information 
my_book ={
    "title": "Treason: The Case Against Tyrants & Renegades",
    "author": "Miguna Miguna",
    "year": 2019
}
# access dictionary values via their keys
my_book["author"]

# Creating DataFrames - From a list of dictionaries & dictionary of lists

# From a list of dictionaries
"""
*constructed row by row
"""
# #creating a list f dictionaries 
list_of_dicts = [
    {"name": "Ginger", "breed":"Dachshund", "height_cm":22, 
     "weight_kg":10, "date_of_birth": "2019-03-14"},
     {"name": "Scout", "breed":"Dalmatian", "height_cm":59, 
     "weight_kg":25, "date_of_birth": "2019-05-09"},
]
new_dogs = pd.DataFrame(list_of_dicts)
print(new_dogs)

# From a dictionary of lists
"""
*constructed column by column
"""
# #creating a dictionary of lists - Key = column name, value = list of column values
dict_of_lists = {
    "name": ["Ginger", "Scount"],
    "breed": ["Dachshund", "Dalmatian"],
    "height_cm": [22, 50],
    "weight_kg": [10, 25],
    "date_of_birth": ["2019-03-14", "2019-05-09"]
}
new_dogs = pd.DataFrame(dict_of_lists)
print(new_dogs)

# EXERCISE

# List of dictionaries
"""
*You recently got some new avocado data from 2019 that you'd like to put in a DataFrame using the list of dictionaries method. Remember that with this method, you go through the data row by row.
"""
# Create a list of dictionaries with new data
avocados_list = [
    {"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071},
    {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)

# Dictionary of lists
"""
*Some more data just came in! This time, you'll use the dictionary of lists method, parsing the data column by column.
"""
# Create a dictionary of lists with new data
avocados_dict = {
  "date": ["2019-11-17", "2019-12-01"],
  "small_sold": [10859987, 9291631],
  "large_sold": [7674135, 6238096]
}

# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)

# Print the new DataFrame
print(avocados_2019)