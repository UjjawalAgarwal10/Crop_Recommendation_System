# 🌾Crop_Recommendation_System :-
- An end-to-end Machine Learning project that recommends the most suitable crop to cultivate based on soil nutrients (N, P, K), climatic conditions (temperature, humidity,rainfall), and soil pH.
- This will help farmers and agronomists to make data driven agricultural decisions.

## 📖 Table of Contents :-
- Overveiw
- Dataset
- Exploratory Data Analysis(EDA)
- Preprocessing and Feature Scaling
- Model Training
- Model Evaluation
- Visualization Graphs
- Model Serialization
- Prediction
- Flask Web Application
- Tech Stack
- How to run
- Future Improvements

## 📌 Overview :-
- This project uses [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) to train a **RandomForestClassifier Model** that predicts the best crop to grow for a given set of soil and climate conditions.
- The pipeline contains model exploration, preprocessing, training, evaluation, visualization and is deployed using **Flask Web API** where user can input soil and climate conditions through a form and wil get instant recommendation.

## 📊 Dataset :-

| Detail | Value |
|--------|-------|
| Source | Crop Recommendation Dataset (Kaggle) |
| Rows | 2200 |
| Features | 7 → `N`, `P`, `K`, `temperature`, `humidity`, `ph`, `rainfall` |
| Target | `label` — 22 crop types (rice, maize, cotton, coffee, banana, etc.) |
| Missing Values | None |
| Duplicate Rows | None |

## 🔍 Exploratory Data Analysis (EDA) :-

- Verified dataset shape, column data types, and absence of null/duplicate values.
- Analyzed unique value counts and class-wise label distribution (`value_counts`).
- Computed group-wise feature means per crop label (`groupby("label").mean()`) to understand how nutrient/climate profiles differ across crops.

## ⚙️ Feature Engineering & Preprocessing :-

- Separated the dataset into **features (X)** and **target labels (y)**
- Applied **StandardScaler** to normalize all numerical features to a common scale
- Performed a **stratified 80-20 train-test split** to preserve class balance across all 22 crop types.

## 🤖 Model Training :-
I have trained a model using **RandomForestClassifier** which is present in **sklearn.ensemble library** with some tuned hyperparamters to balance accuracy,precision and to avoid overfitting.
- 1.n_estimators: 100
- 2.max_depth: 10
- 3.min_samples_split: 5
- 4.min_samples_leaf: 5
- 5.random_state: 42

## 📈 Model Evaluation
I have evaluated model using multiple weighted metrics on the held-out test set:
| Metric | Score |
|--------|-------|
| Training Accuracy | 99.66% |
| Testing Accuracy | 99.55% |
| Precision (weighted) | 99.57% |
| F1-Score (weighted) | 99.55% |
| Recall (weighted) | 99.55% |

  




