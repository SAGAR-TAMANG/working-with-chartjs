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

cities_compare = pd.read_csv(r"C:\Users\TAMANG\Documents\GitHub\working-with-chartjs\city to state\Indian Cities Database.csv")
cities_compare['City'] = cities_compare['City'].apply(cleaning)
print(cities_compare)

counter = 0

num_lines = dt.shape[0]

print('Number of lines in DataFrame :', num_lines)

for index, row in df.iterrows:
    print(row)