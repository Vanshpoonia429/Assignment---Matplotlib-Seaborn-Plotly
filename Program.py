Q3. Write a Python program to plot a sine wave using these customizations.

Import numpy as np
Import matplotlib.pyplot as plt

# Generate data for sine wave

x = np.linespace(0, 2 * np.pi, 100)
y = np.sin(x)

# Plot sine wave with customization

plt.plot (
	x, y,
	color = ‘blue’,
	linestyle = ‘--’,
	linewidth = 2,
	marker = ‘o’,
	markevery = 10,
	label = ‘Sine wave’
)

# Add title and labels

plt.title(‘Customized Sine Wave”)
plt.xlabel(“x values”)
plt.ylabel(“sin(x)”)

# Display legend and grid

plt.legend()
plt.grid(True)

# Display the plot

plt.show()

Q4. Explain the concept of hue in Seaborn plots with a suitable example.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create sample dataset

data = pd.DataFrame ({
	‘study_Hours’ : [2, 3, 4, 5, 6, 7],
	‘Marks’ : [40, 50, 55, 65, 75, 85],
	‘Class’ ; [‘A’, ‘A’, ‘B’, ‘B’, ‘A’, ‘B’]
})

# create scatter plot using hue

sns.scatterplot(
	data=data,
	x = ‘Study_Hours’,
	y = ‘Marks’,
	hue = ‘Class’
)

plt.title(“Study Hours vs Marks”)
plt.xlabel(“Study Hours”)
plt.ylabel(“Marks”)
plt.show()

Q5. Write a Python program to create both a vertical and a horizontal bar chart using this data.

categories = ["A", "B", "C", "D"]
values = [23, 17, 35, 29]

import matplotlib.pyplot as plt

# Given data

categories = [“A”, “B”, “C”, “D”]
values = [23, 17, 35, 29]

# Creates vertical bar chart

plt.figure(figsize=(6, 4))
plt.bar(categories, values, color = ‘skyblue’)
plt.title(“Vertical Bar Chart”)
plt.xlabel(“Categories”)
plt.ylabel(“Values’)
plt.show()

# Creates horizontal bar chart

plt.figure(figsize=(6, 4))
plt.barh(categories, values, color=’orange’)
plt.title(“Horizontal Bar Chart”)
plt.xlabel(“Values”)
ple.ylabel(“Categories”)
plt.show()

Q6. Write a Python program to generate 1000 random values using np.random.randn() and plot
a histogram with bins=30.

Import numpy as np
Import matplotlib.pyplot as plt

# generate 1000 random values

data = np.random.randn(1000)

# Plot the histogram

plt.hist(data, bins=30, color=’skyblue’, edgecolor=’black’

# Add title and labels

plt.title(“Histogram of 1000 Random values”)
plt.xlabel(“Value”)
plt.ylabel(“Frequency”)

# Display the histogram

plt.show

Question 7: Consider the following dataset:
sizes = [40, 25, 20, 15]
labels = ["Apples", "Bananas", "Cherries", "Dates"]

Write a Python program to:

1. Create a pie chart showing the percentage share of each fruit.
2. Display the percentages on the chart using autopct.
3. Set the start angle of the pie chart to 120 degrees.
4. Explain why plt.axis("equal") is used in a pie chart.

Answer:

import matplotlib.pyplot as plt

# Given dataset

sizes = [40, 25, 20, 15]
labels = [“Apple”, “Banana”, “Cherries”, “Dates”]

# Creates a pie chart

plt.pie(
	sizes,
	labels=labels,
	autopct=’%1.1f%%’,
	startangle=120
)

# Set equal aspect ratio

plt.axis(“equal”)

# Add title 

plt.title(“Percentage Share of Fruits”)

# Display the chart

plt.show()

Q8. Write a Python program to plot a sine wave and annotate its peak point with an arrow and the
label "Peak".

import numpy as np
import matplotlib.pyplot as plt

# Generate x values

x = np.linspace(0, 2 * np.pi, 100)

# Calculate sine values

y = np.sin(x)

# Plot the sine wave

plt.plot(x, y, label=”Sine Wave”)

# Annotate the peak point

plt.annotate (
	“Peak”,
	xy=(np.pi / 2, 1),
	xytext=(2, 1.3),
	arrowprops=dict(facecolor=’black’, arrowstyle=’->’)
)

# Add title and labels

plt.title(“Sine wave with peak annotation”)
plt.xlabel(“x values”)
plt.ylabel(“Sin(x)”)
plt.legend()

# Display the graph

plt.show()

Question 9: Consider the following list of scores:
scores = [45, 67, 89, 23, 56, 78, 90, 34]

Write a Python program using Seaborn to:

1. Load this list into a DataFrame with the column name "Score".
2. Create a histogram of the scores using sns.histplot().
3. Create a boxplot of the scores using sns.boxplot().
4. Identify any outliers visible in the boxplot.

Answer:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given list of scores

scores = [45, 67, 89, 23, 56, 78, 90, 34]

# Load scores into a DataFrame

df = pd.DataFrame({‘Score’: scores)}

# Create a histogram

sns.histplot(data=df, x=’Score’, bins=5, kde=False)
plt.title(“histogram of scores”)
plt.xlabel(“Score”)
plt.ylabel(“Frequency”)
plt.show()

# create a boxplot

sns.boxplot(data a=df, x=’Score’)
plt.title(“Boxplot of scores”)
plt.xlabel(“Score”)
plt.show()


Question 10: What is Plotly, and how is it different from Matplotlib and Seaborn?
Write a Python program using plotly.express to create an interactive scatter plot for the following
data, and explain one advantage of using Plotly over static plots.
x = [1, 2, 3, 4, 5]
y = [10, 14, 22, 18, 27]

Answer:

Plotly is a Python data visualization library used to create interactive graphs and charts. It allows users to zoom in zoom out, and hover over data points to view their values.

Different between Plotly, Matplotlib, and seaborn

Matplotlib : Used to create basic and highly customizable graphs, such as line charts, bar charts, and histogram
Seaborn : Used to create attractive statical graphs and visualize relationship between data.
Plotly : Used to create interactive graphs and charts that allow user to explore data easily.

Python program : 

import pandas as pd
importantly. Express as px

# Given data

X = [1, 2, 3, 4, 5]
y = [10, 14, 22, 18, 27]

# create a DataFrame 
df = pd.DataFrame ({
	‘X’ : x,,
	‘Y’ : y

# Create an interactive scatter plot

fig = px.scatter (
	df ,
	x=’x’ ,
	y=’Y’,
	title=’Interactive scatter plot’,
labels={‘X’ : ‘X values’, ‘Y’ : “values’}

)

# Display the plot

fig.show()
