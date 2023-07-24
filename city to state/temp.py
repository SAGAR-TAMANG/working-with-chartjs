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
    # print('FEATURE  :', feature)
    feature["id"] = feature["properties"]["state_code"]
    # print("FEATURE's ID :", feature['id'])
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]
    
print(state_id_map)


df = pd.read_csv("StatewiseTestingDetails.csv")
# df["Density"] = df["Density[a]"].apply(lambda x: int(x.split("/")[0].replace(",", "")))
df["TotalSamples"]
df["id"] = df["State"].apply(lambda x: state_id_map[x])


print(df.head())    
