import pickle
import streamlit as st

# Load preprocessed data and models
st.set_page_config(page_title="🎵 Music Recommender System", layout="wide")

st.markdown("""
    <style>
    .title-text {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: white;
    }
    .recommendation-container {
        display: flex;
        justify-content: center;
        gap: 20px;
    }
    .stText {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='title-text'>🎶 Music Recommender System 🎶</div>", unsafe_allow_html=True)

# Load data
music = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

music_list = music['song'].values
selected_song = st.selectbox(
    "🎼 Type or select a song from the dropdown:",
    music_list
)

def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = [music.iloc[i[0]].song for i in distances[1:6]]
    return recommended_music_names

if st.button('🔍 Show Recommendations'):
    recommended_music_names = recommend(selected_song)
    
    st.markdown("<h3 style='text-align: center;'>🎧 Recommended Songs:</h3>", unsafe_allow_html=True)
    
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.markdown(f"<p style='text-align: center; font-size: 18px; font-weight: bold;'>{recommended_music_names[i]}</p>", unsafe_allow_html=True)
            #st.image("https://i.postimg.cc/0QNxYz4V/social.png", use_column_width=True)

st.sidebar.write("🎶 Enjoy your personalized playlist!")
