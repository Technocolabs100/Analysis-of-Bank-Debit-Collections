
# CORPORTATE BANKRUPTCY PREDICTION

This is Internship Project For Technocolabs Software. The goal of the project is to identify the best classification model in terms of accuracy and performance for predicting the bankruptcy of corporations using various statistical forecasting techniques like Logistic Regression, LightBGM, Neural Network and Random Forest Classifier. Deploy ML model using AWS.



## PROCESS OF PROJECT

- BLUEPRINT 
-  EDA
- MODEL DEVELOPMENT
- DEPLOYMENT OF ML MODEL


## 🔗 Links for Respective Project Works

## 🚀 About Me
hi, my name is Sivaprasad V
I'm a Data Science Enthusiast.
I am interested in Business Analytics and Market Research as well as Predictve Finance Analysis.
I am skilled in Python Language, Data Science and ML , Data Visualisation and Keras/ Tensorflow, Stramlit and Business Analytics. 



Summary:
Bankruptcy prediction is the task of predicting bankruptcy and various measures of financial distress of firms, and is important due to the relevance for creditors and investors in evaluating the likelihood that a firm may go bankrupt.

The aim of predicting financial distress is to develop a predictive model that combines various econometric parameters which allow foreseeing the financial condition of a firm. In this project we document our observations as we explore, build, and compare, some of the widely used classification models:

Gaussian Naïve Bayes
Logistic Regression
Decision Trees
Random Forests
Extreme Gradient Boosting
Balanced Bagging
We have chosen the Polish companies’ bankruptcy data set where synthetic features were used to reflect higher-order statistics.

We begin by carrying out data preprocessing and exploratory analysis where we impute the missing data values using some of the popular data imputation techniques like Mean, k-Nearest Neighbors, Expectation-Maximization and Multivariate Imputation by Chained Equations (MICE).

To address the data imbalance issue, we apply Synthetic Minority Oversampling Technique (SMOTE) to oversample the minority class labels.

Later, we model the data using K-Fold Cross Validation on the said models, and the imputed and resampled datasets.

Finally, we analyze and evaluate the performance of the models on the validation datasets using several metrics such as accuracy, precision, recall, etc., and rank the models accordingly.  


# Exploratory Data Analysis (EDA) for 5-Year Bankruptcy Prediction

**Introduction:**

- The dataset, originally comprised of stock data, has been transformed into a 5-year bankruptcy prediction dataset.
- This dataset now contains 43,405 rows and 65 columns, making it a valuable resource for bankruptcy prediction modeling.
- The dataset includes a mix of continuous and float data types, with various features used for predicting bankruptcy outcomes.
This EDA will help us gain insights into the dataset's characteristics and prepare for building effective bankruptcy prediction models. 



**Univariate Analysis for 5-Year Bankruptcy Prediction:**

In this section, we delve into the characteristics of the 5-year bankruptcy prediction dataset to gain a deeper understanding of its individual variables.

- **Histograms**: We begin by plotting histograms for each column to visualize the distribution of data. These histograms provide insights into the data's skewness, central tendency, and potential outliers.

- **Variable Distribution**: Through our analysis, we have observed that while some variables exhibit a roughly normal distribution, others may deviate significantly. This diversity in distribution highlights the complexity of the data.

- **Feature Significance**: Determining which variables are most relevant for bankruptcy prediction is a crucial step. While some features, such as Subjectivity and Polarity, are derived from sentiment analysis, our focus extends to understanding how both historical stock variables and derived features relate to the bankruptcy prediction task.

This univariate analysis forms the foundation for subsequent multivariate and predictive modeling steps. It assists us in identifying key features that could play a vital role in forecasting bankruptcy events over a 5-year horizon. 


Logistic Regression
Logistic Regression is a valuable tool for modeling the probability of a binary outcome, such as predicting whether a company will go bankrupt within a 5-year period.
The logistic regression function is defined as: P(y) = 1 / (1 + e^-(A + Bx)), where:
P(y) represents the probability of bankruptcy.
A is the intercept, and B is the regression coefficient, which are determined during model training.
x represents the features used in the model.
In the context of bankruptcy prediction, logistic regression aims to identify the best-fit S-curve that captures the relationship between input features and the likelihood of bankruptcy. The output of logistic regression is a probability score, which can be used to classify companies as at risk of bankruptcy or not.
Random Forest Classifier
The Random Forest Classifier is a powerful ensemble learning algorithm for 5-year bankruptcy prediction.
Instead of a single decision tree, it combines the predictions of many decision trees. Each tree is built on a different subset of the data (bagging) and with feature randomness (random feature selection), resulting in a collection of diverse, uncorrelated trees.
This ensemble approach helps mitigate overfitting and improves prediction accuracy.
For 5-year bankruptcy prediction, the Random Forest Classifier leverages the collective wisdom of multiple decision trees to make more accurate and robust predictions about whether a company is likely to face bankruptcy in the future.
In the context of 5-year bankruptcy prediction, both Logistic Regression and Random Forest Classifier are valuable techniques for building models that can inform financial decision-making and risk assessment. These models help stakeholders make informed choices about investments and business partnerships. 


When we apply the **logistic regression** model the accuracyb was 97%.
When we apply **random forest** model the accuracy was 95%.

## Deployment

Bankruptcy-Prediction-using-Pyspark-Python-and-AWS-


This project uses the Pyspark , Map reduce , Python to evaluate  machine learning models like logistic regression , Decision Tree, Random Forest , Gradient Boosting Tree
We evaluated the best model that will suit our model based upon the Model analysis , Evaluation Metrics , Parallelisim and Scalability , Hyperparameter tuning and Feature selection. We did build the ML pipe line by perfroming EDA of the dataset and then implementing imputing , scaler assembling and smote analysis . The data was feeded into it by partition and caching . Further more to reduce the dimentinality reduction by PCA we again repartioned it . More over after every model was training we did perform unpersist so as to free the memory and see good results of parallesim . Further more this model was deployed over the AWS EMR service which is meant to support the deployment of Machine learning models using Spark , hadoop , etc. 


