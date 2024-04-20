import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Use raw strings for file paths
movies = pickle.load(open(r"D:\Downloads\python intern\2\movies_list.pkl", 'rb'))
similarity = pickle.load(open(r"D:\Downloads\python intern\2\similarity.pkl", 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommender System")

imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
]

st.image(imageUrls, width=200)

select_value = st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

if st.button("Show Recommendations"):
    movie_names, movie_posters = recommend(select_value)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_names[0])
        st.image(movie_posters[0], width=200)
    with col2:
        st.text(movie_names[1])
        st.image(movie_posters[1], width=200)
    with col3:
        st.text(movie_names[2])
        st.image(movie_posters[2], width=200)
    with col4:
        st.text(movie_names[3])
        st.image(movie_posters[3], width=200)
    with col5:
        st.text(movie_names[4])
        st.image(movie_posters[4], width=200)
