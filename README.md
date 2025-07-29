# 🛳️ Titanic Exploratory Data Analysis (EDA)

This project explores the famous [Titanic dataset](https://www.kaggle.com/competitions/titanic) using Python. It's a hands-on demonstration of data cleaning, analysis, and visualization techniques.

## 📌 What This Project Covers

- Handling missing data (e.g., filling `Age` with median, `Embarked` with mode)
- Dropping columns with too many missing values (`Cabin`)
- Converting data types for better analysis (e.g., mapping `Survived` to "Yes"/"No")
- Generating group-based insights like survival rates by **gender** and **passenger class**
- Visualizing patterns using:
  - Bar plots for survival counts
  - Correlation heatmap for numeric features

## 🛠️ Tools Used

- Python 🐍
- Pandas
- Matplotlib
- Seaborn

## 📊 Key Insights

- 💡 ~74% of women survived, compared to ~19% of men
- 💡 ~63% of 1st class passengers survived, while only ~24% of 3rd class did

## 📸 Preview

Bar chart example:

![Survival by Gender](figures/survival_by_gender.png)

Correlation heatmap:

![Correlation Heatmap](figures/correlation_heatmap.png)

## ▶️ How to Run

```bash
# Clone this repo
git clone https://github.com/Kouka05/titanic-eda.git
cd titanic-eda

# Install dependencies (create virtual env recommended)
pip install pandas matplotlib seaborn

# Run the Jupyter notebook or Python script
jupyter notebook titanic_analysis.ipynb
