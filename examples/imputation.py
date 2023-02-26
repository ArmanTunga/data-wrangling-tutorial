import pandas as pd
import seaborn as sns
import numpy as np

###########################################
#         Fill Missing AGE Values         #
###########################################
# Load the Titanic dataset from seaborn
df = sns.load_dataset("titanic")

# Compute the mean age for each combination of Sex, Pclass, and Survived
grouped = df.groupby(["sex", "class", "survived"])
mean_age = grouped.age.mean()


# Define a function to impute missing "Age" values
def impute_age(row):
    if pd.isnull(row['age']):
        age_value = mean_age.loc[(row['sex'], row['class'], row["survived"])]
        return round(age_value)
    else:
        return row['age']


# Apply the function to the DataFrame
df['age'] = df.apply(impute_age, axis=1)

# Check if there are any missing values left
print(df.isnull().sum())

################################################
#         Fill Missing SURVIVED Values         #
################################################

# Set first 10 rows to NaN
df.loc[:9,"survived"] = np.nan

# Compute the mean survival rate for each combination of Sex, Pclass, and Age
df["age_grouped"] = pd.cut(df["age"], [0, 18, 50, df["age"].max()])
grouped = df.groupby(["sex", "class", "age_grouped"])
mean_survival = grouped.survived.mean()


# Define a function to impute missing "Survived" values
def impute_survived(row):
    if pd.isnull(row['survived']):
        survived_value = mean_survival.loc[(row['sex'], row['class'], row["age_grouped"])]
        return round(survived_value)
    else:
        return row['survived']


# Apply the function to the DataFrame
df['survived'] = df.apply(impute_survived, axis=1)

# Check if there are any missing values left
print(df.isnull().sum())
df.head()
