import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Error handling
"""
*When you use a function incorrectly it should throw an error. 
"""
# Errors and Exceptions 
"""
* Exceptions - caught during execution.
*Catch exceptions with try-except clause.
    .Python runs the code following try.
    .If there's an exception, run the code following except.
"""
# Write a squareroot function and catch an exceptions raised 

def sqrt(x):
    """
    Returns the square root of a number.
    """
    try:
       return print(x ** 0.5)
    except:
        print(x + " must be an integer or a float")
sqrt("Olela")
sqrt(56478)
# Catching type errors
def sqr(x):
    """
    Returns the square root of a number.
    """
    try:
        return x ** 0.5
    except TypeError:
        print(x +" must be an integer or a float.")
sqr("Olela Wafula")

# Instead of printing an error raise the error

# raise a valueError for negative numbers 
def sqrr(x):
    'Returns square root of a number.'
    if x < 0:
        raise ValueError('x must be non-negative')
    try:
        return print(x ** 0.5)
    except TypeError:
        print("x must be an integer or a float.")
sqrr(-144)

# EXERCISE 

# Error handling with try-except
"""
*A good practice in writing your own functions is also anticipating the ways in which other people (or yourself, if you accidentally misuse your own function) might use the function you defined.
"""
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word = ""
    shout_words =""
    

    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo

        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + "!!!"
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")

    # Return shout_words
    return shout_words

# Call shout_echo
shout_echo("particle", echo=4)

# Error handling by raising an error
"""
*Another way to raise an error is by using raise. In this exercise, you will add a raise statement to the shout_echo() function you defined before to raise an error message when the value supplied by the user to the echo argument is less than 0.
"""
# Define shout_echo
def shout_echoe(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo < 0:
        raise ValueError('echo must be greater than or equal to 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo
shout_echoe("particle", echo=5)

# Bringing it all together

# Load tweets as a DataFrame
tweets_df = pd.read_csv('tweets_df.csv')

# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)

"""
*Sometimes, we make mistakes when calling functions - even ones you made yourself. But don't fret! In this exercise, you will improve on your previous work with the count_entries() function by adding a try-except block to it. 

*This will allow your function to provide a helpful message when the user calls your count_entries() function but provides a column name that isn't in the DataFrame.
"""
# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Add try block
    try:
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

    # Add except block
    except:
        print('The DataFrame does not have a ' + col_name + ' column.')

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)

"""
*raise a ValueError in the case that the user provides a column name that isn't in the DataFrame.
"""
# Define count_entriess()
def count_entriess(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

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

# Print result1
print(result1)