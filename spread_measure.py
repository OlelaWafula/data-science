import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import iqr

# Measures of Spread
"""
*Spread describes how spread apart or close together the data points are.

    i. Variance - measures average distance from each data point to the mean.
        # Calculating Variance:
            .Subtract mean from each data point
            .Square each distance
            .Sum squared distances 
            .Divide the sum of square distances by the number of data points - 1 (n-1)
        # The higher the variance, the more spread the data is.
        # Units of varianced are squared.
        # we can use python to calculate variance as:

            variance = np.var(msleep['sleep_total'], ddof=1)

                *Without ddof=1, population variance is calculated instead of sample variance. 
    
    ii. Standard deviation
        #Calculated by getting squareroot of the variance

            std_dev = np.sqrt(np.var(msleep['sleep_total'], ddof=1))

                                OR

            std_dev = np.std(msleep['sleep_total'], ddof=1)

    iii. Mean absolute deviation
        # gets the mean of absolute distances values from the mean

            dists = msleep[msleep['sleep_total']] - np.mean(msleep['sleep_total'])

            mean_absolute_dev = np.mean(dists)
            
"""
# Load Data 
msleep = pd.read_csv('msleep.csv')

# Variance 
dists = msleep[msleep['sleep_total']] - np.mean(msleep['sleep_total'])
sq_dists = dists ** 2
sum_sq_dists = np.sum(sq_dists)

variance = sq_dists / (83-1)
variance = np.var(msleep['sleep_total'], ddof=1)

# Standard deviation
std_dev = np.sqrt(np.var(msleep['sleep_total'], ddof=1))

std_dev = np.std(msleep['sleep_total'], ddof=1)

# Mean Absolute deviation
dists = msleep[msleep['sleep_total']] - np.mean(msleep['sleep_total'])
mean_absolute_dev = np.mean(dists)

"""
* Standard deviation vs. mean absolute deviation
    .Standard deviation squares distances, penalizing longer distances more than shorter ones. 
    .Mean absolute deviation penalizes each distances equally. 
    .SD is more common than MAD
"""

# Quantiles / Percentiles 
"""
*Splits up the data into some number of equal parts.
"""
np.quantile(msleep['sleep_total'], 0.5) # 0.5 quantile = Median
np.quantile(msleep['sleep_total'], [0, 0.25, 0.5, 0.75, 1]) # Quartiles

# Boxplots use quartiles 
"""
#The boxes in boxplots represent quartiles. 
    *The bottom of the box is the first quartile.
    *THE top of the box is the third quartile.
    *The middle line is the second quartile/the median.

#We can use np.linspace() as a shortcut for a list of quartiles:
    
    np.linspace(start, stop, num)

    start - first quartile
    stop - last quartile
    num - number of quartiles
"""
np.quantile(msleep['sleep_total'], np.linspace(0, 1, 5))

# iv. Interquartile range (IQR)
"""
*It is another measure of spread. 
*It is the distance between the 25th and the 75th percentile. 
*It is also the height of the box in a boxplot.
*Cab be calculated by: 

    iqrange = np.quantile(msleep['sleep_total'], 0.75) - np.quantile(msleep['sleep_total'], 0.25) 

            OR

    iqrange = iqr(msleep['sleep_total'])

"""
iqrange = np.quantile(msleep['sleep_total'], 0.75) - np.quantile(msleep['sleep_total'], 0.25)

iqrange = iqr(msleep['sleep_total'])

# Outliers 
"""
*Data points that are substantially different from the others.
*How do we know what a substantial difference is? A data point is an outlier if: 

    . data < Q1 - 1.5 * IQR 

    or any data

    . data > Q3 + 1.5 * IQR
"""
#Finding outliers
"""
*First calculate the iqr 
"""

iqr = iqr(msleep['bodywt'])
lower_threshold = np.quantile(msleep['bodywt'], 0.25) - 1.5 * iqr
upper_threshold = np.quantile(msleep['bodywt'], 0.75) + 1.5 * iqr

# subset the dataframe to find the mammals whose body weight are lower or above the body weight thresholds:
msleep[(msleep['bodywt'] < lower_threshold) | 
       (msleep['bodywt'] > upper_threshold)]

# Many of the above summary statistics can be calculated using .describe()
msleep['bodywt'].describe()

# EXERCISE 

# Quartiles, quantiles, and quintiles
"""
*Quantiles are a great way of summarizing numerical data since they can be used to measure center and spread, as well as to get a sense of where a data point stands in relation to the rest of the data set. For example, you might want to give a discount to the 10% most active users on a website.

*In this exercise, you'll calculate quartiles, quintiles, and deciles, which split up a dataset into 4, 5, and 10 pieces, respectively.
"""
# Load Data
food_consumption = pd.read_csv('food_consumption.csv')

# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0,1, 5)))

# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], 
                  [0, 0.2, 0.4, 0.6, 0.8, 1]))

# Calculate the deciles of co2_emission
print(np.quantile(food_consumption['co2_emission'], 
                  np.linspace(0, 1, 11)))

# Variance and standard deviation
"""
*Variance and standard deviation are two of the most common ways to measure the spread of a variable, and you'll practice calculating these in this exercise. Spread is important since it can help inform expectations. 
*For example, if a salesperson sells a mean of 20 products a day, but has a standard deviation of 10 products, there will probably be days where they sell 40 products, but also days where they only sell one or two. Information like this is important, especially when making predictions.
"""
# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Create histogram of co2_emission for food_category 'beef'
food_consumption.query('food_category=="beef"')['co2_emission'].hist()
# Show plot
plt.show()

# Create histogram of co2_emission for food_category 'eggs'
food_consumption.query('food_category=="eggs"')['co2_emission'].hist()
# Show plot
plt.show()

# Finding outliers using IQR
"""
Outliers can have big effects on statistics like mean, as well as statistics that rely on the mean, such as variance and standard deviation. Interquartile range, or IQR, is another way of measuring spread that's less influenced by outliers. IQR is also often used to find outliers. I
*If a value is less than Q1 - 1.5 * IQR  or greater than Q3 + 1.5 * IQR, it's considered an outlier. In fact, this is how the lengths of the whiskers in a matplotlib box plot are calculated.
"""
# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]
print(outliers)