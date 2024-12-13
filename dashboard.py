import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
movies_file = "movies.csv"
ratings_file = "ratings.csv"

movies = pd.read_csv(movies_file)
ratings = pd.read_csv(ratings_file)
data = pd.merge(ratings, movies, on="movieId")

# 앱 제목
st.title("MovieLens Dashboard")
st.sidebar.title("Filters")

# 필터: 영화 장르 선택
genres = data['genres'].str.get_dummies(sep='|').columns
selected_genre = st.sidebar.selectbox("Select a Genre", ["All"] + list(genres))

# 필터 데이터 적용
if selected_genre != "All":
    data = data[data['genres'].str.contains(selected_genre, na=False)]

# 데이터 통계
st.header("Summary Statistics")
st.write(data.describe())

# 영화별 평점 분포
st.header("Ratings Distribution")
fig, ax = plt.subplots()
data['rating'].hist(bins=10, ax=ax)
ax.set_title("Ratings Distribution")
ax.set_xlabel("Rating")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# 가장 인기 있는 영화
st.header("Top 10 Movies")
top_movies = (
    data.groupby("title")["rating"]
    .agg(["mean", "count"])
    .rename(columns={"mean": "Average Rating", "count": "Number of Ratings"})
    .sort_values(by="Number of Ratings", ascending=False)
    .head(10)
)
st.write(top_movies)
