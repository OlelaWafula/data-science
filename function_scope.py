import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Scope and user-defined functions
"""
*Not all objects are accessible everywhere in a program.
*Scope - which part of a program where an object or name may be accessed.
*Types of scope:
    .Global scope - defined in the main body of the script or program. 

    Local scope - defined within a function once execution of a function is complete any name within the local scope ceases to exist. i.e. You cannot access those names outside the function definition.

    .Built-in scope - consists of names in the pre-defined built-ins module python provides such as print(), sum(), etc.
"""
def square(value):
    """
    Returns the square of a number.
    """
    new_value = value ** 2
    return new_value
square(3)
"""
*If we try to access the variable new_value outside the function, the name is inaccessible and returns an error. i.e. It was defined only within the local scope of a function.
"""
# Defining the name globally
new_val = 2

def squared(val):
    """
    Return the square of a number.
    """
    new_val = val ** 2
    return new_val
square(3)
"""
*When we reference a name, first the local scope is searched, then the global, if the name is in neither then the built-in scope is searched.
"""
# Altering the value of a global name within a function call, this is where the key name global is useful. 
new_num = 10 

def squarred(num):
    """
    A function to return the square of a number.
    """
    global new_num 
    new_num = new_num ** 2
    return new_num
squarred(3)
print(new_num) 

# EXERCISE 

# The keyword global

# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = "justice league"
# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)

# NESTED FUNCTIONS
"""
        def outer(...):
            "" ... ""
            x = ...

            def inner(...):
                "" ... ""
                y = x ** 2
            return ...

*Why nest functions:
    .Need to use a function several times, define an ineer function within a function and call it when necessary.
"""
def mod2plus5(x1,x2,x3):
    """
    Returns the remainder plus 5 of three values.
    """
    def inner(x):
        """
        Returns the remainder plus 5 of a value
        """
        return x % 2 + 5
    
    return (inner(x1), inner(x2), inner(x3))

print(mod2plus5(1, 2, 3)) # (6, 5, 6)

# Returning functions 
def raise_val(n):
    """
    Return the inner function.
    """
    def inner(x):
        raised = x ** n
        return raised
    
    return inner

squar = raise_val(2) # creates a function that squares any number
cube = raise_val(3) # creates a function that cubes any number
print(squar(2), cube(4)) # Returns 4 and 64

# Nested functions use of nonlocal to create and change names in an enclosing scope
def outer():
    """
    Prints the value of n.
    """
    n = 1

    def innerr():
        nonlocal n
        n = 2
        print(n)

    innerr()
    print(n)

print(outer()) # Returns 2 and 2

# EXERCISE 

# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))

# Nested Functions 
"""
*One other pretty cool reason for nesting functions is the idea of a closure. This means that the nested or inner function remembers the state of its enclosing scope when called. Thus, anything defined locally in the enclosing scope is available to the inner function even when the outer function has finished execution.
"""
# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))

# The keyword nonlocal and nested functions

# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""
    
    # Concatenate word with itself: echo_word
    echo_word = word + word
    
    # Print echo_word
    print(echo_word)
    
    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""    
        # Use echo_word in nonlocal scope
        nonlocal echo_word
        
        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + "!!!"
    
    # Call function shout()
    shout()
    
    # Print echo_word
    print(echo_word)

# Call function echo_shout() with argument 'hello'
echo_shout('hello')