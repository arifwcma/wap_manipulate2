import pandas as pd
import re
from pyproj import Transformer

df = pd.read_csv("arcgis/data/Master5.csv")

df.loc[df["New Site Code"] == "WAP_2025_08_00533", "Easting GDA 94 (start of works only)"] = 694010
df.loc[df["New Site Code"] == "WAP_2025_08_00579", "Easting GDA 94 (start of works only)"] = 681500

df.to_csv("data/Master6.csv", index=False)

