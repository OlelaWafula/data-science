import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Saving Visualizations

# Load Data
medals = pd.read_csv("medals.csv", index_col=0)

# Visualize Data
fig, ax = plt.subplots()

ax.bar(medals.index, medals["Gold"])
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel("Number of medals")
fig.savefig("gold_medals.png") # Save the output as an image

# Different file formats
"""
*.png file - the image will retain high quality but will also take up relatively large amount of disk space/ bandwidth. 

*You can choose other file formats depending on your need. e.g. if the image is going to be partof the website you can choose '.jpg' format. i.e. fig.savefig("gold_medals.jpg"). 

* You can also control how small the resulting image will be i.e. the degree of loss of quality by setting the "quality" keyword argument with a number between 1 and 100. But youb should avoid values above 95, because at that point the compression is no longer effective. 

    fig.savefig("gold_medals.jpg", quality=50)


*Choosing the ".svg" file format will produce a vector graphics file where different elements can be added in detail by advanced graphics software such as gip or adobe illustrator. If you need to edit the figure after producing it this might be a good choice. 

    fig.savefig("gold_medals.svg", dpi=300)

*dpi stands for dots per inch. The higher the dpi, the more densely the image will be rendered. If you set dpi=300, this will render a fairly high quality resolution of your image to file. 

*Size of the figure - To contro the figure size you use:

    fig.set_size_inches([5, 3])

    - This function takes a sequence of numbers, the first number sets the width of the figure on the page while the second number sets the height of the figure. 

    - Setting the size will also determine the aspect ratio of the figure. i.e. you can set your figure to be wide and short i.e. 
    fig.set_size_inches([5, 3]) or long and narrow fig.set_size_inches([3, 5])
"""
# EXERCISE 

# Saving a file several times
"""
*If you want to share your visualizations with others, you will need to save them into files. Matplotlib provides as way to do that, through the savefig method of the Figure object. 

*In this exercise, you will save a figure several times. Each time setting the parameters to something slightly different. We have provided and already created Figure object.
"""
# Examine the figure by calling the plt.show() function.
plt.show()

# Save the figure into the file my_figure.png, using the default resolution.
fig.savefig("my_figure.png")

# Save the figure into the file my_figure_300dpi.png and set the resolution to 300 dpi.
fig.savefig("my_figure_300dpi.png", dpi=300)

# Save a figure with different sizes
"""
*Before saving your visualization, you might want to also set the size that the figure will have on the page. 

*To do so, you can use the Figure object's set_size_inches method. This method takes a sequence of two values. The first sets the width and the second sets the height of the figure.

*Here, you will again have a Figure object called fig already provided (you can run plt.show if you want to see its contents). Use the Figure methods set_size_inches and savefig to change its size and save two different versions of this figure.
"""
# Set the figure size as width of 3 inches and height of 5 inches and save it as 'figure_3_5.png' with default resolution.
fig.set_size_inches([3, 5])
fig.savefig("figure_3_5.png")

# Set the figure size to width of 5 inches and height of 3 inches and save it as 'figure_5_3.png' with default settings.
fig.set_size_inches([5, 3])
fig.savefig("figure_5_3.png")



