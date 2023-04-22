import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import uniform, binom, norm

# The Normal Distribution
"""
*The shape of a normal distribution is commonly referred to as a bell curve. 

*Properties of a normal distribution:
    i. symmetrical - the left side is the mirror image of the right. 
    ii. area beneath the curve = 1.
    iii. curve never hits 0 - the probability never hits o. 

*The normal distribution is described by its mean and standard deviation. 
*When a normal distribution has mean = 0 and standard deviation = 1, it is a special distribution called THE STANDARD NORMAL DISTRIBUTION. 

*For a normal distribution - The 68-95-99.7 Rule:
            - 68% of the area is within 1 standard deviation. i.e. between -1 and 1 on the x-axis.
            - 95% of the area falls within 2 standard deviations of the area. i.e. between -2 and 2 on the x-axis.
            - 99.7% of the area falls within 3 standard deviations of the area. i.e. between -3 and 3 on the x-axis.
"""
# Approximating data with the normal distribution
"""
        norm.cdf(# number of interest, mean, standard deviation)
"""
# What percentage of women are shorter than 154 cm?
shorter_than_154 = norm.cdf(154, 161, 7) # Returns 16% of the women. 

# What c
taller__than_154 = 1 - norm.cdf(154, 161, 7) # Returns 84% of women. 

# percentage of women are 154 - 157 cm?
between_154_and_157 = norm.cdf(157, 161, 7) - norm.cdf(154, 161, 7) #12.5%

# Calculating perccntiles 

# What height are 90% of women shorter than?
height_90percent_shorter_than = norm.ppf(0.9, 161, 7) # 90% of women are shorter than 169.97086 cm tall. 

# What height are 90% of women taller than?
height_90percent_taller_than = norm.ppf(1 - 0.9, 161, 7) # 152.029 cm

# Generating Random Numbers 
"""
    random_numbers = norm.rvs(mean, standard deviation, size=n)
"""
#Generate 10 random numbers 
ten_random_numbers = norm.rvs(161, 7, size = 10)

# EXERCISE 

# Distribution of Amir's sales
"""
*Since each deal Amir worked on (both won and lost) was different, each was worth a different amount of money. 
*These values are stored in the amount column of amir_deals As part of Amir's performance review, you want to be able to estimate the probability of him selling different amounts, but before you can do this, you'll need to determine what kind of distribution the amount variable follows.
"""
# Load Data 
amir_deals = pd.read_csv('amir_deals.csv')

# Create a histogram with 10 bins to visualize the distribution of the amount. Show the plot.
amir_deals['amount'].hist(bins=10)
plt.show()

# Probabilities from the normal distribution
"""
*Since each deal Amir worked on (both won and lost) was different, each was worth a different amount of money. 
*These values are stored in the amount column of amir_deals and follow a normal distribution with a mean of 5000 dollars and a standard deviation of 2000 dollars. As part of his performance metrics, you want to calculate the probability of Amir closing a deal worth various amounts.
"""
# What's the probability of Amir closing a deal worth less than $7500?
prob_less_7500 = norm.cdf(7500, 5000, 2000)
print(prob_less_7500)

#What's the probability of Amir closing a deal worth more than $1000?
prob_over_1000 = 1 - norm.cdf(1000, 5000, 2000)
print(prob_over_1000)

# What's the probability of Amir closing a deal worth between $3000 and $7000?
prob_3000_to_7000 = norm.cdf(7000, 5000, 2000) - norm.cdf(3000, 
                                                          5000, 2000)
print(prob_3000_to_7000)

# What amount will 25% of Amir's sales be less than?
pct_25 = norm.ppf(0.25, 5000, 2000)
print(pct_25)

# Simulating sales under new market conditions
"""
*The company's financial analyst is predicting that next quarter, the worth of each sale will increase by 20% and the volatility, or standard deviation, of each sale's worth will increase by 30%. 
*To see what Amir's sales might look like next quarter under these new market conditions, you'll simulate new sales amounts using the normal distribution and store these in the new_sales DataFrame, which has already been created for you.
"""
# Currently, Amir's average sale amount is $5000. Calculate what his new average amount will be if it increases by 20% and store this in new_mean.
new_mean = 5000 * 1.2

# Amir's current standard deviation is $2000. Calculate what his new standard deviation will be if it increases by 30% and store this in new_sd.
new_sd = 2000 * 1.3

# Create a variable called new_sales, which contains 36 simulated amounts from a normal distribution with a mean of new_mean and a standard deviation of new_sd.
new_sales = norm.rvs(new_mean, new_sd, size=36)

# Plot the distribution of the new_sales amounts using a histogram and show the plot.
plt.hist(new_sales)
plt.show()

# Which market is better?
"""
*The key metric that the company uses to evaluate salespeople is the percent of sales they make over $1000 since the time put into each sale is usually worth a bit more than that, so the higher this metric, the better the salesperson is performing.

*Recall that Amir's current sales amounts have a mean of $5000 and a standard deviation of $2000, and Amir's predicted amounts in next quarter's market have a mean of $6000 and a standard deviation of $2600.

*Based only on the metric of percent of sales over $1000, does Amir perform better in the current market or the predicted market?
"""
current_market = 1 - norm.cdf(1000, 5000, 2000)
print(current_market) # 0.97725

new_market = 1 - norm.cdf(1000, 6000, 2600)
print(new_market) # 0.97276

"""
Amir performs about equally in both markets.
"""