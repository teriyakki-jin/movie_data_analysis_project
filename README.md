# Movie Data Analysis Project

이 프로젝트는 [MovieLens](https://movielens.org)에서 제공하는 **ml-latest-small** 데이터셋을 이용하여 간단한 영화 데이터 분석과 시각화를 수행합니다.

## 구성

- `movies.csv`, `ratings.csv`, `tags.csv`, `links.csv` : MovieLens 데이터셋 파일
- `data_load.py` : Pandas를 사용해 데이터를 불러오는 예제 스크립트
- `movie_dataset_analysis.ipynb` : 데이터 탐색과 분석이 담긴 Jupyter 노트북
- `dashboard.py` : Streamlit 기반 대시보드 애플리케이션

## 실행 방법

필요한 패키지를 먼저 설치합니다.

```bash
pip install pandas streamlit matplotlib
```

대시보드를 실행하려면 다음 명령어를 사용합니다.

```bash
streamlit run dashboard.py
```

브라우저가 열리면 다양한 필터와 통계 정보를 통해 영화 평점 데이터를 탐색할 수 있습니다.

## 데이터 출처 및 라이선스

본 저장소에서 사용하는 데이터는 [GroupLens Research](https://grouplens.org/datasets/movielens/)에서 배포하는 MovieLens `ml-latest-small` 데이터셋입니다. 데이터에 대한 자세한 설명과 라이선스 정보는 `README.txt` 파일을 참고하세요.
