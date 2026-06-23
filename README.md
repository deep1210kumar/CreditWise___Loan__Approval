# 💳 CreditWise — Loan Approval Prediction System

A machine learning web application that predicts whether a loan application will be **approved or rejected** based on applicant financial and personal details.

---


---

## 📌 Project Overview

CreditWise is a Streamlit-based web app that uses a **Gaussian Naive Bayes** classifier to predict loan approval. The model is trained on 1,000 applicant records with 20 features including income, credit score, DTI ratio, employment status, and more.

---

## 🧠 ML Models Evaluated

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---|---|---|---|
| **Logistic Regression** | **87.5%** | 79.0% | 80.3% | 79.7% |
| **Naive Bayes** ✅ (Selected) | **86.5%** | 78.3% | 77.0% | 77.7% |
| KNN | 75.5% | 62.0% | 50.8% | 55.9% |

> Naive Bayes was selected as the final model for its simplicity, speed, and good generalization.

---

## 📊 Dataset Features

| Feature | Type |
|---|---|
| Applicant_Income | Numerical |
| Coapplicant_Income | Numerical |
| Credit_Score | Numerical |
| DTI_Ratio | Numerical |
| Savings | Numerical |
| Collateral_Value | Numerical |
| Loan_Amount | Numerical |
| Loan_Term | Numerical |
| Age | Numerical |
| Dependents | Numerical |
| Existing_Loans | Numerical |
| Employment_Status | Categorical |
| Marital_Status | Categorical |
| Loan_Purpose | Categorical |
| Property_Area | Categorical |
| Education_Level | Categorical |
| Gender | Categorical |
| Employer_Category | Categorical |
| **Loan_Approved** | 🎯 Target |

---

## 🗂️ Project Structure

```
CreditWise__Loan_Aprroval/
│
├── main.py                  # Streamlit web app
├── loan_model.pkl           # Trained Naive Bayes model
├── scaler.pkl               # StandardScaler object
├── requirements.txt         # Python dependencies
├── Notebook/
│   └── CreditWise_Loan_system.ipynb   # EDA + Model training
└── README.md
```

---

## ⚙️ Tech Stack

- **Frontend:** Streamlit
- **ML Library:** Scikit-learn
- **Data Processing:** Pandas, NumPy
- **Visualization:** Seaborn, Matplotlib
- **Model Serialization:** Joblib

---

## 🛠️ Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/deep1210kumar/creditwise___loan__approval.git
cd creditwise___loan__approval

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run main.py
```

---

## 📈 Data Preprocessing

- Missing values handled via imputation
- Categorical features encoded using **Label Encoding**
- Numerical features scaled using **StandardScaler**
- Train/Test split: **80/20**

---

## 👨‍💻 Author

**Deepu Kumar**
- GitHub: [@deep1210kumar](https://github.com/deep1210kumar)

---


