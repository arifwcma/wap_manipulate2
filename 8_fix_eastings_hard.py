import pandas as pd
import re
from pyproj import Transformer
from pyproj import Transformer
import pandas as pd

df = pd.read_csv("qgis/data/Master5.csv")

df.loc[df["New Site Code"] == "WAP_2025_08_00533", "Easting GDA 94 (start of works only)"] = 694010
df.loc[df["New Site Code"] == "WAP_2025_08_00579", "Easting GDA 94 (start of works only)"] = 681500

transformer = Transformer.from_crs("EPSG:28354", "EPSG:4326", always_xy=True)

for code in ["WAP_2025_08_00533", "WAP_2025_08_00579"]:
    row = df.loc[df["New Site Code"] == code].iloc[0]
    x = float(row["Easting GDA 94 (start of works only)"])
    y = float(row["Northing GDA 94  (start of works only)"])
    lon, lat = transformer.transform(x, y)
    df.loc[df["New Site Code"] == code, "lon"] = lon
    df.loc[df["New Site Code"] == code, "lat"] = lat

df.to_csv("qgis/data/Master6.csv", index=False)


