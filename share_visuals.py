import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load Data 
seattle_weather = pd.read_csv('seattle_weather.csv', index_col=0)
austin_weather = pd.read_csv('austin_weather.csv', index_col=0)

# Changing Plot Style
fig, ax = plt.subplots()

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
ax.set_xlabel("Time (months)")
ax.set_ylabel("Average temperature (Fahrenheit degrees)")
plt.show()

# Choosing a style - use ggplot style of the R - Library
plt.style.use("ggplot")
fig, ax = plt.subplots()

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
ax.set_xlabel("Time (months)")
ax.set_ylabel("Average temperature (Fahrenheit degrees)")
plt.show()

"""
*Note - This style will apply to all of the figures in this session until you change it by choosing another style.
*For example, to go back to the default style, you run:

        plt.style.use("default")

8To view others styles use this link https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html 

OR view style_sheets_reference.py file. 
"""
# Guidelines for choosing style
"""
*Dark backgrounds are generally discouraged because they are less visible. Only use them if you have a good reason to do so.

*If colors are important, consider using a color-blind friendly style suchas 'seabor-colorblind' or 'tableau-colorblind10'. These are designed to retain color differences even if viewed by color blind individuals.

*If the reports/figures of your visuals will be printed consider using less ink. i.e. Avoid colored backgrounds. 

If the printer used is likely to be black-and-white, consider using the "grayscale" style. Because it will retain the differences on screen when printed out in a black-and-white printer. 
"""

# EXERCISE 

# Selecting a style for printing
"""
*You are creating a figure that will be included in a leaflet printed on a black-and-white printer. What style should you choose for your figures? - plt.style.use("grayscale")
"""
# Switching between styles
"""
*Selecting a style to use affects all of the visualizations that are created after this style is selected.

*Here, you will practice plotting data in two different styles. The data you will use is the same weather data we used in the first lesson: you will have available to you the DataFrame seattle_weather and the DataFrame austin_weather, both with records of the average temperature in every month.
"""
# Select the 'ggplot' style, create a new Figure called fig, and a new Axes object called ax with plt.subplots.

plt.style.use("ggplot")
fig, ax = plt.subplots()

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()

# 'Solarize_Light2' style, create a new Figure called fig, and a new Axes object called ax with plt.subplots.
plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()