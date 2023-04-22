import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import uniform, binom

# The Binomial Distribution
"""
*Binary outcome - is an outcome with two possible values. Can be represennted by 1/0, Success/Failure or Win/Loss.
*In python we can simulate this by importing binom from scipy.stats i.e.

            from scipy.stats import binom

*A single coin flip: 

            binom.rvs(# of coins, probability of heads/success, 
                      size = # of trials)
"""
# Flip one coin with 50% probabilty of heads one time
binom.rvs(1, 0.5, size=1)

# One coin many times 
binom.rvs(1, 0.5, size=8)

# Many coins one time
binom.rvs(8, 0.5, size=1)

# Many coins many times 
binom.rvs(3, 0.5, size=10)

# Other probabilities 
"""
*A coin that is heavier on side than the other. e.g. H = 25%, T = 75%
"""
# Many coins many times 
binom.rvs(3, 0.25, size=10)

# BINOMIAL DISTRIBUTION
"""
*Decsribes the number of successes in a sequence of independent trials. 
e.g. number of heads in a sequence of coin flips.

*Binomial distribution can be described using two parameters n and p:
        n - total number of trials 
        p - probability of success.

        binom.rvs(# of coins, p, n)

        binom.rvs(3, 0.25, size=10)

*N/B - Binomial distribution is only applicable if each trial is independent. i.e. the outcome of one trial should not have an effect on the next trial.
"""
# probability of getting 7 heads out of 10 coins
"""
        binom.pmf(# heads, # trials, probability of heads)
"""
binom.pmf(7, 10, 0.5)

# the probability of getting a number of successes <= first argument
prob_success_7_or_less = binom.cdf(7, 10, 0.5)

# the probability of getting a number of successes >= first argument
prob_success_7_or_more = 1 - binom.cdf(7, 10, 0.5)

# EXPECTED VALUE OF BINOMIAL DISTRIBUTION
"""
    Expected value = n * p
"""
expected_num_heads_out_of_10_flips = 10 * 0.5

# EXRECISE 

# Simulating sales deals
"""
*Assume that Amir usually works on 3 deals per week, and overall, he wins 30% of deals he works on. Each deal has a binary outcome: it's either lost, or won, so you can model his sales deals with a binomial distribution. In this exercise, you'll help Amir simulate a year's worth of his deals so he can better understand his performance.
"""
# Simulate 1 deal worked on by Amir, who wins 30% of the deals he works on.
print(binom.rvs(1, 0.3, size=1))

#Simulate a typical week of Amir's deals, or one week of 3 deals.
print(binom.rvs(3, 0.3, size=1))

# Simulate a year's worth of Amir's deals, or 52 weeks of 3 deals each, and store in deals and Print the mean number of deals he won per week.
deals = binom.rvs(3, 0.3, size=52)
print(deals.mean())

# Calculating binomial probabilities
"""
*Just as in the last exercise, assume that Amir wins 30% of deals. He wants to get an idea of how likely he is to close a certain number of deals each week. 
*In this exercise, you'll calculate what the chances are of him closing different numbers of deals using the binomial distribution.
"""
# What's the probability that Amir closes all 3 deals in a week? Save this as prob_3.
prob_3 = binom.pmf(3, 3, 0.3)
print(prob_3)

# What's the probability that Amir closes 1 or fewer deals in a week? Save this as prob_less_than_or_equal_1.
prob_less_than_or_equal_1 = binom.cdf(1, 3, 0.3)
print(prob_less_than_or_equal_1)

# What's the probability that Amir closes more than 1 deal? Save this as prob_greater_than_1.
prob_greater_than_1 = 1 - binom.cdf(1, 3, 0.3)
print(prob_greater_than_1)

# How many sales will be won?
"""
*Now Amir wants to know how many deals he can expect to close each week if his win rate changes. Luckily, you can use your binomial distribution knowledge to help him calculate the expected value in different situations. 
*Recall from the video that the expected value of a binomial distribution can be calculated by n x p
"""
# Calculate the expected number of sales out of the 3 he works on that Amir will win each week if he maintains his 30% win rate.
won_30pct = 3 * 0.3
print(won_30pct)

# Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate drops to 25%.
won_25pct = 3 * 0.25
print(won_25pct)

# Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate rises to 35%.
won_35pct = 3 * 0.35
print(won_35pct)