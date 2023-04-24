import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Default and flexible arguments

# Add a default argument
def power(number, pow=1):
    """
    Raise number to the power of pow.
    """
    new_value = number ** pow
    return new_value
power(9, 2) # Returns 81
power(9) # Returns 9

# Flexible arguments: *args
"""
*Write a function but not sure how many arguments will be used. 
"""
def add_all(*args):
    """
    Sum all values in *args together.
    """
    # initialize sum
    sum_all = 0

    # Accumulate the sum
    for num in args:
        sum_all += num

    return sum_all

add_all(1) # Returns 1
add_all(1, 2) # Returns 3
add_all(5,10, 15, 20)# Returns 50

# Flexible arguments **kwargs - keyword arguments
"""
*Arguments preceeded by identifiers.
"""
def print_all(**kwargs):
    """
    Print out key-value pairs in kwargs.
    """
    # Print out the key-value pairs
    for key, value in kwargs.items():
        print(key + ":" + value)

print_all(name="Dennis Tarno", title="MD") # Returns name: Dennis Tarno     title: MD

# EXERCISE 

# Functions with one default argument\

# Define shout_echo
def shouts_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shouts_echo("Hey")

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shouts_echo("Hey", 5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo)

# Functions with multiple default arguments

# Define shout_echo
def shout_echo(word1, echo=1, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Make echo_word uppercase if intense is True
    if intense is True:
        # Make uppercase and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'

    # Return echo_word_new
    return echo_word_new

# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo("Hey", 5, True)

# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo("Hey", intense=True)

# Print values
print(with_big_echo)
print(big_no_echo)

# Functions with variable-length arguments (*args)
"""
*Flexible arguments enable you to pass a variable number of arguments to a function. In this exercise, you will practice defining a function that accepts a variable number of string arguments.

*The function you will define is gibberish() which can accept a variable number of string values. Its return value is a single string composed of all the string arguments concatenated together in the order they were passed to the function call. You will call the function with a single string argument and see how the output changes with another call using more than one string argument. Recall from the previous video that, within the function definition, args is a tuple.
"""
# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge = ""

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word

    # Return hodgepodge
    return hodgepodge

# Call gibberish() with one string: one_word
one_word = gibberish("luke")

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)

# Functions with variable-length keyword arguments (**kwargs)
"""
*What makes **kwargs different is that it allows you to pass a variable number of keyword arguments to functions. Recall from the previous video that, within the function definition, kwargs is a dictionary.

*Define a function that accepts a variable number of keyword arguments. The function simulates a simple status report system that prints out the status of a character in a movie.
"""
# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

    print("\nEND REPORT")

# First call to report_status()
report_status(name="luke", affiliation="jedi", status="missing")

# Second call to report_status()
report_status(name="anakin", affiliation="sith lord", status="deceased")

# Bringing it all together

# Load datasets
tweets_df = sns.load_dataset("tweets_df")

# Define count_entries()
def count_entriess(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1

        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entriess(tweets_df)

# Call count_entries(): result2
result2 = count_entriess(tweets_df, col_name='source')

# Print result1 and result2
print(result1)
print(result2)

"""
*Generalize the above function one step further by allowing the user to pass it a flexible argument, that is, in this case, as many column names as the user would like!
"""
# Define count_entries()
def count_entries(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    #Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # Iterate over column names in args
    for col_name in args:
    
        # Extract column from DataFrame: col
        col = df[col_name]
    
        # Iterate over the column in DataFrame
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
    
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang', 'source')

# Print result1 and result2
print(result1)
print(result2)