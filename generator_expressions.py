import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

# Generator expressions
"""
*A enerator is like a list comprehension except it does not store the list in memory: it does not construct the list, but is an object we can iterate over to produce elements of the list as required.
"""
# Printing values from generators
result = (num for num in range(10))
for num in result:
    print(num)

# derive a list from a generator
gen = (x **3  if x%3 == 0 else 0 for x in range(50, 60))
print("\nList from a genertor: ", list(gen))

# like any other iterator, we can pass a generator to the function next in order to iterate through its elements.
result = (num for num in range(10))
print(next(result)) # 0
print(next(result)) # 1

"""
*This is an example of something called lazy evaluation, whereby the evaluation of the expression is delayed until its value is needed. 

*This can help a great deal when working with extremely large sequences as you don't want to store the entire list in memory, which is what comprehensions would do; you want to generate elements of the sequence on the fly.
"""

# Iterate over a large number of sequence - to do so use the analogous generator object instead of a list comprehension to avoind memory deadlock.
large_num = (num for num in range(10**10000000)) 

# Generator functions
"""
* These functions that when called produce generator objects. 
* Generator functions are written with the syntax of any other user-defined function, however instead of returning values using the keyword return, they yield sequences of values using the keyword yield.
"""
# a generator function that, when called with a number n, produces a generator object that generates integers 0 though n.
def num_sequence(n):
    """
    Generate values from 0 to n.
    """
    i = 0
    while i < n:
       yield i
       i += 1

"""
We can see within the function definition that i is initialized to 0 and that the first time the generator object is called, it yields i equal to 0. It then adds one to i and will then yield one on the next iteration and so on. The while loop is true until i equals equals n and then the generator ceases to yield values.
"""
# Use a generator function
result = num_sequence(5)
print(result) # <class 'generator'>

for item in result:
    print(item)

# Create generator object: result
result = (num for num in range(31))

# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Print the rest of the values
for value in result:
    print(value)

"""
*Write a generator expression that will generate the lengths of each string in lannister. Use person as the iterator variable. Assign the result to lengths.
"""
# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(person) for person in lannister)

# Iterate over and print the values in lengths
for value in lengths:
    print(value)

# Generator function

# Create a list of strings
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)

# Print the values generated by get_lengths()
for value in get_lengths(lannister):
    print(value)

# EXERCISE 

# Load data 
df = sns.load_dataset('tweets.csv')

# List comprehensions for time-stamped data
"""
Create a list comprehension that extracts the time from each row in tweet_time. Each row is a string that represents a timestamp, and you will access the 12th to 19th characters in the string to extract the time. Use entry as the iterator variable and assign the result to tweet_clock_time
"""
# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time ]

# Print the extracted times
print(tweet_clock_time)

"""
Create a list comprehension that extracts the time from each row in tweet_time. Each row is a string that represents a timestamp, and you will access the 12th to 19th characters in the string to extract the time. Use entry as the iterator variable and assign the result to tweet_clock_time. Additionally, add a conditional expression that checks whether entry[17:19] is equal to '19'.
"""
# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)
