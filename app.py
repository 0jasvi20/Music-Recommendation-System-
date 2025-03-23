import pickle
import streamlit as st

# Function to recommend songs based on similarity
def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    for i in distances[1:6]:
        recommended_music_names.append(music.iloc[i[0]].song)
    return recommended_music_names

st.header('Music Recommender System')

# Load data
music = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

music_list = music['song'].values
selected_song = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)

if st.button('Show Recommendation'):
    recommended_music_names = recommend(selected_song)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_music_names[0])
    with col2:
        st.text(recommended_music_names[1])
    with col3:
        st.text(recommended_music_names[2])
    with col4:
        st.text(recommended_music_names[3])
    with col5:
        st.text(recommended_music_names[4])
