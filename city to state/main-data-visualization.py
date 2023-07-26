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
    print(feature['properties']['st_nm'])
    feature["id"] = feature["properties"]["state_code"]
    statename_title= feature["properties"]["st_nm"].title()
    state_id_map[statename_title] = feature["id"]
    # state_id_map[feature["properties"]["st_nm"]] = 

print(state_id_map)

df = pd.read_excel("data.xlsx")
df = df.dropna(subset=["State"])
df['State'] = df['State'].str.title()

# df["Density"] = df["Density[a]"].apply(lambda x: int(x.split("/")[0].replace(",", "")))
# df["TotalSamples"]


# state_counts = df['State'].value_counts().reset_index()
# print('STATE COUNT:', state_counts)

# df["id"] = df["State"].apply(lambda x: state_id_map[x])
# state_counts["id"] = df["State"].apply(lambda x: state_id_map[x])

df2 = pd.DataFrame(df["State"].value_counts()).reset_index()
df2["id"] = df2["State"].apply(lambda x: state_id_map[x])
print(df2)    

# df["TotalSamplesScale"] = np.log10(df["TotalSamples"])

fig = px.choropleth_mapbox(
    df2,
    locations="id",
    geojson=india_states,
    color="State",
    hover_name="State",
    hover_data=["count"],
    title="Map of India showing the job listings",
    mapbox_style="carto-positron",
    center={"lat": 22, "lon": 78},
    zoom=3.5,
    opacity=0.5,
)
fig.write_html('india.main.html')
fig.show()