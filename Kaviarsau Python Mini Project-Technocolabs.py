#!/usr/bin/env python
# coding: utf-8

# # Assignment- Mini project -Technocolabs
# 

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df=pd.read_csv(r"C:\Users\Tesla\Downloads\bank_data.csv")


# In[5]:


df.head(10)


# In[12]:


df.isnull().sum()


# In[13]:


df.info()


# In[14]:


df.describe()


# In[19]:


sns.displot(df.expected_recovery_amount)


# In[20]:


sns.displot(df.actual_recovery_amount)


# # Graphical exploratory data analysis

# In[33]:


plt.scatter(x=df.actual_recovery_amount,y=df.age,c='g',s=4)
plt.show
plt.xlim(0,5000)


# In[32]:


plt.scatter(x=df.actual_recovery_amount,y=df.age,c='g',s=4)
plt.xlim(0,2000)
plt.ylim(0,100)
plt.xlabel("Bank Expected recovery amount")
plt.ylabel("Customer_Age")
plt.show()


# In[24]:


plt.scatter(x=df.expected_recovery_amount,y=df.age,c='g',s=4)
plt.show


# # Statistical test: age vs. expected recovery amount 

# In[38]:


plt.scatter(x=df.actual_recovery_amount,y=df.age,c='g',s=10)
plt.xlim(900,1100)
plt.ylim(0,100)
plt.xlabel("Bank Expected recovery amount")
plt.ylabel("Customer_Age")
plt.show()


# # Statistical test: sex vs. expected recovery amount

# In[57]:


minrange=900
maxrange=1100
df_rangefilt = df[(df['expected_recovery_amount'] >= minrange) & (df['expected_recovery_amount'] <= maxrange)]
df_rangefilt


# In[58]:


male=len(df_rangefilt[df_rangefilt.sex=='Male'])
malepercent=male/len(df_rangefilt) *100
print("total_male_percent=",malepercent)


# In[59]:


female=len(df_rangefilt[df_rangefilt.sex=='Female'])
femalepercent=female/len(df_rangefilt) *100
print("total_female_percent=",femalepercent)


# In[56]:


df_rangefilt[df_rangefilt.sex=='Male'].shape[0]


# # Exploratory graphical analysis: recovery amount

# In[63]:


plt.scatter(x=df['actual_recovery_amount'],y=df['expected_recovery_amount'],c="g",s=20)
plt.xlim(0,2000)
plt.ylim(900,1100)
plt.xlabel("Actual recovery amount in bank")
plt.ylabel("Expected recovery amount in bank")
plt.show()


# # Statistical analysis: recovery amount 

# In[64]:


from scipy.stats import kruskal
data_rangefilter = df[(df['expected_recovery_amount'] >= 900) & (df['expected_recovery_amount'] <= 1100)]
groups = data_rangefilter.groupby('actual_recovery_amount')['expected_recovery_amount'].apply(list)
statistic, pvalue = kruskal(*groups)
print("statistic:", statistic)
print("p-value:", pvalue)


# In[70]:


data_rangefilter = df[(df['expected_recovery_amount'] >= 950) & (df['expected_recovery_amount'] <= 1050)]
groups = data_rangefilter.groupby('actual_recovery_amount')['expected_recovery_amount'].apply(list)
statistic, pvalue = kruskal(*groups)
print("statistic:", statistic)
print("p-value:", pvalue)


# In[ ]:





# In[ ]:




