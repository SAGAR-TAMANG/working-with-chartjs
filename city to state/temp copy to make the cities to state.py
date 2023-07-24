import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
import re
import string
pio.renderers.default = 'browser'

naukri = pd.read_excel(r"C:\Users\TAMANG\Documents\GitHub\working-with-chartjs\city to state\NaukriJobListing_2023-07-24.xlsx")
india_states = json.load(open(r"C:\Users\TAMANG\Documents\GitHub\working-with-chartjs\city to state\states_india.geojson", "r"))

# print(india_states['features'][0]['properties'])
counter = 0
def cleaning(text):
    global counter
    try:
        # converting to lowercase, removing URL links, special characters, punctuations...
        text = text.lower()
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('[’“”…]', '', text)
        return text
    except Exception as e:
        counter = counter + 1
        print("EXCEPTION NUMBER: ", counter)
        pass

dt = naukri
# print(dt)
dt['City'] = naukri['City'].apply(cleaning)
print("THIS IS AFTER THE CLEANING: ", dt['City'])

# state_id_map = {}
# for feature in india_states["features"]:
#     # print('FEATURE  :', feature)
#     feature["id"] = feature["properties"]["state_code"]
#     # print("FEATURE's ID :", feature['id'])
#     state_id_map[feature["properties"]["st_nm"]] = feature["id"]


# df = pd.read_csv("StatewiseTestingDetails.csv")
# # df["Density"] = df["Density[a]"].apply(lambda x: int(x.split("/")[0].replace(",", "")))
# df["TotalSamples"]
# df["id"] = df["State"].apply(lambda x: state_id_map[x])


# print(df.head())    

