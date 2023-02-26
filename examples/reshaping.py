import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({
   'Name': ['John', 'Sara', 'Peter'],
   'Math': [90, 85, 95],
   'Science': [80, 95, 88],
   'English': [92, 91, 87]
})

df.head()

# Reshape the dataframe from wide to long format
df_long = pd.melt(df, id_vars=['Name'], value_vars=['Math', 'Science', 'English'],
                  var_name='Subject', value_name='Score')

df_long.head()