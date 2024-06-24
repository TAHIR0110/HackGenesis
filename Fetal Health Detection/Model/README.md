# Fetal Health Classification Using CTG data

## 🎯 Goal
The goal of this project is to classify fetal health using Cardiotocography (CTG) data. We aim to build machine learning models to predict the health status of fetuses based on various medical features.

## 🧵 Dataset
The dataset used in this project is from Kaggle, containing CTG data for fetal health classification.
Link: https://www.kaggle.com/datasets/andrewmvd/fetal-health-classification/data

## 🧾 Description
Cardiotocography (CTG) is a technical means of recording the fetal heartbeat and the uterine contractions during pregnancy. The dataset contains measurements and the classification of fetal health into three classes: Normal, Suspect, and Pathological.

## 🧮 What I had done!
This project involves the following steps:

1. **Data Exploration:**
I started by loading the dataset and performing an initial exploration to understand its structure and contents. This included checking the shape of the dataset, identifying any missing values, and summarizing the statistics of each feature.

2. **Data Visualization:**
To gain insights into the data distribution and relationships between features, I created several visualizations:
    - Histograms: Displayed the distribution of each feature.
    - Correlation Matrix: Visualized the correlations between features to identify any strong linear relationships.
    - Target Variable Distribution: Showed the distribution of the target variable 'fetal_health' to understand class imbalances.
3. **Data Preprocessing:**
Before training the models, I performed data preprocessing:
    - Feature and Target Separation: Separated the features (X) from the target variable (y).
    - Standardization: Standardized the features using StandardScaler to ensure all features have a mean of 0 and a standard deviation of 1, which is crucial for the performance of many machine learning algorithms.
    - Train-Test Split: Split the data into training and testing sets (80% training, 20% testing) using stratified sampling to maintain the same proportion of classes in both sets.
4. **Model Training and Evaluation:**
I trained four different machine learning models to classify fetal health status and evaluated their performance:
    - Logistic Regression: Trained a logistic regression model, evaluated using classification report, confusion matrix, and various error metrics (MAE, MSE, RMSE, MAPE).
    - Decision Tree Classifier: Trained a decision tree classifier, evaluated using the same metrics.
    - Random Forest Classifier: Trained a random forest classifier, evaluated using the same metrics.
    - Gradient Boosting Classifier: Trained a gradient boosting classifier, evaluated using the same metrics.
For each model, I calculated and reported the accuracy, precision, recall, F1-score, confusion matrix, and error metrics to compare their performance.

5. **Model Performance Visualization:**
To visually compare the performance of the models, I created an interactive bar plot using Plotly, which displays the accuracy of each model with hover tooltips.
![image](https://github.com/abckhush/ThereForYou/assets/127378920/a0936d73-d27f-4845-926a-abeb9eb45495)


## 📚 Libraries Needed
1. numpy
2. pandas
3. seaborn 
4. matplotlib.pyplot
5. plotly.graph_objects
6. sklearn

## 📈 Performance of the Models based on the Accuracy Scores
| Models      |       Accuracy Scores|
|------------ |------------|
|Logistic Regression| 91.08%|
|Decision Tree|	92.02%|
|Random Forest|	95.77%|
|Gradient Boosting|	95.54%|

## 📢 Conclusion
The RandomForestClassifier performed the best among all the models with an accuracy of 95.77%. This project demonstrates how machine learning models can be used to classify fetal health status using CTG data.

## ✒️ Your Signature
1. Name- Khushi Kalra
2. Github- https://github.com/abckhush
3. Role- GSSoC'24 Contributor
