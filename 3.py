import pandas as pd
df = pd.read_csv("data.csv")
df["Total"] = df["Marks"] + 10
df.rename(columns={"Marks": "Score"}, inplace=True)
df.fillna(0, inplace=True)
df.drop_duplicates(inplace=True)
print("Modified Data:\n", df)