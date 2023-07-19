import json
import pandas as pd
import plotly.express as px

# pio.renderers.default = 'chrome'

indian_states = json.load(open('states_india.geojson', 'r'))

print(indian_states['id'])

df = pd.read_csv('StatewiseTestingDetails.csv')

state_id_map = {}

# for feature in indian_states['features']:
#     feature['id'] = 