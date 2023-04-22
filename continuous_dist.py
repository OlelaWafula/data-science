import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Continuous Distributions
"""
*Probability = area

*Get the probability of waiting for a bus between minute 4 and 7:
    .Note wait time for a bus is between minute 0 and 12

    P(4 <= wait time <= 7) = (7-4) * 1/12
                           = 3/12 
                           = 25%
"""
# Use uniform distribution in Python to calculate probability of waiting for 7 minues or less:
from scipy.stats import uniform

prob_wait_time_7_or_less = uniform.cdf(7, 0, 12) # 0 - lower limit, 12 - upper limit # returns 58%

prob_wait_time_7_or_more = 1- prob_wait_time_7_or_less

prob_wait_time_4_to_7 = uniform.cdf(7, 0, 12) - uniform.cdf(4, 0, 12)

# Generating random numbers according to uniform distribution
uniform.rvs(0, 5, size=10) # 0 - minimum, 5 - maximum value

# EXERCISE 

# Data back-ups
"""
*he sales software used at your company is set to automatically back itself up, but no one knows exactly what time the back-ups happen. It is known, however, that back-ups happen exactly every 30 minutes. 

*Amir comes back from sales meetings at random times to update the data on the client he just met with. He wants to know how long he'll have to wait for his newly-entered data to get backed up. Use your new knowledge of continuous uniform distributions to model this situation and answer Amir's questions.
"""
# To model how long Amir will wait for a back-up using a continuous uniform distribution, save his lowest possible wait time as min_time and his longest possible wait time as max_time. Remember that back-ups happen every 30 minutes.

min_time = 0
max_time = 30

# Import uniform from scipy.stats and calculate the probability that Amir has to wait less than 5 minutes, and store in a variable called prob_less_than_5.

from scipy.stats import uniform

prob_less_than_5 = uniform.cdf(5,0, 30)
print(prob_less_than_5)

# Calculate the probability that Amir has to wait more than 5 minutes, and store in a variable called prob_greater_than_5.

prob_greater_than_5 = 1- uniform.cdf(5, 0, 30)
print(prob_greater_than_5)

# Calculate the probability that Amir has to wait between 10 and 20 minutes, and store in a variable called prob_between_10_and_20.

prob_between_10_and_20 = uniform.cdf(20, 0, 30) - uniform.cdf(10, 0, 30)
print(prob_between_10_and_20)

# Simulating wait times
"""
*To give Amir a better idea of how long he'll have to wait, you'll simulate Amir waiting 1000 times and create a histogram to show him what he should expect. Recall from the last exercise that his minimum wait time is 0 minutes and his maximum wait time is 30 minutes.
"""
# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform

# Generate 1000 wait times between 0 and 30 mins
wait_times = uniform.rvs(0, 30, size=1000)

# Create a histogram of simulated times and show plot
plt.hist(wait_times)
plt.show()