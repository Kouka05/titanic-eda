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

<img width="795" height="600" alt="image" src="https://github.com/user-attachments/assets/512a5113-4875-466d-9a10-4608b7d49a07" />

<img width="795" height="603" alt="image" src="https://github.com/user-attachments/assets/fe578e2c-e86f-4fff-ae34-bc7fde817796" />

<img width="795" height="628" alt="image" src="https://github.com/user-attachments/assets/a92017de-e4a1-4f83-947a-b9ba992574e0" />


## ▶️ How to Run

```bash
# Clone this repo
git clone https://github.com/Kouka05/titanic-eda.git
cd titanic-eda

# Install dependencies (create virtual env recommended)
pip install pandas matplotlib seaborn

# Run the Python script
python main.py
