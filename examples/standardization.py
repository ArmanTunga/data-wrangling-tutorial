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
