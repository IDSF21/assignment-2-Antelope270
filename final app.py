#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from pandas.core.base import DataError
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import altair as alt



Image = Image.open('C:\\Users\\Antelope Cai\\Desktop\\spotify.gif')
st.image(Image,width=150)
st.title('Guess your favorite song!')
st.caption('The dataset is from Kaggle, 2020-2021')


def load_data():
    data = pd.read_csv('C:\\Users\\Antelope Cai\\Desktop\\CMU\\IDS\\spotify_dataset.csv')
    return data


data = load_data()
df = pd.DataFrame(data,columns=(['Song Name','Popularity','Release Date','Artist','Danceability','Acousticness','Energy','Valence']))
df= df.astype('string')
song=df[~df['Energy'].isin([' '])]
song['Energy']=song['Energy'].astype(float)
song['Acousticness']=song['Acousticness'].astype(float)
song['Valence']=song['Valence'].astype(float)
song['Danceability']=song['Danceability'].astype(float)
song['Popularity']=song['Popularity'].astype(float)
song.reset_index(drop=True, inplace=True)

# st.dataframe(song)

# data type test
# new_song=song.rename(columns = {
#     col : f"{col} ({dtype})"
#     for col, dtype in song.dtypes.to_dict().items()
# }).head()

# st.dataframe(new_song)

#selector filter
st.markdown("### 1. What is the relationship between song features and popularity?")
option = st.selectbox(
     'Select a audio feature you want to see the relationship bewteen it and popularity?',
     ('Danceability', 'Acousticness', 'Energy', 'Valence'))

st.write('You selected:', option)


# Basic Altair line chart changed from selection
st.markdown("#### Outcome: line chart")
basic_chart = alt.Chart(song).mark_line().encode(
    x='Popularity',
    y=option,
).properties(
    width=700,
    height=400
).configure_mark(
    color='green'
)
st.altair_chart(basic_chart)

#slider filter
st.markdown("### 2. Use the song feature sliders to filter your favorite song!")
dance_min = min(song['Danceability'])
dance_max = max(song['Danceability'])

acoust_min= min(song['Acousticness'])
acoust_max= max(song['Acousticness'])

energy_min = min(song['Energy'])
energy_max = max(song['Energy'])

valence_min = min(song['Valence'])
valence_max = max(song['Valence'])


sliders = {
    "Danceability": st.slider(
        "What is your desired Danceability?", dance_min, dance_max, 0.56
    ),

    "Acousticness":st.slider(
        "What is your desired Acousticness?", acoust_min, acoust_max, 0.495
    ),

    "Energy":st.slider(
        "What is your desired Energy?", energy_min, energy_max, 0.51
    ),
    "Valence":st.slider(
        "What is your desired Valence?", valence_min, valence_max, 0.50
    ),
    
}

filter = np.full(1545, True)  # Initialize filter as only True

st.markdown("#### Outcome: Filtered Spotify song table")
for feature_name, slider in sliders.items():
    # Here we update the filter to take into account the value of each slider
    filter = (
        filter
         & (song[feature_name] >= slider)
    )
filter.reset_index(drop=True, inplace=True)

st.write(song[filter])

with st.sidebar:
    st.header('Appendix')
    with st.expander("Spotify Audio Feature definitions"):
            st.subheader("Danceability")
            st.markdown("Describes how suitable a track is for dancing based on a "+
                    "combination of musical elements including tempo, rhythm stability, beat strength, "+
                    "and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.")

            st.subheader("Acousticness")
            st.markdown("A confidence measure from 0.0 to 1.0 of whether the "+
                    "track is acoustic. 1.0 represents high confidence the track is acoustic.")

            st.subheader("Energy")
            st.markdown("Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity "+
                    "and activity. Typically, energetic tracks feel fast, loud, and noisy."+
                    "For example, death metal has high energy, while a Bach prelude scores low on the scale. "+
                    "Perceptual features contributing to this attribute include dynamic range, perceived loudness, "+
                    "timbre, onset rate, and general entropy.")

            st.subheader("Valence")
            st.markdown("A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. "+
            "Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low"+
            "valence sound more negative (e.g. sad, depressed, angry).")