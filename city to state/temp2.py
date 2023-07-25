import pandas as pd


dt = naukri
# print(dt)
dt['City'] = naukri['City'].apply(cleaning)
print("THIS IS NAUKRI AFTER THE CLEANING:\n ", dt['City'])

cities_compare = pd.read_csv(r"C:\Users\TAMANG\Documents\GitHub\working-with-chartjs\city to state\Indian Cities Database.csv")
cities_compare['City'] = cities_compare['City'].apply(cleaning)
print('THIS IS CITY/STATE Compare after cleaning: \n', cities_compare)

for index, row in dt.iterrows():
    counter = 0
    try:
        city = row['City'].split()
    except Exception as e:
        counter = counter + 1
        print("EXCEPTION OCCURED IN SPLIT")
        pass
    try:
        for i in city:  
            matching_row = cities_compare.str.contains(i, case=False)
            dt = pd.concat([dt, matching_row])
            print(matching_row)
    except Exception as e:
        counter = counter + 1
        print("EXCEPTION OCCCURED", counter)
        pass
dt.to_excel('temp.xlsx')