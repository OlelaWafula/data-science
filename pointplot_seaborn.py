import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Point plots
"""
*Show the mean of quantitative variable for the observations in each category.
Vertical bars extending above and below the mean represent the 95% conficence levels for that mean.

*Point v Line plots
    Both show
        . mean of quantitative variable 
        .95% confidence intervals for the mean.
    Difference:
        .Line plots are relational plots (both x and y are quantitative variables).
        .Point plot one axis (usually x - axis) is a categorical variable making it a categorical plot.

*Point v Bar plots
    Both show
        .Mean of quantitative varoable
        . 95% confidence intervals for the mean.

"""
# Load Data
masculinity_data = sns.load_dataset("masculinity_data")
tips = sns.load_dataset("tips")

# Point plot 
sns.catplot(x="age", y="masculinity_importatnt", data=masculinity_data, hue="feel_masculine", kind="point")
plt.show()

# To remove the lines joining groups set the join parameter to False
sns.catplot(x="age", y="masculinity_importatnt", data=masculinity_data, hue="feel_masculine", kind="point", join="False")
plt.show()

# Displaying the mean
sns.catplot(x="smoker", y="total_bill", data=tips, kind="point")
plt.show()

# To dispaly median set estimator parameter to median - used when dataset has a lot of outliers.
sns.catplot(x="smoker", y="total_bill", data=tips, kind="point", estimator=np.median)
plt.show()

# Customizing confidence intervals
sns.catplot(x="smoker", y="total_bill", data=tips, kind="point", capsize=0.2)
plt.show()

# Turning off confidence intervals 
sns.catplot(x="smoker", y="total_bill", data=tips, kind="point", ci=None)
plt.show()

# EXERCISE 

# Load dataset
student_data = sns.load_dataset("student_data")

# Customizing point plots
"""
*Let's continue to look at data from students in secondary school, this time using a point plot to answer the question: does the quality of the student's family relationship influence the number of absences the student has in school? Here, we'll use the "famrel" variable, which describes the quality of a student's family relationship from 1 (very bad) to 5 (very good).
"""
# Use sns.catplot() and the student_data DataFrame to create a point plot with "famrel" on the x-axis and number of absences ("absences") on the y-axis.
sns.catplot(x="famrel", y="absences", data=student_data, kind="point")
plt.show()

# Add "caps" to the end of the confidence intervals with size 0.2.
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point", capsize=0.2)
plt.show()

# Remove the lines joining the points in each category.
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2, join=False)
plt.show()
"""
While the average number of absences is slightly smaller among students with higher-quality family relationships, the large confidence intervals tell us that we can't be sure there is an actual association here.
"""
# Point plots with subgroups
"""
*Let's continue exploring the dataset of students in secondary school. This time, we'll ask the question: is being in a romantic relationship associated with higher or lower school attendance? And does this association differ by which school the students attend? Let's find out using a point plot.
"""
# Use sns.catplot() and the student_data DataFrame to create a point plot with relationship status ("romantic") on the x-axis and number of absences ("absences") on the y-axis. Color the points based on the school that they attend ("school").
sns.catplot(x="romantic", y="absences", data=student_data, kind="point", hue="school")
plt.show()

# Turn off the confidence intervals for the plot.
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school", ci=None)
plt.show()

# Since there may be outliers of students with many absences, use the median function that we've imported from numpy to display the median number of absences instead of the average.
sns.catplot(x="romantic", y="absences",
			data=student_data,       kind="point",        hue="school", ci=None, estimator=np.median)
plt.show()
"""
It looks like students in romantic relationships have a higher average and median number of absences in the GP school, but this association does not hold for the MS school.
"""