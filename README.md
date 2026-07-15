# 🏠 Divar Real Estate Price Prediction

This project focuses on predicting the **full deposit value** of Iranian real estate rental advertisements using the Divar real estate dataset. The project covers the complete machine learning workflow, from data preprocessing and exploratory data analysis to feature engineering, model selection, hyperparameter optimization, and final model evaluation.

---

# 📌 Project Overview

The Divar Real Estate Dataset contains more than **one million real estate advertisements** collected from the Divar platform across different cities in Iran. The dataset includes residential and commercial properties together with geographical, structural, financial, and temporal information.

The objective of this project is to build a regression model capable of accurately predicting the **full deposit value** of rental properties based on their characteristics.

---

# 🎯 Objectives

- Perform comprehensive data preprocessing
- Explore and visualize the dataset
- Engineer meaningful features
- Compare multiple regression algorithms
- Optimize model hyperparameters
- Select the best-performing model
- Evaluate the final model on an unseen test set

---

# 📊 Dataset

Original Dataset Size

- More than **1,000,000 advertisements**

Final Dataset Used for Modeling

- **331,202 samples**

Target Variable

- `full_deposit`

---

# 🛠 Data Preprocessing

The following preprocessing steps were performed:

- Removed duplicated and inconsistent records
- Filtered unrealistic values and obvious outliers
- Removed invalid prices and deposits
- Converted data types to memory-efficient formats
- Handled missing values
- Created a unified target variable (`full_deposit`)
- Converted categorical features to appropriate formats
- One-Hot Encoded categorical variables
- Split data into Train / Validation / Test sets

Memory optimization included:

- float32
- Int8 / Int16
- Boolean
- Category

---

# ⚙ Feature Engineering

Several new features were generated to improve prediction performance.

Examples include:

- Building Age
- Created Year
- Created Month
- Unified Full Deposit
- Property characteristics
- Geographical information
- Building facilities

Final Features:

- full_deposit (Target)
- building_size
- building_age
- rooms_count
- floor
- total_floors_count
- unit_per_floor
- city_slug
- cat2_slug
- cat3_slug
- created_year
- created_month
- location_latitude
- location_longitude
- has_parking
- has_elevator
- has_balcony
- has_warehouse
- is_rebuilt

---

# 📈 Exploratory Data Analysis

The project includes several statistical analyses and visualizations, including:

- Distribution of advertisements
- Building year histogram
- Monthly advertisement trends
- Correlation matrix
- Boxplots
- Outlier analysis
- Missing value analysis
- Inflation-adjusted price analysis
- Geographic analysis
- Feature distribution analysis

---

# 🤖 Machine Learning Models

The following regression algorithms were implemented and compared:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- XGBoost Regressor

---

# 🔍 Hyperparameter Optimization

Different optimization strategies were explored.

Final models were optimized using:

- Bayesian Optimization (BayesSearchCV)

The model selection procedure followed the standard workflow:

Train → Validation → Test

No information from the Test set was used during model development.

---

# 📊 Model Performance

| Model | MAE | RMSE | R² |
|-------|------------:|------------:|------:|
| Linear Regression | 294,180,745 | 440,514,415 | 0.4581 |
| Ridge Regression | 294,754,186 | 441,014,850 | 0.4569 |
| Random Forest + Bayesian Optimization | 191,672,647 | 326,883,492 | 0.7016 |
| **XGBoost + Bayesian Optimization** | **189,857,168** | **324,196,861** | **0.7069** |

---

# 🏆 Best Model

**XGBoost Regressor**

Final Test Results

| Metric | Value |
|--------|------:|
| MAE | 189,857,168 |
| RMSE | 324,196,861 |
| R² | **0.7069** |
| Adjusted R² | **0.7055** |

The close agreement between the validation and test scores indicates that the final model generalizes well and does not suffer from significant overfitting.

---

# 📚 Project Workflow

```
Data Collection
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Train / Validation / Test Split
        │
        ▼
Model Training
        │
        ▼
Bayesian Hyperparameter Optimization
        │
        ▼
Model Comparison
        │
        ▼
Final Model Selection
        │
        ▼
Final Test Evaluation
```

---

# 🧰 Technologies Used

Programming Language

- Python

Libraries

- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- XGBoost
- Scikit-Optimize (BayesSearchCV)

Development Environment

- Jupyter Notebook

---

# 📁 Repository Structure

```
.
├── data/
├── notebooks/
├── reports/
├── README.md
└── requirements.txt
```

---

# 📌 Results

The experiments demonstrate that ensemble tree-based models significantly outperform linear regression methods for structured real estate data.

Among all evaluated algorithms, **XGBoost with Bayesian Optimization** achieved the best predictive performance, explaining approximately **71% of the variance** in rental deposit values while maintaining excellent generalization on unseen data.

---

# 🚀 Future Work

Possible improvements include:

- CatBoost
- LightGBM
- Target Encoding
- Spatial Feature Engineering
- Economic Indicators
- Inflation Features
- Advanced Ensemble Learning
- Model Explainability using SHAP

---

# 👥 Team

---

# 📄 License
