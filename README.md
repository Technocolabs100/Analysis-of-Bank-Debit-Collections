# Which Debts Are Worth the Bank's Effort?

## Project Description

In this data science project, we play the role of a bank data scientist and use regression discontinuity to determine if the bank's recovery strategies for charged-off debts are effective. After a debt is declared "uncollectable," the bank still aims to recover some of the owed money. The bank assigns delinquent customers to different recovery strategies based on their expected recovery amount, which is the estimated amount the bank believes it can receive from the customer in the future.

The recovery strategies are implemented at different expected recovery amount thresholds, such as $1000, $2000, etc. The higher the expected recovery amount, the more effort the bank puts into contacting the customer and obtaining payments. However, each additional level of recovery strategy incurs an extra cost of $50 per customer.

The main question we aim to answer is whether the additional amount recovered at the higher strategy level exceeds the extra $50 in costs. To analyze this, we will use regression discontinuity, a method that helps us understand if there is a significant "jump" or "discontinuity" in the amount recovered at the higher strategy level.

## Project Tasks:

### 1. Regression Discontinuity: Banking Recovery
We start by understanding the bank's recovery strategies and how they are implemented based on the expected recovery amount of the customers.

### 2. Graphical Exploratory Data Analysis
We will explore the data graphically and focus on the first transition between Level 0 and Level 1 recovery strategies. This transition occurs at the $1000 expected recovery amount threshold.

### 3. Statistical Test: Age vs. Expected Recovery Amount
We want to ensure that other factors, such as age and sex, do not show significant jumps across the $1000 threshold. This is important to attribute differences in the actual recovery amount to the higher recovery strategy and not other factors.

### 4. Statistical Test: Sex vs. Expected Recovery Amount
Similar to age, we will test if the percentage of male customers shows a significant jump across the $1000 threshold.

### 5. Exploratory Graphical Analysis: Recovery Amount
Now, we focus on the actual recovery amount and develop scatter plots to examine if there is a discontinuity around the $1000 threshold.

### 6. Statistical Analysis: Recovery Amount
We will perform statistical tests using the Kruskal-Wallis test to determine if there is a significant difference in the actual recovery amount just above and just below the $1000 threshold.

### 7. Regression Modeling: No Threshold
We will build a regression model to estimate the impact of the program without considering the threshold.

### 8. Regression Modeling: Adding True Threshold
In this step, we include an indicator of the true threshold in the regression model to examine the impact of the higher recovery strategy.

### 9. Regression Modeling: Adjusting the Window
To ensure the robustness of our results, we will repeat the regression analysis using a slightly larger and slightly smaller window for the expected recovery amount.

By the end of this project, we will have valuable insights into whether the bank's higher recovery strategies are worth the additional costs and if there is a significant jump in the actual recovery amount at the $1000 threshold.

## Libraries Used

- Python
  - NumPy
  - Pandas
  - Matplotlib
  - Seaborn
  - Statsmodels

## Conclusion

By analyzing the data and performing regression discontinuity, we will be able to provide concrete evidence on the effectiveness of the bank's recovery strategies and whether the incremental amount recovered justifies the additional costs. This analysis technique can be applied in various fields, such as medicine, education, finance, and the public sector, whenever threshold assignments are made.

Feel free to explore the Jupyter notebooks and data files in this repository to understand the step-by-step process of this data science project. For any questions or suggestions, please don't hesitate to reach out!

Happy analyzing!
