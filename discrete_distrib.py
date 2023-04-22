import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Discrete Distributions

# Discrete  probabilities represent situations for discrete (counted) outcomes.
"""
*Rolling a dice - each side has 1/6 or 17% chance. This is an example of probability distribution. 

*Probability distribution describes the probability of each possible outcome in a scenario.

*Expected value refers to the mean of the distribution.

    .When all outcomes have the same probability like a fair die, this is a special distribution called Discrete Uniform Distribution.
                
    Expected value of a fair die = (1* 1/6) + (2* 1/6) + (3* 1/6) + 
                                   (4* 1/6) + (5* 1/6) + (6* 1/6)

                                 = 3.5  
*We can visulaize the above probability distribution using a bar plot.

*Probability  = area of probability distribution

    e.g. 
        P(die roll) <= 2:
            = 1/6 + 1/6 
            = 1/3

    Expected value of uneven die = (1* 1/6) + (2* 0) + (3* 1/3) + 
                                   (4* 1/6) + (5* 1/6) + (6* 1/6)

                                 = 3.67

*Visualizing uneven die probabilities we get uneven bars.

    e.g.
        P(uneven die roll) <= 2:
            = 1/6 + 0
            = 1/6
"""
# The Law of Large Numbers 
"""
*As the size of your sample increases, the sample mean will approach the expected value.
"""

# EXERCISE 

# Creating a probability distribution
"""
*A new restaurant opened a few months ago, and the restaurant's management wants to optimize its seating space based on the size of the groups that come most often. On one night, there are 10 groups of people waiting to be seated at the restaurant, but instead of being called in the order they arrived, they will be called randomly. In this exercise, you'll investigate the probability of groups of different sizes getting picked first. 
*Data on each of the ten groups is contained in the restaurant_groups DataFrame.

Remember that expected value can be calculated by multiplying each possible outcome with its corresponding probability and taking the sum.
"""
# Load Data 
restaurant_groups = pd.read_csv('restaurant_groups.csv')

# Create a histogram of restaurant_groups and show plot
restaurant_groups['group_size'].hist(bins=[2, 3, 4, 5, 6])
plt.show()

# Create probability distribution
size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]
# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob']

# Expected value
expected_value = np.sum(size_dist['group_size'] * size_dist['prob'])

# Subset groups of size 4 or more
groups_4_or_more = size_dist[size_dist['group_size'] >= 4]

# Sum the probabilities of groups_4_or_more
prob_4_or_more = np.sum(groups_4_or_more['prob'])
print(prob_4_or_more)