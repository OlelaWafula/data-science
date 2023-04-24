import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from functools import reduce

# Lambda functions
"""
*This is the quicker way of writing functions.
*Anonymous functions - These are lambda functions passed to map():
    . Function map takes two arguments: map(func, seq)
    . map() applies the function to ALL elements in the sequence.
"""
# Rewrite raise_to_power() as a lambda function
raise_to_power = lambda x, y: x ** y
raise_to_power(2, 3) # Returns 8

# use map on the lambda function that squares all elements of a list
nums = [48, 6, 9, 21, 1]
square_all = map(lambda num: num ** 2, nums)
print(list(square_all)) # 2304, 36, 81, 441, 1

# EXECISE 

"""
*How would you write a lambda function add_bangs that adds three exclamation points '!!!' to the end of a string a?
* How would you call add_bangs with the argument 'hello'?
"""
add_bangs = (lambda a: a + "!!!")
add_bangs("hello")

"""
*Some function definitions are simple enough that they can be converted to a lambda function. By doing this, you write less lines of code, which is pretty awesome and will come in handy, especially when you're writing and maintaining big programs.

*Take a look at this function definition:

    def echo_word(word1, echo):
    ""Concatenate echo copies of word1.""
    words = word1 * echo
    return words

*The function echo_word takes 2 parameters: a string value, word1 and an integer value, echo. It returns a string that is a concatenation of echo copies of word1. Your task is to convert this simple function into a lambda function.
"""
echo_word = (lambda word1, echo: word1 * echo)
# Call echo_word: result
result = echo_word('hey', 5)
# Print result
print(result)

# Map() and lambda functions
"""
*The best use case for lambda functions are for when you want these simple functionalities to be anonymously embedded within larger expressions.

*What that means is that the functionality is not stored in the environment, unlike a function defined with def. To understand this idea better, you will use a lambda function in the context of the map() function.
"""
# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item + "!!!", spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)

# Print the result
print(shout_spells_list)

# Filter() and lambda functions
"""
*The function filter() offers a way to filter out elements from a list that don't satisfy certain criteria.

*Your goal in this exercise is to use filter() to create, from an input list of strings, a new list that contains only strings that have more than 6 characters.
"""
# In the filter() call, pass a lambda function and the list of strings, fellowship. The lambda function should check if the number of characters in a string member is greater than 6; use the len() function to do this. Assign the resulting filter object to result.

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member) > 6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Print result_list
print(result_list)

# Reduce() and lambda functions
"""
*The reduce() function is useful for performing some computation on a list and, unlike map() and filter(), returns a single value as a result. To use reduce(), you must import it from the functools module.

*gibberish() simply takes a list of strings as an argument and returns, as a single-value result, the concatenation of all of these strings. In this exercise, you will replicate this functionality by using reduce() and a lambda function that concatenates strings together.

# Define gibberish

    def gibberish(*args):
        ""Concatenate strings in *args together.""
        hodgepodge = ''
        for word in args:
            hodgepodge += word
        return hodgepodge
"""

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce((lambda item1, item2: item1 + item2), stark)

# Print the result
print(result)
