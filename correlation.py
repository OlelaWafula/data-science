import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Correlation
"""
*The variable on x - axis is called the explanatory or independent variable.
*The variable on y - axis is called the response/dependent variable.

*Correlation coefficient - quantifies the linear relationship between two variables. It is a number between 1 and - 1, magnitude corresponds to strength of the relationship and the sign(+ or -) corresponds to the direction of the relationship.

*A positive correlation coefficient indicates that as x oncreases y also increases.
*A negative correlation coefficient indicates that as x increases y decreases.
*We can use scatter plot to visualize relationship between two variables."""
# Load Data
msleep = pd.read_csv('msleep.csv')

# scatter plot using seaborn
sns.scatterplot(x="sleep_total", y="sleep_rem", data=msleep)
plt.show()

# Adding a linear trendline to the scatterplot
# ci = None eliminates any confidence interval margins around the line
sns.lmplot(x="sleep_total", y="sleep_rem", data=msleep, ci=None) 

"""
*Trendlines like these can be helpful to more easily identify the relationship between two variables.
"""
# computing correlation
r = msleep["sleep_t0tal"].corr(msleep["sleep_rem"])

"""
*Pearson product-moment correlation (r) is the most common.
*Variations to Pearson(r) are Kendall's tau and Spearman's rho.
"""
# EXERCISE 

# Relationships between variables
"""
*In this chapter, you'll be working with a dataset world_happiness containing results from the 2019 World Happiness Report. The report scores various countries based on how happy people in that country are. It also ranks each country on various societal aspects such as social support, freedom, corruption, and others. The dataset also includes the GDP per capita and life expectancy for each country.

*In this exercise, you'll examine the relationship between a country's life expectancy (life_exp) and happiness score (happiness_score) both visually and quantitatively.
"""
# Load Data 
world_happiness = pd.read_csv('world_happiness.csv')

# Create a scatterplot of happiness_score vs. life_exp (without a trendline) using seaborn.
sns.scatterplot(x="life_exp", y="happiness_score", data=world_happiness)
plt.show()

# Create a scatterplot of happiness_score vs. life_exp with a linear trendline using seaborn, setting ci to None.
sns.lmplot(x="life_exp", y="happiness_score", 
           data=world_happiness, ci=None)
plt.show()

# Calculate the correlation between life_exp and happiness_score. Save this as cor.
cor = world_happiness['life_exp'].corr(world_happiness['happiness_score'])
print(cor) # returns 0.7802249053272062

# CORRELATION CAVEATS 
"""
*Non-linear relationships - Correlation only accounts for linear relationships, therefore just like summary statistics, correlations shouldn't be used blindly. 
*Always visualize your data when calculating correlation. 
*When the data is highly skewed we can apply a log transformation. 
"""
# create a new column to hold log(bodywt)
msleep['log_bodywt'] = np.log(msleep['bodywt'])

# plotting log_bodywt v awake gives a linear relationship
sns.lmplot(x="log_bodywt", y="awake", data=msleep, ci=None)
plt.show()

# OTHER TRANSFORMATIONS TO MAKE RELATIONSHIP MORE LINEAR
"""
    . Squareroot transformation (sqrt(x))
    . Reciprocal transformation (1/ x)

*The choice of the transformation will depend on the data and how skewed it is. 
                # A combination of these may apply:
                    . log(x) and log(y)
                    . sqrt(x) and 1 / y

                # Why use a transformation?
                    . Certain statistical methods rely on variables having a linear relationship. e.g. 
                                    - correlation coefficient
                                    - Linear regression

*Correlation doesnot imply causation i.e. if x and y are correlated does mean x causes y. e.g. A scatterplot of per capita margarine consumption in the US (lbs/year) v divorce rate in the state of Maine - the correlation between these two variables is 0.99, which is nearly perfect, however this foesn't mean that consuming more margarine will cause more divorces. This is called Spurious correlation - a spurious correlation (or spuriousness) refers to a connection between two variables that appears to be causal but is not.

A phenomenon called confounding can lead to a spurious correlation.e.g   
    i. The relationship between coffee drinking (x) and lung cancer (y) has smoking as a confounder, smoking is associated with coffee consumption, it is also known that smoking causes lung cancer. In reality it turns out that coffee does not cause lung cancer, and is only associated with it but it appeared causal due to the third variable associated with it.

    ii. The relationship between holidays (x) and retail sales (y). While it might be that people buy more around the holidays as a way of celebrating, it is hard to tell how much of the increased sales is due to holidays, and how much is due to special deals and promotions (confounder) that are often run around the holidays. Here, special deals confound the relationship between holidays and sales. 
"""

# EXERCISE 

# What can't correlation measure?
"""
*While the correlation coefficient is a convenient way to quantify the strength of a relationship between two variables, it's far from perfect. 

*In this exercise, you'll explore one of the caveats of the correlation coefficient by examining the relationship between a country's GDP per capita (gdp_per_cap) and happiness score.
"""
# Create a seaborn scatterplot (without a trendline) showing the relationship between gdp_per_cap (on the x-axis) and life_exp (on the y-axis).
sns.scatterplot(x='gdp_per_cap', y='life_exp', data=world_happiness)
plt.show()

# Calculate the correlation between gdp_per_cap and life_exp and store as cor.
cor = world_happiness['gdp_per_cap'].corr(world_happiness['life_exp'])
print(cor)

# Transforming variables
"""
*When variables have skewed distributions, they often require a transformation in order to form a linear relationship with another variable so that correlation can be computed. 
"""
# Create a scatterplot of happiness_score versus gdp_per_cap and calculate the correlation between them.
sns.scatterplot(x="gdp_per_cap", y="happiness_score",data=world_happiness)
plt.show()
cor = world_happiness['gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)

# Add a new column to world_happiness called log_gdp_per_cap that contains the log of gdp_per_cap. Create a seaborn scatterplot of happiness_score versus log_gdp_per_cap. Calculate the correlation between log_gdp_per_cap and happiness_score.
world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

sns.scatterplot(x="log_gdp_per_cap", y="happiness_score", data=world_happiness)
plt.show()

cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)

# Does sugar improve happiness?
"""
*A new column has been added to world_happiness called grams_sugar_per_day, which contains the average amount of sugar eaten per person per day in each country. In this exercise, you'll examine the effect of a country's average sugar consumption on its happiness score.
"""
# Create a seaborn scatterplot showing the relationship between grams_sugar_per_day (on the x-axis) and happiness_score (on the y-axis).
sns.scatterplot(x="grams_sugar_per_day", y="happiness_score", data=world_happiness)
plt.show()

# Calculate the correlation between grams_sugar_per_day and happiness_score.
cor = world_happiness['grams_sugar_per_day'].corr(world_happiness['happiness_score'])
print(cor)

# Confounders
"""
*A study is investigating the relationship between neighborhood residence and lung capacity. Researchers measure the lung capacity of thirty people from neighborhood A, which is located near a highway, and thirty people from neighborhood B, which is not near a highway. Both groups have similar smoking habits and a similar gender breakdown.

*What could be a confounder in this study? - Air pollution
"""