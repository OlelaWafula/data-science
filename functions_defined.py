import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# User defined functions 
"""
i. Define functions without parameters
ii. Define functions with one parameter
iii. Define functions that return a value
iv. Multiple arguments and multiple values
"""
#Python built-in functions
"""
*str() - Accepts objects such as a number and returns a string object.
*While built-in functions are cool, as data scientist you will need functions that have functionalities that are specific to your needs.
"""
# Defining a function - a function that squares a number 

def square():               # function header
    new_value = 4 ** 2      # function body
    print(new_value)
#square()

# Function parameters
def square_1(value):
    new_value = value ** 2
    print(new_value)
#square_1(5)

# Return values from functions
def square_2(value):
    squared = value ** 2
    return squared

num = square_2(12) # assign function to a variable 
print(num)

# Docstrings
"""
*Used to describe what the function does, i.e. the computation it performs or its return values.
*Serves as documentation for the function
*Placed in the immediate line after the function header.
*In between tripple double quotes.i.e. """   """
"""
def squared(value):
    """
    Return the square of a value
    """
    new_value = value ** 2
    return new_value

# EXERCISE 

# Strings in Python
"""
*Unlike with numeric types such as ints and floats, the + operator concatenates strings together, while the * concatenates multiple copies of a string together. 
*It is important to remember that assigning a variable y2 to a function that prints a value but does not return a value will result in that variable y2 being of type NoneType.
"""
# Define a function, shout(), which simply prints out a string with three exclamation marks '!!!' at the end.

def shoutss():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = "congratulations" + "!!!"

    # Print shout_word
    print(shout_word)

# Call shout
shoutss()

# Single-parameter functions

# Define shout with the parameter, word
def shouts(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shouts("congratulations")

# Functions that return single values
# Define shout with the parameter, word
def shoutz(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + "!!!"

    # Replace print with return
    return shout_word

# Pass 'congratulations' to shoutz: yell
yell = shoutz("congratulations")

# Print yell
print(yell)

# Multiple Parameters and Return Values
"""
*Function accept more than 1 parameter
*The order in which arguments are passed correspond to the order of parameters in the function header.
"""
def raise_to_power(value1, value2):
    """Raise value1 to the power of value 2"""
    new_value = value1 ** value2
    return new_value
print(raise_to_power(5, 6))

"""
*You can make functions return multiple values using Tuples. 
*Tuples:
    .It is like a list - can contain multiple values
    . It is immutable - you can't modify values
    . Constructed using paranthesis()

*Unpacking tuples into several variables 
        even_nums = (2, 4, 6)
        a,b,c = even_nums

*Accessing tuple elements:
    .Accessed using indexes as with lists
"""
# Returning multiple values 
def raise_to_powers(value1, value2):
    """Raise value1 to the power of value 2 and vice versa.
    """
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1
    new_tuple = (new_value1, new_value2)
    return new_tuple

result = raise_to_powers(5, 6)
print(result)

# EXERCISE 

# Functions with multiple parameters

# Define shout with parameters word1 and word2
def shout(word1, waord2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + "!!!"
    
    # Concatenate word2 with '!!!': shout2
    shout2 = waord2 + "!!!"
    
    # Concatenate shout1 with shout2: new_shout
    new_shout = shout1 + shout2

    # Return new_shout
    return new_shout

# Pass 'congratulations' and 'you' to shout(): yell
yell = shout('congratulations', 'you')

# Print yell
print(yell)

# Tuples 
nums = (3, 4, 6)

# Unpack nums into num1, num2, and num3
num1, num2, num3 = nums

# Construct even_nums
even_nums = (2, 4, 6)

# Functions that return multiple values
# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + "!!!"
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + "!!!"
    
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)

    # Return shout_words
    return shout_words

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1 = shout_all('congratulations', 'you')[0]
yell2 = shout_all('congratulations', 'you')[1]
# Print yell1 and yell2
print(yell1)
print(yell2)

# Bringing it all together (1)
"""
*In this and the following exercise, you will bring together all these concepts and apply them to a simple data science problem. You will load a dataset and develop functionalities to extract simple insights from the data.

*For this exercise, your goal is to recall how to load a dataset into a DataFrame. The dataset contains Twitter data and you will iterate over entries in a column to build a dictionary in which the keys are the names of languages and the values are the number of tweets in the given language. The file tweets.csv is available in your current directory.
"""

# Import Twitter data as DataFrame: df
df = pd.read_csv("tweets.csv")
tweets_df = pd.read_csv("tweets_df.csv")

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1 
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return langs_count

# Call count_entries(): result
result = count_entries(tweets_df, 'lang')

# Print the result
print(result)