# -*- coding: utf-8 -*-
"""Parkinson's Disease Prediction1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-zmVcycWBNeDqpA7YqE68DG3Wvh2dEqX
"""

import pickle
import warnings

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

warnings.filterwarnings("ignore")
# Load the Parkinson's dataset
parkinsons_data = pd.read_csv("https://raw.githubusercontent.com/Aaron246/parkinsight/main/parkinsons_dataset.csv")
print(parkinsons_data.head(10))

print(parkinsons_data.shape)
# Check for missing values in the dataset
print(parkinsons_data.isnull().sum())
print(parkinsons_data.duplicated().sum())
print(parkinsons_data.info())
print(parkinsons_data.describe())

# Visualize the distribution of the 'Status' column
status_counts = parkinsons_data['Status'].value_counts()
plt.figure(figsize=(8, 6))
sns.barplot(x=status_counts.index, y=status_counts.values, palette="viridis")
plt.title('Count of Status')
plt.xlabel('Status')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

# Select important features for analysis
important_features = ['MDVP:Jitter (%)', 'MDVP:Jitter (Abs)', 'MDVP:Shimmer', 'MDVP:Shimmer (dB)',
                      'MDVP:APQ', 'MDVP:PPQ', 'MDVP:Fo (Hz)', 'MDVP:Fhi (Hz)', 'MDVP:Flo (Hz)', 'HNR']
important_features_dataset = parkinsons_data[important_features]

# Visualize the relationship between important features using pairplot
sns.pairplot(important_features_dataset, diag_kind='kde', palette='husl')
plt.show()

plt.figure(figsize=(16, 8))
sns.set(style="whitegrid")
for i, col in enumerate(parkinsons_data.columns[:-1]):
    plt.subplot(4, 5, i+1)
    sns.boxplot(x='Status', y=col, data=parkinsons_data, palette='Set2')
    plt.title(col)
    plt.xlabel('Status')
    plt.ylabel(col)
plt.tight_layout()
plt.show()
# Define functions for outlier detection and replacement
def replace_outliers(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    for col in df.columns:
        median_val = df[col].median()
        df[col] = df[col].mask((df[col] < lower_bound[col]) | (df[col] > upper_bound[col]), median_val)
    return df

def check_outliers(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = ((df < lower_bound) | (df > upper_bound)).any(axis=1)
    return outliers

numeric_columns = ['MDVP:Fo (Hz)', 'MDVP:Fhi (Hz)', 'MDVP:Flo (Hz)', 'MDVP:Jitter (%)',
                   'MDVP:Jitter (Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP',
                   'MDVP:Shimmer', 'MDVP:Shimmer (dB)', 'Shimmer:APQ3', 'Shimmer:APQ5',
                   'MDVP:APQ', 'Shimmer:DDA', 'HNR', 'NHR', 'DFA', 'Spread1',
                   'Spread2', 'PPE']

# Check for outliers before replacing
outliers_before = check_outliers(parkinsons_data[numeric_columns])
print("\nOutliers before replacing:", outliers_before.sum())
parkinsons_data[numeric_columns] = replace_outliers(parkinsons_data[numeric_columns])
# Check for outliers after replacing
outliers_after = check_outliers(parkinsons_data[numeric_columns])
print("\nOutliers after replacing:", outliers_after.sum())

corr = important_features_dataset.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr, annot=True, cmap='Blues', fmt=".2f", linewidths=0.5)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.title('Correlation Heatmap')
plt.show()

# Split the dataset into features (X) and target variable (Y)
X = parkinsons_data.drop(columns=['Status'], axis=1)
Y = parkinsons_data['Status']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)

# Standardize features by scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
filename = 'ss_parkin.sav'
pickle.dump(scaler, open(filename, 'wb'))
print(X_train_scaled.shape)
print(Y_train.shape)

# Train Support Vector Machine (SVM) model
svc_model = svm.SVC(kernel='linear', C=1)
svc_model.fit(X_train_scaled, Y_train)
y_pred = svc_model.predict(X_test_scaled)
svc_model_accuracy = accuracy_score(Y_test, y_pred)
svc_cls_report = classification_report(Y_test, y_pred)

print("SVM Classification Report:\n", svc_cls_report)
print("SVM Model Accuracy: {:.2f}%".format(svc_model_accuracy * 100))

# Train Random Forest Classifier model
rfc_model = RandomForestClassifier(n_estimators=100, random_state=42)
rfc_model.fit(X_train_scaled, Y_train)
y_pred = rfc_model.predict(X_test_scaled)
rfc_model_accuracy = accuracy_score(Y_test, y_pred)
rfc_cls_report = classification_report(Y_test, y_pred)
print("Random Forest Classification Report:\n", rfc_cls_report)
print("Random Forest Model Accuracy: {:.2f}%".format(rfc_model_accuracy * 100))

