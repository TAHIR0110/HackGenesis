# Breast Cancer Prediction :

### Goal:
This Project helps us to build  a model which helps us to detect if a person have breast cancer or not .
The goal of this project is to build an ML model that can accurately classify whether a tumor is benign or malignant based on various features such as texture, perimeter, and compactness.
Breast cancer is a type of cancer that forms in the cells of the breasts.

## Dataset

Content: The dataset used in this project is the Wisconsin Breast Cancer Dataset which ontains features computed from digitized images of breast mass fine needle aspirates, used for binary classification to predict malignant or benign tumors.

### About  model: 
What I have used in the model:

#### Logistic Regression;-
- Logistic regression is a statistical model used for binary classification, predicting probabilities between two classes based on input features.

#### Support Vector Machine:-
- Support Vector Machine (SVM) is a supervised learning algorithm used for classification and regression tasks. It finds the optimal hyperplane that maximally separates data points of different classes in a high-dimensional space.

#### Random Forest Classifier:-
- Random Forest Classifier is an ensemble learning method used for classification tasks. It constructs multiple decision trees during training and outputs the mode of the classes for classification, improving accuracy and controlling overfitting.


## What I have done!
- Load CSV file into DataFrame.
- Get DataFrame's dimensions (rows, columns).
- computes pairwise correlation of columns, excluding NA/null values. 
- Creates a new DataFrame x excluding the "diagnosis" column.
- Creates a count plot of the target variable y.
- create a heatmap of the correlation matrix corr with annotations.
- created an instance of the StandardScaler class from the sklearn.preprocessing module. 
- transform the data in x to a standardized form.
- Splits the data into training and testing sets with a 70-30 ratio.
- Support Vector Machine classifier from scikit-learn was used  to classify the data.
- Logistic Regression classifier from scikit-learn was used to classify the data.
- Random Forest Classifier from scikit-learn was used to classify the data.



## Conclusion:-
This study focuses on the development and evaluation of a breast cancer detection model using machine learning techniques. The model was trained on a dataset consisting of various features such as radius_mean, texture_mean, perimeter_mean, compactness_mean etc..




