import os, json
import pandas as pd
import plotly.express as px

dir_data_path = r'C:\Users\Kirill\Desktop\GEO\result'

list_json = list()
for f in os.listdir(dir_data_path):
    if f.find('data') > -1:
        print(f)
        with open(os.path.join(dir_data_path, f), 'r',) as f:
            read_json_data = json.load(f)
            list_json.append(read_json_data)

all_adr_coords = dict()
for d in list_json:
    all_adr_coords = all_adr_coords | d

lst = []

for name, adr in all_adr_coords.items():
    lst.append({"name":name, "adr":adr, "lat": adr[1], "lon": adr[0]})

df = pd.DataFrame(lst)
import random
df['size'] = random.randint(0, 100)

fig = px.scatter_geo(
        data_frame=df.sample(100),
        lat="lat",
        lon="lon",
        size="size",
        projection="natural earth",
    )

fig.write_html('geo.html')
