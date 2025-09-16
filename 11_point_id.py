import pandas as pd

df = pd.read_csv("qgis/data/Master6.csv")
df["Point ID"] = df.groupby("New Site Code").cumcount() + 1
df["Point ID"] = df["New Site Code"].astype(str) + "_" + df["Point ID"].astype(str)
df.to_csv("qgis/data/Master7.csv", index=False)
