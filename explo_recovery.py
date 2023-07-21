# Import modules
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("bank_data.csv")
from matplotlib import pyplot as plt
# Scatterplot: Actual Recovery Amount vs Expected Recovery Amount
plt.scatter(x = df['expected_recovery_amount'], y = df['actual_recovery_amount'], c = "brown", s =2)
plt.xlim(900, 1100) #just below, just above threshold
plt.ylim(0, 2000)
plt.xlabel('Expected Recovery Amount')
plt.ylabel('Actual Recovery Amount')
plt.legend(loc = 2)
plt.show()