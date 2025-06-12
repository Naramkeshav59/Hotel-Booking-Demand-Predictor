
# 🏨 Hotel Booking Demand Predictor

A full end-to-end Machine Learning pipeline to predict hotel booking cancellations based on historical data. The project handles data ingestion, preprocessing, feature engineering, model training, and evaluation with modular and reproducible design.

---

## 📌 Table of Contents

* [🚀 Project Overview](https://github.com/Naramkeshav59/Hotel-Booking-Demand-Predictor/new/main#-project-overview)
* [⚙️ Pipeline Stages](https://github.com/Naramkeshav59/Hotel-Booking-Demand-Predictor/new/main#️-pipeline-stages)
* [🛠️ Tech Stack](https://github.com/Naramkeshav59/Hotel-Booking-Demand-Predictor/new/main#️-tech-stack)
* [🏃‍♂️ How to Run](https://github.com/Naramkeshav59/Hotel-Booking-Demand-Predictor/new/main#️-how-to-run)
* [📊 Results](https://github.com/Naramkeshav59/Hotel-Booking-Demand-Predictor/new/main#-results)
* [👤 Author](https://github.com/Naramkeshav59/Hotel-Booking-Demand-Predictor/new/main#-author)

---

## 🚀 Project Overview

Hotel booking cancellations can lead to operational and financial losses. This project uses a supervised machine learning approach to predict whether a booking is likely to be canceled, enabling better planning and customer management.

---

## ⚙️ Pipeline Stages

1. **Data Ingestion**
   * Loads raw CSV data
   * Splits into training and test sets
   * Saves processed data for the pipeline

2. **Data Processing**
   * Drops irrelevant columns
   * Handles outliers and null values
   * Saves cleaned dataset

3. **Feature Engineering**
   * Encodes categorical variables
   * Selects top features using Mutual Information
   * Saves the final feature set

4. **Model Training**
   * Performs hyperparameter tuning using Grid Search
   * Trains a Gradient Boosting Classifier
   * Evaluates model performance on test data

---

## 🛠️ Tech Stack

- **Languages & Tools:** Python, Pandas, Scikit-learn, XGBoost, Matplotlib, Seaborn  
- **ML Workflow:** Data Cleaning, Feature Engineering (Mutual Information), Hyperparameter Tuning, Model Evaluation  
- **Pipeline & Automation:** Jenkins (CI/CD), Docker  
- **Cloud & Deployment:** AWS S3, AWS ECR, AWS ECS with Fargate, Application Load Balancer  
- **Logging & Monitoring:** Python logging, Jenkins logs, AWS CloudWatch (optional)

---

## 🏃‍♂️ How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/<your-username>/hotel-booking-demand-predictor.git
   cd hotel-booking-demand-predictor
```

2. Create conda environment:

   ```bash
   conda create -n hotel_pred_env python=3.10
   conda activate hotel_pred_env
   pip install -r requirements.txt
   ```

3. Run the pipeline:

   ```bash
   python main.py
   ```

---

```

---

## 📊 Results

| Metric      | Score                                                          |
| ----------- | -------------------------------------------------------------- |
| Accuracy    | 96.39%                                                         |
| Precision   | 96.56%                                                         |
| Recall      | 96.38%                                                         |
| F1-score    | 96.35%                                                         |
| Best Params | `{'learning_rate': 0.1, 'max_depth': 15, 'n_estimators': 300}` |

---

## 👤 Author

**Keshav Naram**
Graduate Student in Applied Machine Learning
[LinkedIn](https://www.linkedin.com/in/keshav-naram-33a834285)

---