# Train Logistic Regression model
logreg_model = LogisticRegression(random_state=42)
logreg_model.fit(X_train_scaled, Y_train)
y_pred = logreg_model.predict(X_test_scaled)
logreg_model_accuracy = accuracy_score(Y_test, y_pred)
logreg_cls_report = classification_report(Y_test, y_pred)
print("Logistic Regression Classification Report:\n", logreg_cls_report)
print("Logistic Regression Model Accuracy: {:.2f}%".format(logreg_model_accuracy * 100))

# Train XGBoost Classifier model
xgb_model = XGBClassifier(random_state=42)
xgb_model.fit(X_train_scaled, Y_train)
y_pred = xgb_model.predict(X_test_scaled)
xgb_model_accuracy = accuracy_score(Y_test, y_pred)
xgb_cls_report = classification_report(Y_test, y_pred)
print("XGBoost Classification Report:\n", xgb_cls_report)
print("XGBoost Model Accuracy: {:.2f}%".format(xgb_model_accuracy * 100))

# Store model accuracies for comparison
model_accuracies = {
    'SVM': svc_model_accuracy,
    'Random Forest': rfc_model_accuracy,
    'Logistic Regression': logreg_model_accuracy,
    'XGBoost': xgb_model_accuracy
}

plt.figure(figsize=(10, 6))
plt.bar(model_accuracies.keys(), model_accuracies.values(), color=['blue', 'green', 'orange', 'purple'])
plt.title('Model Comparison: Accuracy')
plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.show()

# Hyperparameter Tuning for Random Forest
from sklearn.model_selection import GridSearchCV

