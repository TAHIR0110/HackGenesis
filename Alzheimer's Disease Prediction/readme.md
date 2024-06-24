
# Alzheimers Disease Prediction

## 🎯 Goal
The main goal of the model is to accurately predict whether a person diagnosed with Alzheimer's disease or not based on demographic details, lifestyle factors, medical history, clinical measurements, cognitive and functional assessments, symptoms.

## 🧵 Dataset

Here is the link to dataset:

[Link](https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset/data)

## 🧾 Description

In this project, the model is trained with Random Forest Classifier and the accuracy of the model is calculated . The accuracy score turned out to be nearly 92%. To improve the accuracy, RandomizedSearchCV hyperparameter tuning is used and finally accuracy is 94%.

## 🧮 Changes made

1. Downloading Dataset : I have downloaded the dataset using Kaggle API.
2. Importing necessary libraries
3. Summary Statistics: In this section, I have created the summary of the data,EDA.
4. Splitting Training and Testing data: Splitting training and testing data helps to predict the models performance.
5. Model Training: Training the model using `RandomForestClassifier`
6. Hyperparameter Tuning: Tuning the model's hyperparameters using `RandomizedSearchCV`

## 📢 Conclusion

RandomForestClassifier gives better results on this model. By tuning hyperparameters, it gave best results. 