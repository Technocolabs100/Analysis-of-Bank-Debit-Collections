# Import modules
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("bank_data.csv")
# Scatterplot: Age vs Expected Recovery Amount
from matplotlib import pyplot as plt
plt.scatter(x = df['expected_recovery_amount'], y = df['age'], c = 'brown', s = 2)
plt.xlim(0, 2000) #limit exp recov amount to $2000
plt.ylim(0, 60) #to avoid non-data whitespace
plt.xlabel('Expected Recovery Amount')
plt.ylabel('Age')
plt.legend(loc = 2)
plt.show()