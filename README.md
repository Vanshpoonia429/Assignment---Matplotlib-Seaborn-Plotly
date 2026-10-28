# Assignment---Matplotlib-Seaborn-Plotly
Assignment - Matplotlib | Seaborn | Plotly


Question 1: What is Matplotlib, and why is it used for data visualization in Python? Explain the
difference between plt.plot() and plt.scatter() with suitable examples.

Answer:

Matplotlib is a popular Python library used for data visualization. It helps represent data in graphical forms such as line plots, bar charts, scatter plots, and histograms, It makes data easier to understand and helps identify trends, patterns, and relationships.

Uses of Matplotlib:

It represents data visually using graphs and charts.
It helps identify trends and patterns in datasets.
It allows customization of titles. Labels, colors, and legends.
It is useful for data analysis and presenting results.

Difference between plt.plot() and plt.scatter() ;

plt.plot()  is used to create line plots by connecting data points. It is useful for showing changes and trends over time.

plt.scatter()  is used to create scatter p[lots that display individual data points. It is useful for examining relationships between two variables.

Example of plt.plot() : 

Import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5]
Y = [10, 20, 15, 30, 25]

plt.plot (x, y)
plt.xlabel (“x values”)
plt.ylabel (“y values”)
plt.title (“Line Plot”)
plt.show()


Example of plt.scatter() :

Import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5,]
y = [10, 20, 15, 30, 25]

plt.scatter (x, y, color=’red’)
plt.xlabel (“x values”)
plt.ylabel (“y values”)
plt.title (“Scatter Plot”)
plt.show()


Question 2: What is a Figure and an Axes in Matplotlib? Explain the difference between
plt.subplot() and plt.subplots() with an example.

Answer:

In Matplotlib, a Figure is the entire window or canvas on which plots are displayed, whereas Axes is the ares inside the figure where data is plotted. An axes contains the x-axis, y-axis, title, labels, and plotted data.

Difference between Figure and Axes : 

Figure : It is the overall container that can hold one or more plots.
Axes : It is an individual plotting area within a figure where graphs are drawn.

Difference between plt.subplot() and plt.subplots() : 

plt.subplot() is used to create or select a single subplot within a grid of plots.

plt.subplots()  creates a figure and one or more subplot axes at the same time. It is more convenient when working with multiple plots.

Example of plt.subplot() : 

Import matplotlib.pyplot as plt

plt.subplot(1, 2, 1)
plt.plot ( [1, 2, 3], [10, 20, 30] )
plt.title(“Line Plot”)

plt.subplot (1, 2, 2)
plt.bar ( [1, 2, 3], [10, 20, 30] )
plt.title(“Bar Plot”)

plt.tight_layout()
plt.show()


Example of plt.subplots() : 

Import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2)

ax[0].plot ( [1, 2, 3], [10, 20, 30] )
ax[0].set_title(“Line plot”)

ax[1].bar ( [1, 2, 3], [10, 20, 30] )
ax[1].set-title (“Bar Plot”)

plt.tight_layout()
plt.show()

Question 3: Explain how to customize a line plot in Matplotlib using color, linestyle,
linewidth, marker, and label.

Answer:

In Matplotlib, a line plot can be customized using different parameters to make it more attractive and easier to understand.

The main customization parameters are:

Color : Specifies the color of the line, such as red, blue, or green.
Linestyle : Defines the style of the line, such as solid( ‘-’), dashed (‘--’), or dotted (‘:’).
Linewidth : controls the thickness of the line.
Marker : Specifies the symbol used to represent individual data points, such as circles ( ‘o’ ) or squares ( ‘s’ ).
Label : Assigns a name to the line, which can be displayed using a legend.

Question 4: What is Seaborn, and how is it different from Matplotlib? Explain the concept of
hue in Seaborn plots with a suitable example.

Answer:

Seaborn is a Python data visualization library built on top of matplotlib. It provides a high-level interface for creating attractive and informative statistical graphs. It works well with Pandas DataFrames and makes it easier to visualize relationships and distributions in data.

Difference between Seaborn and Matplotlib 

Matplotlib 								seaborn

A general-purpose data visualization library		A statistical data visualization library built 
							on Matplotlib

Requires more code for complex visualization.	Provides simple functions for statistical								
Offers detailed control over plot customization.	Provides attractive default styles and color 
							palettes.

Works with lists, arrays, and DataFrames.	          Works especially well with Pandas DataFram

Customization is generally more manual.		Supports statistical visualization and 									grouping features easily.


Concept of hue in Seaborn

The hue parameter is used to differentiate data categories by assigning different colors to them in a plot. It helps compare multiple groups within the same visualization.
For example, in a scatter plot of study hours and marks, the hue parameter can assign different colors to students belonging to different classes.


Question 5: Explain the difference between plt.bar() and plt.barh().
Consider the following data:

Answer:

In Matplotlib, plt.bar() and plt.barh() are used to create bar charts for comparing values across different categories.

Difference between plt.bar() and plt.brah():

plt.bar() : Creates a vertical bar chart in which categories are displayed on the x-axis and values on the y-axis.
plt.barh() : Creates a horizontal bar chart in which categories are displayed on the y-axis and values on the x-axis.



Question 6: What is a histogram, and what does its shape tell us about a dataset?

Answer:

A histogram is a graphical representation of the frequency distribution of numerical data. It divides data into intervals called bins and uses bars to show how many values fall within each interval.

The shape of a histogram tells us several things about a dataset : 

Symmetric distribution : Data is distributed evenly around the center.
Skewed distribution : Data is concentrated on one side, with a longer tail on the other.
Uniform distribution : Values occur with approximately equal frequency across intervals.
Normal distribution : The histogram has a bell-shaped curve.
Outliers : isolated bars may indicate unusual values in the dataset.

