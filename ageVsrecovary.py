# Import modules
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("bank_data.csv")
# Import stats module
from scipy import stats

#Compute average age just below & above threshold ($1000)
era_900_1100 = df.loc[(df['expected_recovery_amount']<1100) & 
                      (df['expected_recovery_amount']>=900)]
by_recovery_strategy = era_900_1100.groupby(['recovery_strategy'])
print(by_recovery_strategy['age'].describe().unstack())

# Perform Kruskal-Wallis test
Level_0_age = era_900_1100.loc[df['recovery_strategy']=="Level_0_Age"]['age']
Level_1_age = era_900_1100.loc[df['recovery_strategy']=="Level_1_Age"]['age']
print(stats.kruskal(Level_0_age, Level_1_age))