import pandas as pd
import streamlit as st
import requests
import json
#import pydeck as pdk
import numpy as np



#print("hello")

response=requests.get("http://api.open-notify.org/astros.json")

astronauts=json.loads(response.text)

#description about the page
st.markdown("# Astronaut Dashboard")
st.markdown('_This dashboard shows up-to-date information about current space actitivies_ :rocket:')

st.write('There are currently', astronauts["number"], ' humans in space:')

#print out all names of people in space

for astro in astronauts["people"]:
    st.markdown(astro["name"])


iss_response=requests.get("http://api.open-notify.org/iss-now.json")
iss=json.loads(iss_response.text)

lat=float(iss['iss_position']['latitude'])
long=float(iss['iss_position']['longitude'])

iss_position= pd.DataFrame(np.array([[lat,long]]), columns=["lat","lon"])

st.markdown('_The position of ISS is shown below by the red circle:_')

st.map(iss_position)



# st.pydeck_chart(pdk.Deck(
#      map_style='mapbox://styles/mapbox/light-v9',
#     #  initial_view_state=pdk.ViewState(
#     #      longitude=long,
#     #      latitude=lat
#     #  ),
#      layers=[
#          pdk.Layer(
#              'ScatterplotLayer',
#              data=iss_position,
#              get_position='[longitude,latitude]',
#              get_color='[200, 30, 0, 160]',
#              get_radius=300000,
#          ),
#      ],
#      ))
