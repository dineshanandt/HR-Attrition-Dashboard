# HR Attrition Dashboard

An interactive dashboard and predictive modeling project to analyze employee attrition trends, identify risk factors, estimate revenue loss, and support data-driven HR strategies.

---

## 📊 Project Overview

This project analyzes IBM's HR Employee Attrition dataset using Python, machine learning, and Dash. It includes:

- 🧪 Exploratory Data Analysis (EDA)
- 🔍 Predictive Modeling (Logistic Regression, Random Forest, XGBoost)
- 💸 Revenue Loss Estimation
- 📊 Dash Web App for Interactive Visualization

---

## Dataset

The project uses the **IBM HR Employee Attrition dataset**, a publicly available dataset designed for HR analytics and data science applications.  
It contains 1,470 employee records and 35 features including:

- Demographics: Age, Gender, Education, Marital Status
- Job-related details: Department, Job Role, Job Level, Salary, Stock Option Level
- Work-life balance: Work-Life Balance, Overtime, Business Travel
- Performance and engagement: Performance Rating, Years at Company, Job Satisfaction

Dataset link: [IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

---

## ✨ Key Features

- Attrition Breakdown by Role & Department  
- Revenue Loss Estimation per department  
- Tenure Heatmap by Job Role and Department  
- Interactive Dropdown to filter by department  
- ML Model Accuracy with SMOTE to balance attrition data  

---

## 📁 Project Structure

```
HR-Attrition-Dashboard/
├── app.py                                 # Dash web app script
├── employee_attrition_prediction.ipynb    # Full EDA + ML notebook
├── attrition_dashboard_data.csv           # Cleaned dataset for Dash
├── HR-Employee-Attrition.csv              # Original dataset
├── requirements.txt                       # Python dependencies
├── screenshots/                           # Project screenshots
│   ├── Screenshot 1.png
│   ├── Screenshot 2.png
│   └── Screenshot 3.png
└── README.md                              # Project documentation
```
---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/dineshanandt/HR-Attrition-Dashboard.git
cd HR-Attrition-Dashboard
```

### 2. Create a virtual environment & activate it (recommended)
```bash
python -m venv venv
source venv/bin/activate         # Mac/Linux
venv\Scripts\activate            # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Dash app
```bash
python app.py
```
Then visit http://127.0.0.1:8050 in your browser.

## 🧠 Machine Learning Models  
Trained on a cleaned dataset with SMOTE applied to handle class imbalance. Models include:

- **Logistic Regression** — Accuracy around **84%**, effective for baseline comparison  
- **Random Forest** — Captures non-linear relationships with good generalization  
- **Gradient Boosting** — Boosted decision trees for improved accuracy  
- **XGBoost** — Tuned using threshold optimization to prioritize **recall**, improving identification of potential attrition cases

## 🖼️ Screenshots
<p align="center">
  <img src="screenshots/Screenshot 2.png" width="700"><br>
</p>

## ✍️ Author

**[Dinesh Anand Thulasiraman](https://www.linkedin.com/in/dineshat/)**  
📍 Data Science Graduate Student  
🔗 [GitHub Profile](https://github.com/dineshanandt) | [LinkedIn](https://www.linkedin.com/in/dineshat/)
