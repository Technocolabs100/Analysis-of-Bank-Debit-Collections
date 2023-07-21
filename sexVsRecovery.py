# Import modules
import pandas as pd
import numpy as np
# Import stats module
from scipy import stats

# Load dataset
df = pd.read_csv("bank_data.csv")
# Number of customers in each category
# Compute the crosstab of sex and recovery_strategy
crosstab = pd.crosstab(df.loc[(df['expected_recovery_amount']<1100) & 
                              (df['expected_recovery_amount']>=900)]['recovery_strategy'], 
                       df['sex'])
crosstab

# Chi-square test
chi2_stat, p_val, dof, ex = stats.chi2_contingency(crosstab)
print('p-val is: ', p_val)