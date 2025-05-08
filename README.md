# 🚢 Titanic Survival Prediction

This Python-based data science project analyses passenger data from the Titanic disaster to predict survival using data preprocessing, Exploratory Data Analysis (EDA), and machine learning. The code is structured for use in **PyCharm** and consists of modular `.py` script files.

---

## 🧠 Objective

Explore and model the Titanic dataset to identify key features affecting survival and build a machine learning model for prediction. This project uses the [Kaggle Titanic dataset](https://www.kaggle.com/c/titanic/data) to explore data cleaning, visualization, and machine learning for survival prediction.

---

## 🗂️ Project Structure

```
titanic_survival_project/
├── data/
│   └── titanic.csv             # Place original dataset here
│   └── titanic_cleaned.csv     # Output of cleaning script
├── figures/
│   └── age_distribution.png    
│   └── survival_by_sex.png  
├── models/
│   └── encoder_embarked.pkl            
│   └── encoder_sex.pkl 
│   └── logistics_model.pkl
├── src/
│   ├── data_cleaning.py
│   ├── exploratory_analysis.py
│   └── model_training.py
│   └── utils.py
├── .gitignore
├── power_point_presentation.py
├── README.md
├── requirements.txt
└── Titanic_Survival_Prediction_Project.pptx

```

---

## 🛠️ Technologies Used

- Python 3.8+
- pandas, numpy
- seaborn, matplotlib
- scikit-learn, joblib
- powerpoint
- csv file
- pycharm

---

## 🚀 Setup Instructions

1. **Clone the repository**

```
https://github.com/AAdewunmi/titanic_survival_project.git
```

2. **Create a virtual environment (macOS/Linux)**

```bash
# Set up virtual environment
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run scripts
python src/data_cleaning.py
python src/eda.py
python src/model.py
```

---

## 📈 Visualizations

Output plots will be saved in the `figures/` folder.

---

## ✅ Model Performance

- Accuracy: ~80%
- Key features: `sex`, `pclass`, `fare`

---

## 👤 Author

Adrian Adewunmi – [GitHub](https://github.com/AAdewunmi)
