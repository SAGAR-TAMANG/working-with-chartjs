import pandas as pd

df = pd.read_excel("data.xlsx")

# df["Density"] = df["Density[a]"].apply(lambda x: int(x.split("/")[0].replace(",", "")))
# df["TotalSamples"]

# df["id"] = df["State"].apply(lambda x: state_id_map[x])

df2 = pd.DataFrame(df["State"].value_counts()).reset_index()

print(type(df2))
df2.to_excel('data2.xlsx')