# Define hyperparameter grid for Random Forest,
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
# Perform Grid Search CV for Random Forest
grid_search = GridSearchCV(estimator=rfc_model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
grid_search.fit(X_train_scaled, Y_train)

print("Best Hyperparameters for Random Forest:\n", grid_search.best_params_)
best_rfc_model = grid_search.best_estimator_
y_pred = best_rfc_model.predict(X_test_scaled)
best_rfc_accuracy = accuracy_score(Y_test, y_pred)
print("Best Random Forest Model Accuracy after Hyperparameter Tuning: {:.2f}%".format(best_rfc_accuracy * 100))

# Save the tuned model
joblib.dump(best_rfc_model, 'best_rfc_model.pkl')
# Load Parkinson's symptoms dataset
symptoms_data = pd.read_csv("https://raw.githubusercontent.com/Aaron246/parkinsight/main/parkinsons_symptoms_dataset.csv")
symptoms_data.head(10)

symptoms_data.isnull().sum()

symptoms_data.duplicated().sum()

symptoms_data.describe()

# Split the dataset into features and target variable
sd_X = symptoms_data.drop('Status', axis=1)
sd_y = symptoms_data['Status']

# Split the dataset into training and testing sets (80% train, 20% test)
sd_X_train, sd_X_test, sd_y_train, sd_y_test = train_test_split(sd_X, sd_y, test_size=0.2, random_state=42 , stratify = sd_y)

sd_scaler = StandardScaler()
sd_X_train_scaled = sd_scaler.fit_transform(sd_X_train)
sd_X_test_scaled = sd_scaler.transform(sd_X_test)

rf_classifier = RandomForestClassifier()
rf_classifier.fit(sd_X_train_scaled , sd_y_train)

sd_y_pred = rf_classifier.predict(sd_X_test_scaled)
sd_y_pred

sd_X_test_scaled

# Evaluate the performance of the classifier
sd_rf_accuracy = accuracy_score(sd_y_test, sd_y_pred)
print("Accuracy:", sd_rf_accuracy)

!pip install nolds

import librosa
import nolds
from scipy.signal import find_peaks


def extract_audio_features(audio_file):
    # Load audio file
    signal, fs = librosa.load(audio_file)
    print("Selected audio file:", audio_file)

    f0, voiced_flag, voiced_probs = librosa.pyin(signal, fmin=75, fmax=600)
    f0 = f0[~np.isnan(f0)]
    mdvp_fo = np.mean(f0)
    mdvp_fhi = np.max(f0)
    mdvp_flo = np.min(f0)
    jitter_percent = np.mean((np.abs(np.diff(f0)))/np.mean(f0)) * 100
    jitter_abs = np.mean(np.abs(np.diff(f0)))
    peaks, _ = find_peaks(signal, height=0)
    duration = len(signal) / fs
    mdvp_rap = np.sum(np.abs(np.diff(peaks))) / (len(peaks) * duration)
    mdvp_ppq = np.sum(np.abs(np.diff(peaks, n=2))) / (len(peaks) * duration)
    jitter_ddp = np.mean(np.abs(np.diff(f0))) * 3
    shimmer_array1 = np.abs(signal)
    desired_samples = len(f0)
    downsampling_factor = len(shimmer_array1) // desired_samples
    shimmer_array = shimmer_array1[::downsampling_factor][:desired_samples]
    shimmer = np.mean(np.abs(np.diff(shimmer_array)))
    mdvp_shimmer_db = 20 * np.mean(np.abs(np.log10(shimmer)))
    shimmer_apq3 = np.mean(np.abs(np.diff(shimmer_array, n=3, axis=0)))
    shimmer_apq5 = np.mean(np.abs(np.diff(shimmer_array, n=5, axis=0)))
    mdvp_apq = np.mean(np.sqrt(np.diff(shimmer_array) ** 2 + np.diff(f0) ** 2))
    shimmer_dda = np.mean(np.abs(np.diff(f0))) + np.mean(np.abs(np.diff(shimmer_array)))
    harmonics_energy = np.sum(signal[signal > np.mean(signal)] ** 2)
    noise_energy = np.sum(signal[signal <= np.mean(signal)] ** 2)
    hnr = harmonics_energy / noise_energy
    nhr = 1 / hnr
    mfccs = librosa.feature.mfcc(y=signal, sr=fs, n_mfcc=13)
    dfa = nolds.dfa(signal)
    spread1 = np.std(f0)
    spread2 = np.var(f0)
    ppe = np.mean(voiced_probs)

    features = {
        'MDVP:Fo (Hz)': mdvp_fo,
        'MDVP:Fhi (Hz)': mdvp_fhi,
        'MDVP:Flo (Hz)': mdvp_flo,
        'MDVP:Jitter (%)': jitter_percent,
        'MDVP:Jitter (Abs)': jitter_abs,
        'MDVP:RAP': mdvp_rap,
        'MDVP:PPQ': mdvp_ppq,
        'Jitter:DDP': jitter_ddp,
        'MDVP:Shimmer': shimmer,
        'MDVP:Shimmer (dB)': mdvp_shimmer_db,
        'Shimmer:APQ3': shimmer_apq3,
        'Shimmer:APQ5': shimmer_apq5,
        'MDVP:APQ': mdvp_apq,
        'Shimmer:DDA': shimmer_dda,
        'HNR': hnr,
        'NHR': nhr,
        'DFA': dfa,
        'Spread1': spread1,
        'Spread2': spread2,
        'PPE': ppe
    }
    return features

# Define or load rf_model, sd_scaler, and rf_classifier here

# @title Parkinsight
audio_file = "PD_AH_inputfile2" # @param ["HC_AH_inputfile1", "HC_AH_inputfile2", "PD_AH_inputfile1", "PD_AH_inputfile2"]
tremor = 6 # @param {type:"slider", min:0, max:9, step:1}
bradykinesia = 5 # @param {type:"slider", min:0, max:9, step:1}
rigidity = 4 # @param {type:"slider", min:0, max:9, step:1}

filepath = "/content/" + audio_file + ".wav"
feat_dict = extract_audio_features(filepath)
# Predict status using audio features extracted from input file
feat_dict

input_data = feat_dict.values()

input_data_array = np.asarray(list(input_data))
print("\nInput Data in Array form :\n",input_data_array)

input_data_reshaped = input_data_array.reshape(1,-1)
print("\nInput Data Reshaped :\n",input_data_reshaped)

std_input_data = scaler.transform(input_data_reshaped)
print("\nInput Data Scaled :\n",std_input_data)

input_data = feat_dict.values()

input_data_array = np.asarray(list(input_data))
print("\nInput Data in Array form :\n",input_data_array)

input_data_reshaped = input_data_array.reshape(1,-1)
print("\nInput Data Reshaped :\n",input_data_reshaped)

std_input_data = scaler.transform(input_data_reshaped)
print("\nInput Data Scaled :\n",std_input_data)

voice_pred = rfc_model.predict(std_input_data)
print("\nVoice Prediction:\n",voice_pred)
# Predict status using symptoms provided by the user
test_data = np.array([ tremor,  bradykinesia,  rigidity])
print(test_data)

test_data_reshaped = test_data.reshape(1, -1)
print(test_data_reshaped)

test_data_scaled = sd_scaler.transform(test_data_reshaped)
print(test_data_scaled)

symptoms_pred = rf_classifier.predict(test_data_scaled)
print("\nSymptoms Prediction :\n",symptoms_pred)
# Output prediction result based on audio features and symptoms
if (voice_pred == 0 and symptoms_pred == 0):
    print("No, you do not have Parkinsons Disease.")

elif (voice_pred == 0 and symptoms_pred == 1):
    print("You may have stage 1 Parkinson's disease (tremor) !.\n Consider consulting a doctor for further evaluation and monitoring.")

elif (voice_pred == 1 and symptoms_pred == 0):
    print("You may be experiencing early voice symptoms(voice changes) associated with Parkinson's disease.\nIt's advisable to seek medical advice for assessment.")

else:
    print("Yes, you have Parkinsons Disease.\nIt's important to consult a doctor for further diagnosis and treatment.")

