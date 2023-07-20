import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'browser'

india_states = json.load(open("states_india.geojson", "r"))

# print(india_states['features'][0]['properties'])

state_id_map = {}
for feature in india_states["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]

df = pd.read_csv("StatewiseTestingDetails.csv")
# df["Density"] = df["Density[a]"].apply(lambda x: int(x.split("/")[0].replace(",", "")))
df["TotalSamples"]
df["id"] = df["State"].apply(lambda x: state_id_map[x])

print(df.head())    

df["TotalSamplesScale"] = np.log10(df["TotalSamples"])

fig = px.choropleth_mapbox(
    df,
    locations="id",
    geojson=india_states,
    color="TotalSamples",
    hover_name="State",
    hover_data=["TotalSamples"],
    title="India Covid",
    mapbox_style="carto-positron",
    center={"lat": 22, "lon": 78},
    zoom=3.5,
    opacity=0.5,
)
fig.show()

