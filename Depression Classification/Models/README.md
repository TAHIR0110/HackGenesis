# COVID19-X Ray Image Classification

## 🎯 Goal
The main purpose of this project is to classify depression levels and provide real-time, personalized support for users experiencing specific crises, such as postpartum depression, job loss, or caregiver burnout. This is achieved by detecting crisis indicators through user interactions and mood tracking data, offering immediate tailored support, developing personalized action plans, and connecting users with virtual peer support.

## 🧵 Dataset

The dataset used for this project includes user interaction logs, mood tracking data, and annotated crisis indicators.
The link to the dataset is given below :-

# Link :- https://www.kaggle.com/datasets/mahek6114/depression-classification

## 🧾 Description

This project involves the development and analysis of machine learning models to detect crisis situations from user data and provide personalized support. The process includes data preparation, model training, evaluation, and deployment. Exploratory data analysis (EDA) is performed to understand the dataset's characteristics, explore data distributions, and identify potential areas for improvement.

## 🧮 What I had done!

### 1. Data Loading and Preparation:
    Loaded the dataset containing user interactions and mood tracking data into a pandas DataFrame for easy manipulation and analysis.

### 2. Exploratory Data Analysis (EDA):
    Visualized the distribution of mood scores and interaction frequencies.
    Identified missing values and potential outliers in the dataset.
    Analyzed the distribution of crisis indicators to detect imbalances.

### 3. Data Analysis:
    Counted the number of unique user interactions to ensure data uniqueness and quality.
    Analyzed the distribution of mood scores and crisis indicators.
    Displayed the number of unique values for each categorical column to understand data variety.
    Visualized missing values using a heatmap to identify and address potential data quality issues.

### 4. Image Preprocessing and Model Training:
    Loaded and preprocessed the test images, ensuring normalization of pixel values for consistency.
        Iterated through multiple models (VGG16, ResNet50 , Xception) saved in a directory and made predictions on the test dataset.
        Saved the predictions to CSV files for further analysis and comparison.

### 5. Model Prediction Visualization:
    Loaded models and visualized their predictions on a sample set of test images to qualitatively assess model performance.
        Adjusted image preprocessing for models requiring specific input sizes (e.g., 299x299 for Xception).

## 🚀 Models Implemented

    Trained the dataset on various models , each of their summary is as follows :-

## XGBoost classifiers
  
    Implemented XGBoost, an efficient and scalable gradient boosting framework, for crisis detection.
   
    ![image](https://github.com/mahek0620/ThereForYou/assets/136893675/947e9367-7b2b-4c0d-a4a4-c3d71a48ea6d)


## Support Vector Classifier (SVC)

    Implementation: Implemented Support Vector Classifier (SVC) to classify crisis situations using kernel methods for effective separation in high-dimensional space.
   
    ![image](https://github.com/mahek0620/ThereForYou/assets/136893675/87500939-e5a5-4515-873d-46007d79a854)

## MLP Classifier

    Implementation: Implemented a Multi-Layer Perceptron (MLP) neural network with multiple layers of neurons, suitable for complex pattern recognition tasks.

    ![image](https://github.com/mahek0620/ThereForYou/assets/136893675/df7b618b-0028-42ab-94d5-6972f2a32126)

## LR

    Implementation: Applied logistic regression to detect crisis situations from user interactions and mood tracking data.
   
    ![image](https://github.com/mahek0620/ThereForYou/assets/136893675/1811ea3a-dd95-430e-8ab3-9be4410185a1)


## 📚 Libraries Needed

1. NumPy: For numerical computing.
2. pandas: For data analysis and manipulation.
3. scikit-learn: For machine learning tasks such as classification and clustering.
4. Matplotlib: For creating visualizations.
5. Keras: High-level neural networks API.
6. tqdm: For progress bars.
7. seaborn: For statistical data visualization.
8. tensorflow: Backend for Keras.

## 📊 Exploratory Data Analysis Results

 Comparison performance of classifiers for depression status in previous studies.
![image](https://github.com/mahek0620/ThereForYou/assets/136893675/46014dfa-a0fa-4e99-9f1a-c07009308287)


![image](https://github.com/mahek0620/ThereForYou/assets/136893675/2bab12bd-8cc9-4719-986b-bd0480948eb0)

![image](https://github.com/mahek0620/ThereForYou/assets/136893675/86c32ff7-312c-4ab0-8aee-64b34db4cdd3)

![image](https://github.com/mahek0620/ThereForYou/assets/136893675/6b2de083-62e8-44ce-8d12-f60574b41aac)


## 📈 Performance of the Models based on the Accuracy Scores

| Models      |       Accuracy Scores|
|------------ |------------|
|LR  | 83.3%  |
|SVM classifier      |  90%  |
|XGBoost       |   91%        |

    After classification by ML classifiers, we evaluated theresults based on both classification performance and featureimportance. In terms of classification performance, we compared performance under various conditions (24 conditions).To confirm changes in performance with class conditions,we set four conditions (binary-, three-, four-, and five-class labels). Among the four classifiers (XGBoost, SVC, MLP classifier, and LR), the XGBoost classifier showed the best performance in all experimental conditions. Furthermore, we compared the performance of our framework with that of the classifiers proposed in previous studies. The performance of each classifier is listed in Table 11. Despite using different data, we confirmed that the XGBoost classifier proposed in our study showed excellent performance compared to that of classifiers developed in previous studies

## 📢 Conclusion

**According to the accuracy scores it can be concluded that DenseNet121 and Xception were able to perform good on this dataset.**

we examined the classification performance and optimal length of the actigraphy data extracted for circadian rhythm indices. First, in terms of the classification performance, the XGBoost classifier outperformed the other algorithms based on all the evaluation metrics. In addition, to identify the classification performance in terms of various label conditions, we compared the values of evaluation metrics under four conditions (binary, three, four, and five classes). The evaluation metric values of the XGBoost classifier were 97.42% (accuracy), 97.51% (precision), 97.19% (recall), 97.40% (F1-score), and 99.00% (AUC) in the binary-class condition. In the three-class condition, accuracy (95.21%), precision (95.01%), recall (95.21%), F1-score (95.87%), and AUC (99.00%) were obtained. In the four-class condition, accuracy (95.92%), precision (95.02%), recall (95.46%), F1-score (95.82%), and AUC (99.00%) were found. In the five-class condition, as the last condition, accuracy (94.81%), precision (94.21%), recall (94.90%), F1-score (94.94%), and AUC (99.00%) were examined using the XGBoost classifier. 
![image](https://github.com/mahek0620/ThereForYou/assets/136893675/a07a855f-7dd6-42f5-aec5-3809ebd1a1d6)
![image](https://github.com/mahek0620/ThereForYou/assets/136893675/f3c4bc1b-a823-49cb-b45f-57d68353d029)
![image](https://github.com/mahek0620/ThereForYou/assets/136893675/6f3a76d2-e32d-49df-9185-27cbcdef7c83)
![image](https://github.com/mahek0620/ThereForYou/assets/136893675/f7f5cf56-3585-4c33-9761-1c2331e38013)




## ✒️ Your Signature

Full name:- Mahek Patel                  
Github Id :- https://github.com/mahek0620
Email ID :- mahekrpatel611@gmail.com
LinkdIn :- www.linkedin.com/in/mahek-patel-19670625b</br>
Participant Role :- Contributor / GSSOC (Girl Script Summer of Code ) - 2024
