import streamlit as st
import pandas as pd
import pickle

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [movies.iloc[i[0]].title for i in movie_list]
    return recommended_movies

# Load data
movies_dict = pickle.load(open('movie_dict_list.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit App Layout
st.set_page_config(page_title='Movie Recommender System', layout='wide')

# Add background style
st.markdown(
    """
    <style>
    body {
        background-color: #f5f7fa;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .recommend-card {
        transition: transform 0.3s ease-in-out;
    }
    .recommend-card:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    footer {
        visibility: hidden;
    }
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 10px;
        background-color: #4CAF50;
        color: white;
        text-align: center;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title with custom styling
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🎬 Movie Recommender System 🎥</h1>",
    unsafe_allow_html=True,
)

# Subtitle with styling
st.markdown(
    "<p style='text-align: center; font-size: 18px;'>Find your next favorite movie based on your choice!</p>",
    unsafe_allow_html=True,
)

# Create a centered layout
st.write("---")
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    selected_movie_name = st.selectbox(
        "Select a Movie",
        movies['title'].values,
        help="Select a movie to get personalized recommendations.",
    )

# Recommend button
if st.button("Recommend 🎬"):
    with st.spinner("Fetching recommendations..."):
        recommendations = recommend(selected_movie_name)

    # Display recommendations in a grid
    st.write("---")
    st.subheader("Here are the top recommendations for you:")

    # Create a grid layout for recommendations
    cols = st.columns(5)
    for idx, movie in enumerate(recommendations):
        with cols[idx]:
            st.markdown(
                f"""
                <div class="recommend-card" style="padding: 10px; border: 2px solid #4CAF50; border-radius: 10px; background-color: #f9f9f9; text-align: center;">
                    <h3 style="font-size: 16px; color: #333;">{movie}</h3>
                </div>
                """,
                unsafe_allow_html=True,
            )

# Add footer
st.markdown(
    """
    <div class="footer">
        <p>✨ Built with ❤️ by Sumit and Tanishq | Find your next favorite movie! ✨</p>
    </div>
    """,
    unsafe_allow_html=True,
)
