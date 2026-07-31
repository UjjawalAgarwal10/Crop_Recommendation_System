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
- Visualization Images
- Model Serialization
- Prediction
- Flask Web Application
- Tech Stack
- How to run
- Future Improvements

## 📌 Overview :
- This project uses [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) to train a **RandomForestClassifier Model** that predicts the best crop to grow for a given set of soil and climate conditions.
- The pipeline contains model exploration, preprocessing, training, evaluation, visualization and is deployed using **Flask Web API** where user can input soil and climate conditions through a form and wil get instant recommendation.

## 📊 Dataset

| Detail | Value |
|--------|-------|
| Source | Crop Recommendation Dataset (Kaggle) |
| Rows | 2200 |
| Features | 7 → `N`, `P`, `K`, `temperature`, `humidity`, `ph`, `rainfall` |
| Target | `label` — 22 crop types (rice, maize, cotton, coffee, banana, etc.) |
| Missing Values | None |
| Duplicate Rows | None |

## 🔍 Exploratory Data Analysis (EDA)

- Verified dataset shape, column data types, and absence of null/duplicate values
- Analyzed unique value counts and class-wise label distribution (`value_counts`)
- Computed group-wise feature means per crop label (`groupby("label").mean()`) to understand how nutrient/climate profiles differ across crops

