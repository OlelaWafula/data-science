import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# List comprehensions
"""
*Syntax - within the [ ] write the values you wish to create also known as the output expression, followed by the 'for clause' referring to the original list.

*List comprehensions collapse for loops for building lists into a single line. The required components are:
    . Iterable 
    . Iterator variable (represent members of the iterable)
    . Output expression.
"""
nums = list(np.arange(10, 20, 2))
new_nums = [num + 1 for num in nums]
print(new_nums)

# List comprehension using range() object
result = [num for num in range(10, 20)]
print(result)

# Use of list comprehensions in nested for loops
pairs_1 = []
for num1 in range(0, 2):
    for num2 in range(6, 8):
        pairs_1.append((num1, num2))
print(pairs_1)

# compress above code using list comprehension
pairs_2 = [(num1, num2) for num1 in range(0,2) for num2 in range(6, 8)]
print(pairs_2)
"""
*The tradeoff in the use of list comprehension is the readability of the code.
"""
# EXERCISE 

# Write a list comprehension that produces a list of the squares of the numbers ranging from 0 to 90.
squares = [x ** 2 for x in range(0, 10)]
print("\nSquares: ", squares)

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]

# Print the matrix
print("\nMatrix: \n")
for row in matrix:
    print(row)

# Advanced List Comprehensions

# Conditions in comprehensions
"""
*In this example, the resulting list is the square of the values in range(10) under the condition that the value itself is even.
"""
even_squares = [num ** 2 for num in range(10) if num % 2 == 0]
print("\nSquare of even numbers: ", even_squares)

# conditionalities on the output - if the number is odd return 0
squared = [num ** 2 if num % 2 == 0 else 0 for num in range(10)]
print("\nSquared even and 0 for odd numbers: \n", squared)

# Dictionary comprehensions
"""
* Create new dictionaries from iterables.
* The sysntax is almost similar to list comprehension only that we use curly braces {} instead of [] and the key and value are separated by a colon in the output expression.
"""
pos_neg = { num: -num for num in range(10)}
print("\nA dictionary of negative and positive integers: \n", pos_neg)

# Use member as the iterator variable in the list comprehension. For the conditional, use len() to evaluate the iterator variable. Note that you only want strings with 7 characters or more.

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]

# Print the new list
print(new_fellowship)

# In the output expression, keep the string as-is if the number of characters is >= 7, else replace it with an empty string - that is, '' or "".
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member)>= 7 else '' for member in fellowship]

# Print the new list
print(new_fellowship)

"""
You are given a list of strings fellowship and, using a dict comprehension, create a dictionary with the members of the list as the keys and the length of each string as the corresponding values.
"""
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}

# Print the new dictionary
print(new_fellowship)
