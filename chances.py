import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# What are the chances?
"""
*We measure a chance of an event occuring using probability.

                           # ways event can happen
            P(event) =  _________________________________
                           total # of possible outcomes 

*For example flipping a coin

                          1 way to get heads           1
            P(heads) =   _________________________  =  _  = 50%
                          2 possible outcomes          2

*Probability is always between 0 and 100%. If the probability of something is 0%, it is impossible and if it is 100%, it will certainly happen. 
"""
# Load Data
sales_counts = pd.read_csv('sales_counts.csv')
print(sales_counts.head())

# Sampling from a DataFrame
sales_counts.sample() # returns one row from the DataFrame everytime

# Setting a random seed
"""
*Seed is a number that python's random number generator uses as a starting point. The number itself doesn't matter we could use 5, 100 or 3000000. The only thing that matters is that we use the same seed everytime we run the script, to get the same result. 
"""
np.random.seed(10)
sales_counts.sample()# will return the same result everytime script runs

# Sampling without replacement
"""
* Assuming that the two meetings are happening at the same time and Elexar wants its sales people to represent the Company. 
*The above script selects one representative. To get the people to resent Elexar at the two meetings we parse # 2 as argument in the sample() method
"""
np.random.seed(10)
sales_counts.sample(2)

# Sampling with replacement
"""
*To sample with replacement, set the replace argument to True. So that rows can appear more than once. If there were 5 meetings some representative may appear more than once, since we are replacing them each time. 
"""
np.random.seed(10)
sales_counts.sample(5, replace=True)

# Independent events
"""
*Two events are independent if the probability of the second event isn't affected by the outcome of the first event. 

*For example, sampling with replacement of the above code, the probability that Claire will be picked second is 25% regardless of who is picked first because we are replacing. 

*When sampling with replacement, each pick is independent.
"""

# Dependent events
"""
*Two events are dependent if the probability of the second event is affected by the outcome of the first event.

*For example, if we sample without replacement, the probability of Claire being picked second depends on who is picked first. If Claire is picked first, the probability of being picked the second time is 0%. I f someone else is picked first, there is 33% probability that Claire will be picked second.

*When sampling without replacement, each pick is dependent. 
"""

# Radical replacement judgement
"""
*Correctly identifying the type of sampling that needs to be used is key to calculating accurate probabilities. 

*Examples:
    . With Replacement - Flipping a coin 3 times; Rolling a dice twice.
    .Without Replacement - From a deck of cards, dealing 3 players 7 cards each; Randomly selecting 5 products from the assembly line to test for quality assurance; Randomly picking 3 people to work on the weekend from a group of 20 people. 

"""

# Calculating probabilities
"""
*You're in charge of the sales team, and it's time for performance reviews, starting with Amir. 
*As part of the review, you want to randomly select a few of the deals that he's worked on over the past year so that you can look at them more deeply. 
*Before you start selecting deals, you'll first figure out what the chances are of selecting certain deals.
"""
# Load Data 
amir_deals = pd.read_csv('amir_deals.csv')

# Count the deals for each product
counts = amir_deals['product'].value_counts()
print(counts)

#Calculate the probability of selecting a deal for the different product types by dividing the counts by the total number of deals Amir worked on. Save this as probs.
probs = counts / counts.sum()
print(probs)

# Sampling deals
"""
*In the previous exercise, you counted the deals Amir worked on. Now it's time to randomly pick five deals so that you can reach out to each customer and ask if they were satisfied with the service they received. You'll try doing this both with and without replacement.

*Additionally, you want to make sure this is done randomly and that it can be reproduced in case you get asked how you chose the deals, so you'll need to set the random seed before sampling from the deals.
"""
# Set random seed
np.random.seed(24)

# Sample 5 deals without replacement
sample_without_replacement = amir_deals.sample(5)
print(sample_without_replacement)

# Set random seed
np.random.seed(24)

# Sample 5 deals with replacement
sample_with_replacement = amir_deals.sample(5, replace=True)
print(sample_with_replacement)