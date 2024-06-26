# Anomaly Detection with RNN Autoencoder

## Introduction
The goal of this project is to develop a robust system for detecting anomalies in audio, with a specific focus on identifying choking sounds. This will be accomplished using unsupervised learning techniques such as Convolutional Autoencoder (CAE) and Recurrent Neural Network (RNN) Autoencoder.

## Project Overview
The goal of this project is to develop an anomaly detection system using a Recurrent Neural Network (RNN) Autoencoder. The project comprises several key components:

 **Data Preprocessing**:
   - Audio data preprocessing involves extracting relevant features from the audio signals. In this project, features such as Mel-frequency cepstral coefficients (MFCCs) are extracted, as they are commonly used in audio analysis tasks.
   - The extracted features are then normalized to ensure consistent scaling and improve model convergence during training.

 **Model Training**:
   - An RNN-based Autoencoder model is trained using the preprocessed audio data. The Autoencoder architecture consists of an encoder network that compresses the input data into a latent representation and a decoder network that reconstructs the input from the latent space.
   - During training, the Autoencoder learns to reconstruct normal audio patterns accurately while minimizing reconstruction errors for anomalous patterns.

   We can observe that the RNN Autoencoder generally performs better in terms of MSE, RMSE, and MAE compared to the Convolutional Autoencoder. Here's a breakdown of the comparison of models in the current project:

- The RNN Autoencoder has a lower MSE of 0.560, indicating better reconstruction performance compared to the CAE's MSE of 1.137. RMSE:

-  The RNN Autoencoder also has a lower RMSE of 0.748, indicating a smaller average magnitude of error compared to the CAE's RMSE of 1.066. MAE:

T- he RNN Autoencoder's MAE of 0.579 is lower than the CAE's MAE of 0.856, showing that, on average, the RNN Autoencoder's predictions are closer to the actual values.

Based on these metrics, the RNN Autoencoder appears to provide better reconstruction performance than the Convolutional Autoencoder.