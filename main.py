import pandas as pd
import matplotlib.pyplot as plt

# 1) LOAD & CLEAN
df = pd.read_csv('train.csv')

# Fill missing ages with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill missing Embarked with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop Deck (too many NaNs)
if 'Deck' in df.columns:
    df = df.drop(columns=['Deck'])

# Map Survived to labels and cast Pclass to category
df['Survived'] = df['Survived'].map({0:'No', 1:'Yes'})
df['Pclass']   = df['Pclass'].astype('category')

# 2) SUMMARY STATISTICS
print("=== Overall Summary ===")
print(df.describe(include='all'))

# 3) GROUP‑BASED INSIGHTS
surv_by_sex = (
    df.groupby('Sex')['Survived']
      .value_counts(normalize=True)
      .unstack(fill_value=0) * 100
).round(1)
print("\n=== Survival Rate by Sex (%) ===")
print(surv_by_sex)

surv_by_class = (
    df.groupby('Pclass')['Survived']
      .value_counts(normalize=True)
      .unstack(fill_value=0) * 100
).round(1)
print("\n=== Survival Rate by Class (%) ===")
print(surv_by_class)

# 4) VISUALIZATIONS

# A) Bar plot – survival counts by sex
fig, ax = plt.subplots()
counts_sex = df.groupby('Sex')['Survived'].value_counts().unstack()
counts_sex.plot(kind='bar', ax=ax)
ax.set_title('Survival Counts by Sex')
ax.set_ylabel('Count')
ax.legend(title='Survived')
plt.tight_layout()
plt.show()

# B) Bar plot – survival counts by class
fig, ax = plt.subplots()
counts_cls = df.groupby('Pclass')['Survived'].value_counts().unstack()
counts_cls.plot(kind='bar', ax=ax)
ax.set_title('Survival Counts by Passenger Class')
ax.set_ylabel('Count')
ax.legend(title='Survived')
plt.tight_layout()
plt.show()

# C) Heatmap – numeric correlations
num_cols = df.select_dtypes(include='number').columns
corr = df[num_cols].corr()

fig, ax = plt.subplots()
im = ax.imshow(corr, aspect='auto')
ax.set_xticks(range(len(num_cols)))
ax.set_yticks(range(len(num_cols)))
ax.set_xticklabels(num_cols, rotation=45, ha='right')
ax.set_yticklabels(num_cols)
ax.set_title('Correlation Matrix')
plt.colorbar(im, ax=ax)
plt.tight_layout()
plt.show()
