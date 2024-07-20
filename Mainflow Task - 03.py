import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

data = pd.read_csv("E:\\Main flow Internship data analysis/householdtask3.csv")

print(data.head(10))

# Scatter plot with year against own
plt.scatter(data['year'],data['own'])

# Adding title to the plot
plt.title(" Scattle Plot")

# Setting the X and Y lable
plt.xlabel('year')
plt.ylabel('own')

# Showing the result
plt.show()


# Line Chart
# Line Chart with year against own
plt.plot(data['year'])
plt.plot(data['own'])

# Adding title to the plot
plt.title("Line Chart")

# Setting the X and Y lable
plt.xlabel('year')
plt.ylabel('own')

# Showing the result
plt.show()

#Bar Chart
plt.bar(data['year'],data['own'])

# Adding title to the plot
plt.title("Bar Chart")

# Setting the X and Y lable
plt.xlabel('year')
plt.ylabel('own')

# Showing the result
plt.show()

#Histrogram
plt.hist(data["income"])

# Adding title to the plot
plt.title("Histrogram")

# Showing the result
plt.show()
