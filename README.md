# 🎓 Student Score Predictor

A beginner-friendly Machine Learning project that predicts a student's final exam score based on study hours, attendance percentage, and previous scores — built using Python and Scikit-learn.

---

## 📌 Project Overview

Many students and educators want to understand what factors influence academic performance. This project uses a **Linear Regression model** to analyze these factors and predict final exam scores with reasonable accuracy.

---

## 🖼️ Screenshots

> *(Add screenshots of your charts and output here after running the project)*

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Core programming language |
| Pandas | Data loading and manipulation |
| NumPy | Numerical computations |
| Matplotlib | Data visualization |
| Seaborn | Statistical plots and heatmaps |
| Scikit-learn | Machine Learning model |

---

## 📂 Project Structure

```
student-score-predictor/
│
├── data/
│   └── student_scores.csv       # Dataset
│
├── predictor.py                 # Main ML script
├── visualize.py                 # Charts and graphs
├── requirements.txt             # Dependencies
└── README.md                    # Project documentation
```

---

## ⚙️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/tushar-rajpurohit/student-score-predictor.git
cd student-score-predictor
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the predictor**
```bash
python predictor.py
```

**4. Run the visualizations**
```bash
python visualize.py
```

---

## 📊 Features

- ✅ Loads and cleans student dataset using Pandas
- ✅ Exploratory Data Analysis (EDA) with Seaborn heatmaps and scatter plots
- ✅ Trains a Linear Regression model using Scikit-learn
- ✅ Predicts final exam scores based on:
  - Study hours per day
  - Attendance percentage
  - Previous exam scores
- ✅ Displays model accuracy (R² Score and Mean Absolute Error)
- ✅ Visualizes actual vs predicted scores

---

## 📈 Sample Output

```
Model Accuracy (R² Score): 0.87
Mean Absolute Error: 3.24

Input:  Study Hours = 6, Attendance = 85%, Previous Score = 72
Output: Predicted Final Score = 78.4
```

---

## 📚 Dataset

Dataset sourced from [Kaggle — Student Performance Dataset](https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression)

Contains the following features:
- `Hours Studied` — daily study hours
- `Attendance` — attendance percentage
- `Previous Scores` — scores from prior exams
- `Performance Index` — final score (target variable)

---

## 🧠 What I Learned

- Data preprocessing and cleaning with Pandas
- Exploratory Data Analysis (EDA)
- Building and evaluating a Linear Regression model
- Data visualization using Matplotlib and Seaborn
- Understanding ML metrics: R² Score, MAE

---

## 🚀 Future Improvements

- [ ] Add more features (sleep hours, extracurricular activities)
- [ ] Try other models (Decision Tree, Random Forest)
- [ ] Build a simple web interface using Flask
- [ ] Deploy on Heroku or Render

---

## 👤 Author

**Tushar Rajpurohit**  
B.Tech CSE (AI & ML) — Sreenidhi Institute of Science and Technology  
📧 tusharrajpurohit3579@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/tushar-rajpurohit)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
