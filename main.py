import seaborn as sns
import matplotlib.pyplot as plt



# Sample dataset
data = [10, 20, 30, 35, 40, 45, 50, 100, 150]  # 100 and 150 are outliers

# Create box plot
sns.boxplot(data=data)

# Show plot
plt.show()


import numpy as np
import pandas as pd

# Sample dataset
data = [5, 10, 15, 20, 25, 30, 35, 40, 100]

# Convert to DataFrame
df = pd.DataFrame(data, columns=["values"])

# Calculate Q1, Q3, and IQR
Q1 = df["values"].quantile(0.25)
Q3 = df["values"].quantile(0.75)
IQR = Q3 - Q1

# Calculate Outlier Boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify Outliers
outliers = df[(df["values"] < lower_bound) | (df["values"] > upper_bound)]

print("Outliers:\n", outliers)

