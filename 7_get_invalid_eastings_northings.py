import pandas as pd
import re

def extract_first_number_6_or_more_digits(s):
    s = str(s).replace(",", "")
    m = re.search(r"\d{6,}", s)
    return m.group(0) if m else None

df = pd.read_csv("arcgis/data/Master5.csv")
parsed = df["Northing GDA 94  (start of works only)"].apply(extract_first_number_6_or_more_digits)
df["Parsed Northing"] = parsed
bad = df.loc[parsed.isna() | (parsed.str.len() != 7), ["New Site Code", "Parsed Northing", "Northing GDA 94  (start of works only)"]]
print(bad)

parsed = df["Easting GDA 94 (start of works only)"].apply(extract_first_number_6_or_more_digits)
df["Parsed Easting"] = parsed
bad = df.loc[parsed.isna() | (parsed.str.len() != 6), ["New Site Code", "Parsed Easting", "Easting GDA 94 (start of works only)"]]
print(bad)
