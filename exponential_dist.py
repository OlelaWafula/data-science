import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import uniform, binom, norm, poisson, expon

# Exponrntial Distribution
"""
*Represents the probability of time between Poisson events.

*We can use exponential distribution to predict:
       - the probability of more than a day between adoptions.
       - the probability of fewer than ten minutes between restuarant arrivals.
       - the probability of 6 - 8 months passing between the earthquakes.

*Uses the same lambda value which represents the rate that the Poisson distribution does. 

*It is continuous  since it represents time. e.g.

    # Customer service requests
        . Let's say that on average, one customer service ticket is created every 2 minutes.

            We can rephase this so that it is in terms of time interval of one minute. 

                    λ  = 0.5 customer service tickets created each time. 

    # since λ in Poisson is the expected value, then the expected number of requests per minute is 0.5 i.e. λ = 0.5 requests per minute.

    # In terms of time (exponential distribution):

                    the expected value = 1 / λ
                                       = 1 / 0.5
                                       = 2 i.e. 1 request every 2 minutes. 
"""
# How long until a new request is created?
"""
*The probability of waiting for less than 1 minute for a new request:
"""
prob_less_than_a_minute = expon.cdf(1, scale=2)
print(prob_less_than_a_minute) # returns around 40% chance.

prob_wait_more_than_4_minutes = expon.cdf(4, scale=2)
print(prob_wait_more_than_4_minutes) # returns around 14% chance

prob_wait_btn_1_and_4_minutes = expon.cdf(4, scale=2) - expon.cdf(1, 
                                                                  scale=2)
print(prob_wait_btn_1_and_4_minutes) # returns around 48% chance


# EXERCISE 

# Modeling time between leads

"""
*To further evaluate Amir's performance, you want to know how much time it takes him to respond to a lead after he opens it. On average, he responds to 1 request every 2.5 hours. In this exercise, you'll calculate probabilities of different amounts of time passing between Amir receiving a lead and sending a response.
"""
# What's the probability it takes Amir less than an hour to respond to a lead?
print(expon.cdf(1, scale=2.5))

# What's the probability it takes Amir more than 4 hours to respond to a lead?
print(1 - expon.cdf(4, scale=2.5))

# What's the probability it takes Amir 3-4 hours to respond to a lead?
print(expon.cdf(4, scale=2.5) - expon.cdf(3, scale=2.5))