import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# iterators
"""
* We can iterate over a list using a for loop.
*We can also use a for loop to iterate over a string.

* We use a for loop to iterate over a sequence of numbers produced by a special range object. 

*Iterables: lists, strings, dictionaries, file connections. 
    .An iterable is an object that has an associated iter() method.
    .Applying iter() to an iterable creates an iterator. This is what the 'for loop' does.

*Iterator - an object that has an associated next() method, that produces the consective values.
"""
# iterate over a list
employees = ["Tarno", "Olela", "Juma", "Nabwire"]
for employee in employees:
    print(employee)

# iterate over a string
for letter in 'Olela Wafula':
    print(letter)

# iterate over range
for i in range(4):
    print(i)

# create iterator from iterable - we use the function iter()
word = 'Da'
it = iter(word)
next(it) # Returns the first value
next(it) # returns the consective value.

# iterating at once with *
course = 'Data'
itr = iter(course)
print(*itr) # Returns D a t a 
# the * is referred to as the splash operator.it unpacks all elements of an iterator or iterable. Once you do so you cannot do it again, since there are no more values to iterate through. 

# iterating over dictionaries
elexarites  = {'Managing Director':'Dennis Kipchumba Tarno', 'Chief Operations Director':'Olela Wafula James', 'Legal':'Dr. Duncan Munabi Okubasu', 'Accountant':'Lewis Juma Olela'}
for key, value in elexarites.items():
    print(key,": "+ value)

""" Use for loop to read multiple files and concat"""
# import glob
import glob
# create path variable for the folder containing files
path = "C:\\Users\\HP\\OneDrive\\Desktop\\Data-files"
# variable to each csv file
csv_files = glob.glob(path + "/*.csv")
# create a list of DataFrame called df_list
df_list = (pd.read_csv(file) for file in csv_files)
# concatenate the DataFrames 
combined_df = pd.concat(df_list, ignore_index=True)
    
# iterating over file connections
file = open('file.txt')
it = iter(file)
print(next(it)) # Returns: This is the firt line.
print(next(it)) # This is the second line.

# Iterating over iterables
# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for person in flash:
    print(person)


# Create an iterator for flash: superhero
superhero = iter(flash)

# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))

"""
*Recall that range() doesn't actually create the list; instead, it creates a range object with an iterator that produces the values until it reaches the limit. 

*If range() created the actual list, calling it with a value of may not work, especially since a number as big as that may go over a regular computer's memory. The value 10^100 is actually what's called a Googol which is a 1 followed by a hundred 0s. That's a huge number!
"""
# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for num in range(3):
    print(num)



# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))

# Iterators as function arguments
"""
*here are also functions that take iterators and iterables as arguments. For example, the list() and sum() functions return a list and the sum of elements, respectively.
"""
# Create a range object: values
values = range(10, 21)

# Print the range object
print(values)

# Create a list of integers: values_list
values_list = list(values)

# Print values_list
print(values_list)

# Get the sum of values: values_sum
values_sum = sum(values)

# Print values_sum
print(values_sum)

# Operations with iterators 

# enumerate() - allows addition of a counter to any iterable, while zip() - allows stitching together of an arbitrary number of iterables.

# enumerate() - takes any iterable as an argument
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
e = enumerate(avengers)
print(type(e)) # <class 'enumerate'>

# convert enumerate object to a list of tuples
e_list = list(e)
print(e_list)

# The enumerate object itself is also an iterable and we look loop over it and unpack it

# enumerate() and unpack()
stationery = ['pen', 'pencil', 'staples', 'notebooks', 'papers', 'files']
for index, value in enumerate(stationery):
    print(index, value)

# we can also specify the starting key for enumerated data. i.e. unpacked data replace o with specified start key.
for index, value in enumerate(stationery, start=10):
    print(index, value)

# zip() - accepts arbitrary number of iterables and returns an iterator of tuples
first_name = ['Olela', 'Harnic', 'Topister', 'Nabwire', 'Ajiambo']
second_name = ['Wafula', 'Ibrahim Olela', 'Akinyi', 'Akhenda', 'Namaindi']
full_name = zip(first_name, second_name)
print(type(full_name)) # <class 'zip'>
# use splash (*) operator to print all the elements
print(*full_name)

# convert zip to a list pf tuples
z_list = list(full_name)
print(z_list)

# use for loop to iterate over zip and print tuples
given_name = ['Olela', 'Harnic', 'Topister', 'Nabwire', 'Ajiambo']
last_name = ['Wafula', 'Ibrahim Olela', 'Akinyi', 'Akhenda', 'Namaindi']
for z1, z2 in zip(given_name, last_name):
    print(z1, z2)

# EXERCISE 

# Using enumerate

# Create a list of strings: mutants
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)

# Unpack and print the tuple pairs
for index1, value1 in enumerate(mutants):
    print(index1, value1)

# Change the start index
for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)

# Using zip
"""
*zip() takes any number of iterables and returns a zip object that is an iterator of tuples. If you wanted to print the values of a zip object, you can convert it into a list and then print it. Printing just a zip object will not return the values unless you unpack it first.

"""
aliases = []
powers = []
# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)

# Using * and zip to 'unzip'

# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)
