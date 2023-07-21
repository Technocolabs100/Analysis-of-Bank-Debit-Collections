import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats 
import statsmodels.api as sm 

#Graphical exploratory data analysis
# Read the data from the CSV file
data=pd.read_csv("C:/Users/zaitb/Downloads/bank_data.csv")

# Filter data for Expected Recovery Amounts between $0 and $2000
small_window_data = data[(data['expected_recovery_amount'] >= 0) & (data['expected_recovery_amount'] <= 2000)]

# Scatter plot for the small window data
plt.figure(figsize=(8, 6))
plt.scatter(small_window_data['expected_recovery_amount'], small_window_data['age'])

# Add labels and title
plt.xlabel("Expected Recovery Amount ($)")
plt.ylabel("Customer Age")
plt.title("Customer Age vs. Expected Recovery Amount (0 to $2000)")

# Show the plot
plt.grid(True)
plt.show()

#Statistical test: age vs. expected recovery amount
# Filter data for Expected Recovery Amounts between $900 and $1100 window 1
below_threshold_data_1 = data[(data['expected_recovery_amount'] >= 900) & (data['expected_recovery_amount'] < 1000)]
above_threshold_data_1 = data[(data['expected_recovery_amount'] >= 1000) & (data['expected_recovery_amount'] <= 1100)]

# Calculate the average age for each group
avg_age_below = below_threshold_data_1['age'].mean()
avg_age_above = above_threshold_data_1['age'].mean()

# Print the results
print("Average Age of Customers Below $1000 Threshold:", avg_age_below)
print("Average Age of Customers Above $1000 Threshold:", avg_age_above)

#Statistical test: sex vs. expected recovery amount

# Calculate the number of male customers in each group
below_threshold_male_count = below_threshold_data_1[below_threshold_data_1['sex'] == 'Male']['sex'].count()
above_threshold_male_count = above_threshold_data_1[above_threshold_data_1['sex'] == 'Male']['sex'].count()

male_below = below_threshold_male_count*100 / below_threshold_data_1['sex'].count()
male_above = above_threshold_male_count*100 / above_threshold_data_1['sex'].count() 

print("the pourcentage of male customers Below $1000 Threshold:", male_below)
print("the pourcentage of male customers Above $1000 Threshold:", male_above)

#Exploratory graphical analysis: recovery amount

# Filter data for Expected Recovery Amounts between $900 and $1100
threshold_data = data[(data['expected_recovery_amount'] >= 900) & (data['expected_recovery_amount'] <= 1100)]

# Scatter plot for Expected vs. Actual Recovery Amount
plt.figure(figsize=(8, 6))
plt.scatter(threshold_data['actual_recovery_amount'],threshold_data['expected_recovery_amount'])

# Add labels and title
plt.xlabel("Expected Recovery Amount ($)")
plt.ylabel("Actual Recovery Amount ($)")
plt.title("Expected Recovery Amount vs. Actual Recovery Amount (Range: $900 to $1100)")

# Add a vertical line at the $1000 threshold
plt.axvline(x=1000, color='red', linestyle='--', label="Threshold at $1000")

# Show the plot
plt.legend()
plt.grid(True)
plt.show()


# Split the data into two groups based on the threshold for Window 2 (950$-1050$)
below_threshold_data_2 = data[(data['expected_recovery_amount'] >= 950) & (data['expected_recovery_amount'] < 1000)]
above_threshold_data_2 = data[(data['expected_recovery_amount'] >= 1000) & (data['expected_recovery_amount'] <= 1050)]

# Perform the Kruskal-Wallis test for each window
kw_statistic_window1, p_value_window1 = stats.kruskal(below_threshold_data_1['actual_recovery_amount'], above_threshold_data_1['actual_recovery_amount'])
kw_statistic_window2, p_value_window2 = stats.kruskal(below_threshold_data_2['actual_recovery_amount'], above_threshold_data_2['actual_recovery_amount'])

# Print the results
print("Kruskal-Wallis Test Results for Window 1 ($900 to $1100):")
print("Kruskal-Wallis Statistic:", kw_statistic_window1)
print("P-Value:", p_value_window1)

print("\nKruskal-Wallis Test Results for Window 2 ($950 to $1050):")
print("Kruskal-Wallis Statistic:", kw_statistic_window2)
print("P-Value:", p_value_window2)

# Interpret the results
alpha = 0.05
if p_value_window1 < alpha:
    print("There is a significant discontinuity in actual recovery amount for Window 1.")
else:
    print("There is no significant discontinuity in actual recovery amount for Window 1.")

if p_value_window2 < alpha:
    print("There is a significant discontinuity in actual recovery amount for Window 2.")
else:
    print("There is no significant discontinuity in actual recovery amount for Window 2.")



#Regression modeling: no threshold

# Create the linear regression model for the first model (without threshold)
X = sm.add_constant(below_threshold_data_1['expected_recovery_amount'])  # Add a constant term for the intercept
y = below_threshold_data_1['actual_recovery_amount']

model_below = sm.OLS(y, X).fit()

# Print the model summary
print(model_below.summary())

