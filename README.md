# Data Wrangling Tutorial
This is the repository of [my Medium article](https://medium.com/@armantunga): How To Actually Achieve Your Data Wrangling: A Beginner's Guide

---

## Examples Used In The Article

### 1. Imputation: 
Imputation is a technique used to replace missing values with estimates based on other data. For example, we may use the mean or median value of a variable to impute missing values.
<br><br>Let's fill in the missing age values from the titanic dataset:
```python
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

```
Voila! 🎉
<br>
What about if we set survived column of the first 10 rows to NaN and try to fill in them?
```python
# !!!!!! After setting imputing age column. !!!!!!
# !!!!!! Otherwise we will get an error !!!!!!

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
```

### 2. Standardization:

Standardization is a technique used to ensure that data is formatted consistently. For example, we may convert all dates to a standard format or convert all units of measurement to a common standard.
```python
import pandas as pd

# create a sample dataframe with messy dates
df = pd.DataFrame({
    "date": ["Jan 1, 2022", "2022-02-02", "03/03/2022", "Mar 4th, 2022"]
})

# convert date column to datetime format
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# convert all dates to a standard format
df["date"] = df["date"].dt.strftime("%Y-%m-%d")

print(df)
"""
         date
0  2022-01-01
1  2022-02-02
2  2022-03-03
3  2022-03-04
"""
```
Let's look at an another example where we have different units for weight:
```python
import pandas as pd

# create a sample dataframe with messy measurements
df = pd.DataFrame({
    "patient_id": [1, 2, 3, 4],
    "weight": ["70 kg", "154 lbs", "62 kg", "143 lbs"]
})

# create a conversion dictionary for weight units
unit_conversion = {"kg": 1, "lbs": 0.453592}

# extract the weight and unit into separate columns
df[['weight_num', "weight_unit"]] = df["weight"].str.split(" ", expand=True)

# convert all weights to a standard unit (kg)
df["weight_num"] = pd.to_numeric(df["weight_num"])\
                   * df["weight_unit"].map(unit_conversion)

# drop the original weight and weight_unit columns
df = df.drop(["weight", "weight_unit"], axis=1)

print(df)
"""
   patient_id  weight_num
0           1   70.000000
1           2   69.853168
2           3   62.000000
3           4   64.863656
"""
```
### 3. Filtering:


```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Load dataset
df = pd.read_csv("./datasets/civil_engineering_example.csv")

# Take a look
df.head()

corr_matrix = df.corr()
corr_matrix

fig, ax = plt.subplots(figsize=(10, 8))
heatmap = sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax, xticklabels=corr_matrix.columns, yticklabels=corr_matrix.columns, annot_kws={"fontsize":8})
ax.tick_params(axis='both', labelsize=12) # Change tick label size for both axes
plt.xticks(rotation=45)
plt.show()

df = df.drop(columns=['Number of Lanes'])
```

### 4. Reshaping: 
It is a data manipulation technique that is utilized to convert data from one form to another. This technique involves altering the arrangement of a dataset by either pivoting, melting, or stacking columns to better suit the data analysis or visualization.
```python
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({
   'Name': ['John', 'Sara', 'Peter'],
   'Math': [90, 85, 95],
   'Science': [80, 95, 88],
   'English': [92, 91, 87]
})

df.head()
"""
    Name  Math  Science  English
0   John    90       80       92
1   Sara    85       95       91
2  Peter    95       88       87
"""

# Reshape the dataframe from wide to long format
df_long = pd.melt(df, id_vars=['Name'], value_vars=['Math', 'Science', 'English'],
                  var_name='Subject', value_name='Score')

df_long.head()
"""
    Name  Subject  Score
0   John     Math     90
1   Sara     Math     85
2  Peter     Math     95
3   John  Science     80
4   Sara  Science     95
"""
```
## Conclusion
Data wrangling is an essential stage in data science processes. By cleaning and transforming data, we can ensure that our analysis is accurate and reliable. Although the data wrangling process may consume a considerable amount of time, it's important to invest the necessary time and effort to ensure that our analysis is based on high-quality data.

---
If you’re interested in learning more about data science, be sure to [follow me on Medium](https://medium.com/@armantunga) and check out my other articles. And if you have any questions or comments, please feel free to [reach out to me on LinkedIn](https://www.linkedin.com/in/armantunga/). I’m always eager to connect with fellow data enthusiasts and continue the conversation.

*Connect with me on… [LinkedIn](https://www.linkedin.com/in/armantunga/), or [GitHub](https://github.com/ArmanTunga)*