# -*- coding: utf-8 -*-
"""Project1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Igohx0H3FRxOMcM6QENrXpGzixQE8Db
"""

#1(a)
import pandas as pd
import numpy as np

# Read the data from csv file
df = pd.read_csv('/content/Crime.csv')

# Display the first 5 rows of the dataframe
print(df.head())

from google.colab import drive
drive.mount('/content/drive')

# 1(b)
df_cleaned = df.dropna(subset=['Dispatch Date / Time']).reset_index(drop=True)

# Drop rows with missing Dispatch Date / Time
df_cleaned = df_cleaned[['Dispatch Date / Time', 'Crime Name1', 'Victims','City']]

# Convert Dispatch Date / Time to datetime format
df_cleaned['Dispatch Date / Time'] = pd.to_datetime(df_cleaned['Dispatch Date / Time'])

import matplotlib.pyplot as plt


# 1c) Show graphs using Matplotlib

# Scatterplot of Victims vs Dispatch Date / Time
plt.scatter(df_cleaned['Dispatch Date / Time'], df_cleaned['Victims'])
plt.title('Number of Victims by Dispatch Date / Time')
plt.xlabel('Dispatch Date / Time')
plt.ylabel('Number of Victims')
plt.show()

# Histogram of Victims
plt.hist(df_cleaned['Victims'], bins=10)
plt.title('Distribution of Number of Victims')
plt.xlabel('Number of Victims')
plt.ylabel('Frequency')
plt.show()

# Boxplot of Victims by City
s=df.loc[df['City']=='Silver Spring','Victims'].values

plt.boxplot([s],labels=['Silver Spring'])
plt.boxplot(df_cleaned['Victims'])
plt.title('Box Plot of Victims by City')
plt.xlabel('City')
plt.ylabel('Number of Victims')

plt.ylim(0, 12)
plt.show()

# 1d) Use nonparametric inference for the median of a continuous variable using bootstrap simulation
n_simulations = 1000  # Number of bootstrap simulations
medians = []  # Store the medians from each simulation

# Perform bootstrap simulations
for _ in range(n_simulations):
    bootstrap_sample = np.random.choice(df_cleaned['Victims'], size=len(df_cleaned), replace=True)
    medians.append(np.median(bootstrap_sample))

# Calculate the bootstrap 95% confidence interval for the median
lower_ci = np.percentile(medians, 2.5)
upper_ci = np.percentile(medians, 97.5)

print(f"Bootstrap 95% Confidence Interval for the Median: [{lower_ci}, {upper_ci}]")