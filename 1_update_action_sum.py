import pandas as pd
import os
import tempfile

csv_path = r"arcgis/data\Master.csv"
output_path = r"arcgis/data\Master2.csv"
field_name = "Action "

mapping = {
    "Fencing & revegetation": "Fencing & Revegetation",
    "Platypus study": "Platypus Study"
}

df = pd.read_csv(csv_path, dtype=str, keep_default_na=False)
for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip()
df[field_name] = df[field_name].replace("", "Unknown").map(lambda v: mapping.get(v, v))

fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(csv_path), suffix=".csv")
os.close(fd)
df.to_csv(tmp_path, index=False)
os.replace(tmp_path, output_path)
