# Import modules
import pandas as pd
import numpy as np
from scipy import stats
# Load dataset
df = pd.read_csv("bank_data.csv")

#Compute average age just below & above threshold ($1000)
era_900_1100 = df.loc[(df['expected_recovery_amount']<1100) & 
                      (df['expected_recovery_amount']>=900)]
by_recovery_strategy = era_900_1100.groupby(['recovery_strategy'])


# Compute average actual recovery amount just below threshold
by_recovery_strategy['actual_recovery_amount'].describe().unstack()

# perform Kruskal-Wallis
Level_0_actual = era_900_1100.loc[df['recovery_strategy']=='Level 0 Recovery']['actual_recovery_amount']
Level_1_actual = era_900_1100.loc[df['recovery_strategy']=='Level 1 Recovery']['actual_recovery_amount']
print(stats.kruskal(Level_0_actual, Level_1_actual))