# Scatter plot of actual vs. expected recovery amount for below threshold data
plt.figure(figsize=(8, 6))
plt.scatter(below_threshold_data_1['expected_recovery_amount'], below_threshold_data_1['actual_recovery_amount'], color='blue', label='Below Threshold')

# Plot the regression line
plt.plot(below_threshold_data_1['expected_recovery_amount'], model_below.fittedvalues, color='red', label='Regression Line')

# Add labels and title
plt.xlabel("Expected Recovery Amount ($)")
plt.ylabel("Actual Recovery Amount ($)")
plt.title("Actual Recovery Amount vs. Expected Recovery Amount (Below Threshold)")

# Show the plot
plt.legend()
plt.grid(True)
plt.show()




# Create the linear regression model for above threshold data
X_above = sm.add_constant(above_threshold_data_1['expected_recovery_amount'])  # Add a constant term for the intercept
y_above = above_threshold_data_1['actual_recovery_amount']

model_above = sm.OLS(y_above, X_above).fit()

# Print the model summary for above threshold data
print("\nModel Summary - Above Threshold:")
print(model_above.summary())

# Scatter plot of actual vs. expected recovery amount for above threshold data
plt.scatter(above_threshold_data_1['expected_recovery_amount'], above_threshold_data_1['actual_recovery_amount'], color='green', label='Above Threshold')

# Plot the regression line for above threshold data
plt.plot(above_threshold_data_1['expected_recovery_amount'], model_above.fittedvalues, color='orange', label='Regression Line (Above Threshold)')

# Add labels and title
plt.xlabel("Expected Recovery Amount ($)")
plt.ylabel("Actual Recovery Amount ($)")
plt.title("Actual Recovery Amount vs. Expected Recovery Amount")
# Show the plot
plt.legend()
plt.grid(True)
plt.show()

# Plot the regression lines for below and above threshold
plt.plot(below_threshold_data_1['expected_recovery_amount'], model_below.fittedvalues, color='red', label='Regression Line (Below Threshold)')
plt.plot(above_threshold_data_1['expected_recovery_amount'], model_above.fittedvalues, color='orange', label='Regression Line (Above Threshold)')

# Add labels and title
plt.xlabel("Expected Recovery Amount ($)")
plt.ylabel("Actual Recovery Amount ($)")
plt.title("Actual Recovery Amount vs. Expected Recovery Amount (With Threshold)")

# Add a vertical line at the $1000 threshold
# Show the plot
plt.legend()
plt.grid(True)
plt.show()




# Create the linear regression model for the first model (without threshold)
X = sm.add_constant(below_threshold_data_2['expected_recovery_amount'])  # Add a constant term for the intercept
y = below_threshold_data_2['actual_recovery_amount']

model_below = sm.OLS(y, X).fit()

# Print the model summary
print(model_below.summary())

# Scatter plot of actual vs. expected recovery amount for below threshold data
plt.figure(figsize=(8, 6))
plt.scatter(below_threshold_data_2['expected_recovery_amount'], below_threshold_data_2['actual_recovery_amount'], color='blue', label='Below Threshold')

# Plot the regression line
plt.plot(below_threshold_data_2['expected_recovery_amount'], model_below.fittedvalues, color='red', label='Regression Line')

# Add labels and title
plt.xlabel("Expected Recovery Amount ($)")
plt.ylabel("Actual Recovery Amount ($)")
plt.title("Actual Recovery Amount vs. Expected Recovery Amount (Below Threshold)")

# Show the plot
plt.legend()
plt.grid(True)
plt.show()




# Create the linear regression model for above threshold data
X_above = sm.add_constant(above_threshold_data_2['expected_recovery_amount'])  # Add a constant term for the intercept
y_above = above_threshold_data_2['actual_recovery_amount']

model_above = sm.OLS(y_above, X_above).fit()

# Print the model summary for above threshold data
print("\nModel Summary - Above Threshold:")
print(model_above.summary())

# Scatter plot of actual vs. expected recovery amount for above threshold data
plt.scatter(above_threshold_data_2['expected_recovery_amount'], above_threshold_data_2['actual_recovery_amount'], color='green', label='Above Threshold')

# Plot the regression line for above threshold data
plt.plot(above_threshold_data_2['expected_recovery_amount'], model_above.fittedvalues, color='orange', label='Regression Line (Above Threshold)')

# Add labels and title
plt.xlabel("Expected Recovery Amount ($)")
plt.ylabel("Actual Recovery Amount ($)")
plt.title("Actual Recovery Amount vs. Expected Recovery Amount")
# Show the plot
plt.legend()
plt.grid(True)
plt.show()

# Plot the regression lines for below and above threshold
plt.plot(below_threshold_data_2['expected_recovery_amount'], model_below.fittedvalues, color='red', label='Regression Line (Below Threshold)')
plt.plot(above_threshold_data_2['expected_recovery_amount'], model_above.fittedvalues, color='orange', label='Regression Line (Above Threshold)')

# Add labels and title
plt.xlabel("Expected Recovery Amount ($)")
plt.ylabel("Actual Recovery Amount ($)")
plt.title("Actual Recovery Amount vs. Expected Recovery Amount (With Threshold)")

# Add a vertical line at the $1000 threshold
# Show the plot
plt.legend()
plt.grid(True)
plt.show()


