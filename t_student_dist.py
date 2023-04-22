import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import uniform, binom, norm, poisson, expon

# ()Student's) t - distribution

"""
*Has an almost similar shape as the normal distribution but not quite the same. 

*The t - distributions tails are thicker, this means that in a t - distribution, observations are more likely to fall further from the mean.

*The t -distribution has a parameter called the degrees of freedom (df) which affects the thickness of the distribution's tails. 
        - Lower df results in thicker tails, and a higher standard deviation. 
        - Higher df - increases in degrees of freedom makes the t - distribution to resemble a normal distribution. 
"""

# Log - normal distribution
"""
*Variables that follow log - normal distribution have logarithm that is normally distributed. This results in distributions that are skewed unlike the normal distribution. 

*Examples of log- normal distribution are:
        - Length of chess games 
        - Blood pressure in adults
        - Number of hospitalizations in the COVID-19 outbreak
"""

# Examples of distributions:
"""
i. Poisson distribution :
        . Number of products sold each week. 
        . Number of customers that enter a store each hour.

ii. Exponrntial distribution :
        . Amount of time until someone pays off their loan.
        . Amount of time until the next customer makes a purchase.

iii. Binomial distribution :
        . Number of people from a group of 30 that pass their driving test.
"""
