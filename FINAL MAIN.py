import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
import re
import string

from rapidfuzz import fuzz, process

naukri = pd.read_excel(r"C:\Users\TAMANG\Documents\GitHub\working-with-chartjs\city to state\NaukriJobListing_2023-07-24.xlsx")
india_states = json.load(open(r"C:\Users\TAMANG\Documents\GitHub\working-with-chartjs\city to state\states_india.geojson", "r"))

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
print('NUMBER OF EXCEPTION DURING CLEANING: ', counter)
print("**********************************************")

dt = naukri
dt['City'] = naukri['City'].apply(cleaning)
print("THIS IS NAUKRI AFTER THE CLEANING:\n ", dt['City'])
print("**********************************************")

cities_compare = pd.read_csv(r"C:\Users\TAMANG\Documents\GitHub\working-with-chartjs\city to state\Indian Cities Database.csv")
cities_compare['City'] = cities_compare['City'].apply(cleaning)
print('THIS IS CITY/STATE Compare after cleaning: \n', cities_compare)
print("**********************************************")

counter = 0
counter2 = 0
counter3 = 0
counter_page = 0

for index, row in dt.iterrows():
    try:
        city = row['City'].split()
        # print(city)
    except Exception as e:
        counter = counter + 1
        print("EXCEPTION OCCURED IN SPLIT", counter)
        pass
    
    try:
        city = row['City']
        print('---------------------------------------------------')

        # Initialize variables to keep track of best match and its score
        best_match = None
        best_score = 0

        for compare_city in cities_compare['City']:
            # Performing the fuzzy string matching for each city in cities_compare
            score = fuzz.QRatio(city, compare_city)

            # Updating the best_match and best_score if the current score is better
            if score > 50:
                best_match = compare_city
                best_score = score
        print("CITY:", city, "| Best Match:", best_match, "| with Score:", best_score)

        matched_rows = cities_compare[cities_compare['City'] == best_match]
        
        if not matched_rows.empty:
            state =  matched_rows['State Name'].iloc[0]
            print('BEST STATE: ', state)
            state_df = {
                'State': state
            }
        else:
            state = None
            state_df = {
                'State': [None]
            }
            print("STATE NOT FOUND.")
        
        try: 
            dt.at[counter_page, 'State'] = state
        except Exception as e:
            print('Exception occured as: ', e)
            pass
        counter_page = counter_page + 1
    except Exception as e:
        counter2 = counter2 + 1
        print("EXCEPTION OCCCURED IN CITY", counter2)
        pass


print("**********************************************")

dt.to_excel('visualization_data.xlsx')
# print('Number of Successful cities to:', counter3)

state_counts = dt['State'].value_counts()
print('STATES ALONG WITH ITS COUNTINGS: \n')
print(state_counts)

## PHASE TWO OF THE VISUALIZATION ##

print('**********************************************')

# BEGINS THE VISUALIZATION

pio.renderers.default = 'browser'

india_states = json.load(open("states_india.geojson", "r"))

state_id_map = {}
for feature in india_states["features"]:
    print(feature['properties']['st_nm'])
    feature["id"] = feature["properties"]["state_code"]
    statename_title= feature["properties"]["st_nm"].title()
    state_id_map[statename_title] = feature["id"]

print('**********************************************')

print('STATE ID MAP: \n', state_id_map)

df = pd.read_excel("visualization_data.xlsx")
df = df.dropna(subset=["State"])
df['State'] = df['State'].str.title()

df2 = pd.DataFrame(df["State"].value_counts()).reset_index()
df2["id"] = df2["State"].apply(lambda x: state_id_map[x])
print('\n HERE GOES df2: \n', df2)

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
fig.write_html('map_of_india.html')
fig.show()