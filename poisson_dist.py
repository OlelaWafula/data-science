import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import uniform, binom, norm, poisson
# The Poisson Distribution
"""
*Poisson Process Events appear to happed at a certain rate, but completely at random. e.g. 
    The number of animals adopted from an animal shelter per week. 
    The number of people arriving at a restuarant each hour.
    The number of earthquakes per year in jAPAN. 

* The time unit is irrelevant as long as you use the same unit when talking about the same situation. 

*The Poisson distribution describes the probability of some number of events happening over a fixed period of time. e.g.

        Probability of >=5 animals adopted per week.
        Probability of 12 people arriving at a restuarant in an hour
        Probability of <20 earthquakes in Japan per Year.

*Poisson distribution is represented by Lambda(λ):
        . λ = average number of events per time interval. This value is also the expected value of the distribution.
            e.g.
            Avergae number of adoptions per week = 8
"""
# Probability of a single value
"""
*If the average number of adoptions per week is 8, whats is the probability that the number of adoptions in a week = 5?
"""
prob_5_in_a_week = poisson.pmf(5,8)
print(prob_5_in_a_week) # returns around 9%

# Probability of less than or equal to
"""
**If the average number of adoptions per week is 8, whats is the probability that the number of adoptions in a week <= 5?
"""
prob_5_or_less_in_a_week = poisson.cdf(5, 8)
print(prob_5_or_less_in_a_week) # returns around 20%

# Probability of greater than 
prob_greater_than_5 = 1- poisson.cdf(5, 8)
print(prob_greater_than_5) # returns around 81%

# sampling from a Poisson distribution
poisson.rvs(8, size=10)

# EXERCISE 

# Tracking lead responses 
"""
*Your company uses sales software to keep track of new sales leads. It organizes them into a queue so that anyone can follow up on one when they have a bit of free time. 
*Since the number of lead responses is a countable outcome over a period of time, this scenario corresponds to a Poisson distribution. 
*On average, Amir responds to 4 leads each day. 
*In this exercise, you'll calculate probabilities of Amir responding to different numbers of leads.
"""
# Calculate the probability that Amir responds to 5 leads in a day, given that he responds to an average of 4.
prob_5 = poisson.pmf(5, 4)
print(prob_5)

# Amir's coworker responds to an average of 5.5 leads per day. What is the probability that she answers 5 leads in a day?

# Probability of 5 responses
prob_coworker = poisson.pmf(5, 5.5)
print(prob_coworker)

# What's the probability that Amir responds to 2 or fewer leads in a day?
prob_2_or_less = poisson.cdf(2, 4)
print(prob_2_or_less)

# What's the probability that Amir responds to more than 10 leads in a day?
prob_over_10 = 1 - poisson.cdf(10, 4)
print(prob_over_10)