# assignment-2-Antelope270
assignment-2-Antelope270 created by GitHub Classroom
### 1. What is included in the assigment?
- A python file named final app.py
- A screencast recoding video of the app
- A spotify song dataset: spotify_dataset.csv
- A image of spotify logo: spotify.gif
- A README.md file which explain the description of the goals, rationale for my design decisions and overview of my development process.

### 2. What is the goal of this app?
Use the dataset Spotify Top 200 Charts (2020-2021) to: 
- Provide users a interactive line chart to display explorable data relationships between Audio features (Danceability, Acousticness, Energy, Valence)
- Provide users interactive sliders to select value of Danceability, Acousticness, Energy, Valence to select user's desirable songs.

### 3. Overview of my development process
- Import the data set and build a title
- Clean the data (some of the columns have NaN and ' ')
- Adjust the data types (to string or float)
- Reset the index of data
- Make relationship line chart between song features and popularity 
  -  Make a selectbox between song features: Danceability, Acousticness, Energy, Valence
  -  Draw 4 song featured line charts for selection outcome
- Make sliders filter
  - Draw 4 sliders for dragging
  - Display the filtered song table  
