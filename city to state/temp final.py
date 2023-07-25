import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
import re
import string
# pio.renderers.default = 'browser'
from rapidfuzz import fuzz, process


naukri = pd.read_excel(r"C:\Users\TAMANG\Documents\GitHub\working-with-chartjs\city to state\NaukriJobListing_2023-07-24.xlsx")
india_states = json.load(open(r"C:\Users\TAMANG\Documents\GitHub\working-with-chartjs\city to state\states_india.geojson", "r"))

# print(india_states['features'][0]['properties'])
counter = 0
def cleaning(text):
    global counter
    try:
        # converting to lowercase, removing URL links, special characters, punctuations...
        text = text.lower()
        text = re.sub('https?://\S+|www\.\S+', ' ', text)
        text = re.sub('<.*?>+', ' ', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
        text = re.sub('\n', ' ', text)
        text = re.sub('[’“”…]', '', text)
        return text
    except Exception as e:
        counter = counter + 1
        print("EXCEPTION  OCCURED CLEANING: ", counter)
        pass

dt = naukri
# print(dt)
dt['City'] = naukri['City'].apply(cleaning)
print("THIS IS NAUKRI AFTER THE CLEANING:\n ", dt['City'])

cities_compare = pd.read_csv(r"C:\Users\TAMANG\Documents\GitHub\working-with-chartjs\city to state\Indian Cities Database.csv")
cities_compare['City'] = cities_compare['City'].apply(cleaning)
print('THIS IS CITY/STATE Compare after cleaning: \n', cities_compare)

counter = 0
counter2 = 0
counter3 = 0

print("**********************************************")
df_merged = pd.DataFrame(columns=['City', 'State'])

for index, row in dt.iterrows():
    try:
        city = row['City'].split()
        print(city)
    except Exception as e:
        counter = counter + 1
        print("EXCEPTION OCCURED IN SPLIT", counter)
        pass
    try:
        match, score = process.extractOne(city, cities_compare['City'].tolist(), scorer=fuzz.partial_ratio)
        print("Closest Match:", match, "with Score:", score)
        
        # Get the corresponding state from cities_compare
        state = cities_compare[cities_compare['City'] == match]['State'].iloc[0]
        print("State:", state)
        df_merged = pd.merge(naukri, cities_compare, on='City', how='left')
    except Exception as e:
        counter2 = counter2 + 1
        print("EXCEPTION OCCCURED IN CITY", counter)
        pass
df_merged.to_excel('temp.xlsx')
# print('Number of Successful cities to:', counter3)