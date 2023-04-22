import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import uniform, binom, norm

# The Central Limit Theorem (CLT)
"""
*The sampling distribution will approach a normal distribution as the number of trials increases. 
*The central limit theorem only applies when:
        i. samples are taken randomly
        ii. samples are independent
"""
# Rolling the dice 5 times
die = pd.Series([1, 2, 3, 4, 5, 6])

# Roll 5 times
samp_5 = die.sample(5, replace=True)
print(samp_5) # array([3, 1, 4, 1, 1])
np.mean(samp_5)

# Rolling the dice 5 times 10 times and get the sample means
sample_means = []
for i in range(10):
    samp_5 = die.sample(5, replace=True)
    sample_means.append(np.mean(samp_5))
print(sample_means)

# Sampling distribution - a distribution of summary statistics.
"""
*Plotting the sample_means we get SAMPLING DISTRIBUTION OF THE SAMPLE MEAN
"""
# 100 Sample means
sample_means = []
for i in range(100):
    sample_means.append(np.mean(die.sample(5, replace=True)))
print(sample_means)

# 100 Sample means 
sample_means = []
for x in range(1000):
    sample_means.append(np.mean(die.sample(5, replace=True)))
print(sample_means)

# Plot the sample means
plt.hist(sample_means)
plt.title('SAMPLING DISTRIBUTION OF THE SAMPLE MEAN')
plt.xlabel('Sample Mean')
plt.ylabel('Number')
plt.show()

# Standard deviation and the CLT
sample_stds = []
for m in range(1000):
    sample_stds.append(np.std(die.sample(5, replace=True)))
print(sample_stds)

# Proportions and the CLT
sales_team = pd.Series(['Amir', 'Brian', 'Claire', 'Damian'])
sample_props = sales_team.sample(10, replace=True)

# Mean of sampling distribution

# Estimate the expected value of a die
np.mean(sample_means)

# Estimate proportion of "claire"s 
np.mean(sample_props)

# When to use CLT
"""
*Estimate characteristics of unknown underlying distribution. 
*More easily estimate characteristics of a large population. 
"""
# EXERCISE 

# The CLT in action
"""
*The central limit theorem states that a sampling distribution of a sample statistic approaches the normal distribution as you take more samples, no matter the original distribution being sampled from.

*In this exercise, you'll focus on the sample mean and see the central limit theorem in action while examining the num_users column of amir_deals more closely, which contains the number of people who intend to use the product Amir is selling.
"""
# Load Data 
amir_deals = pd.read_csv('amir_deals.csv')

# Create a histogram of the num_users column of amir_deals and show the plot.
amir_deals['num_users'].hist()
plt.show()

# Set the seed to 104, Take a sample of size 20 with replacement from the num_users column of amir_deals, and take the mean.
samp_20 = amir_deals['num_users'].sample(20, replace=True)
print(np.mean(samp_20))

# Repeat this 100 times using a for loop and store as sample_means. This will take 100 different samples and calculate the mean of each.
sample_means = []

# Loop 100 times
for i in range(100):
  samp_20 = amir_deals['num_users'].sample(20, replace=True)
  samp_20_mean = np.mean(samp_20)
  sample_means.append(samp_20_mean)
print(sample_means)

# Convert sample_means into a pd.Series, create a histogram of the sample_means, and show the plot.
sample_means_series = pd.Series(sample_means)
sample_means_series.hist()
plt.show()

# The mean of means
"""
*You want to know what the average number of users (num_users) is per deal, but you want to know this number for the entire company so that you can see if Amir's deals have more or fewer users than the company's average deal. The problem is that over the past year, the company has worked on more than ten thousand deals, so it's not realistic to compile all the data. Instead, you'll estimate the mean by taking several random samples of deals, since this is much easier than collecting data from everyone in the company.

*amir_deals is available and the user data for all the company's deals is available in all_deals.
"""
# Load Data 
all_deals = pd.read_csv('all_deals.csv')

# Set the random seed to 321.
np.random.seed(321)

# Take 30 samples (with replacement) of size 20 from all_deals['num_users'] and take the mean of each sample. Store the sample means in sample_means.
sample_means = []
# Loop 30 times to take 30 means
for i in range(30):
  # Take sample of size 20 from num_users col of all_deals with replacement
  cur_sample = all_deals['num_users'].sample(20, replace=True)
  # Take mean of cur_sample
  cur_mean = np.mean(cur_sample)
  # Append cur_mean to sample_means
  sample_means.append(cur_mean)

# Print mean of sample_means
print(np.mean(sample_means))

# Print mean of num_users in amir_deals
print(np.mean(amir_deals['num_users']))