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