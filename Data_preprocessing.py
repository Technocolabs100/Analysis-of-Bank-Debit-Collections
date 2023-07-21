# Import modules
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("bank_data.csv")

# Look at first few rows of dataset
print(df.head())
# get the number of missing data points per column
missing_values_count = df.isnull().sum()

# look at the # of missing points in the first ten columns
print(missing_values_count[0:10])
