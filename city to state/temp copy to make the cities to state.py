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
        text = re.sub('https?://\S+|www\.\S+', ' ', text)
        text = re.sub('<.*?>+', ' ', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
        text = re.sub('\n', ' ', text)
        text = re.sub('[’“”…]', '', text)
        return text
    except Exception as e:
        counter = counter + 1
        print("EXCEPTION NUMBER: ", counter)
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
        for i in city:  
            matching_row = cities_compare[cities_compare['City'].str.contains(i, case=False)]
            print(matching_row)
            df_merged = pd.concat([dt, matching_row])
    except Exception as e:
        counter2 = counter2 + 1
        print("EXCEPTION OCCCURED IN CITY", counter)
        pass
df_merged.to_excel('temp.xlsx')
# print('Number of Successful cities to:', counter3)