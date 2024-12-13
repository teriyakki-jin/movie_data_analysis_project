
# 파일 경로 설정
movies_file = "path_to_dataset/movies.csv"
ratings_file = "path_to_dataset/ratings.csv"

# 데이터 로드
movies = pd.read_csv(movies_file)
ratings = pd.read_csv(ratings_file)

# 데이터 확인
print(movies.head())
print(ratings.head())
