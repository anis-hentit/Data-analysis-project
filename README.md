# Churn Prediction and EDA Project

This repository contains the code and data for a Churn Prediction project, including Exploratory Data Analysis (EDA) and machine learning models to predict customer churn. The project aims to provide insights into customer behavior and develop a predictive model to identify potential churners.

## Project Overview

- **Problem**: Churn prediction in a business context refers to identifying customers likely to cancel their subscriptions or services. In this project, we focus on predicting customer churn in a telecom company based on various features.

- **Objective**: The project has two main objectives:

    1. Conduct Exploratory Data Analysis (EDA) to gain insights into the dataset, uncover trends, and visualize the data.
    
    2. Build machine learning models to predict customer churn and evaluate their performance.

## Data

The project utilizes a <a href="https://archive.ics.uci.edu/dataset/563/iranian+churn+dataset">customer churn dataset</a> containing various features related to customer behavior and subscription details. The dataset is available in the 'data' directory.

## Exploratory Data Analysis (EDA)

The EDA process involves:

- Data Cleaning: Handling missing values, outliers, and data preprocessing.
- Data Visualization: Creating visualizations to uncover patterns and trends.
- Feature Analysis: Exploring the relationships between features and identifying potential predictors of churn.

## Churn Prediction Models

The project explores and evaluates the following machine learning models for churn prediction:

- **Logistic Regression**: Achieved an accuracy of 0.88 and demonstrated good precision for non-churn customers.

- **XGBoost**: Outperformed other models with an accuracy of 0.94, high AUC (0.98), and balanced F1-scores for both churn and non-churn classes.

- **Support Vector Machine (SVM)**: Achieved an accuracy of 0.92 and showed a good balance between precision and recall.

## Conclusion

In this project, we performed EDA to gain insights into the dataset and built machine learning models for churn prediction. XGBoost achieved the highest accuracy and AUC, making it a robust model for predicting customer churn. SVM also showed promising performance with a balance between precision and recall. Logistic Regression provided reasonable results but had the lowest accuracy.

The project demonstrates the importance of understanding customer behavior and developing predictive models to identify potential churners. Further improvements can be made to enhance model performance and address specific business requirements.

## Getting Started

To run the code and explore the project, follow these steps:

1. Clone this repository to your local machine.

2. Install the required dependencies.

3. Run the notebook.

4. To deploy the Churn Prediction model as a Flask API simply run the last cell of the notebook and open <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a>

5. Experiment with the API by submitting input data for churn prediction.

Feel free to explore the project and adapt it to your needs.



