import pandas as pd

file = "datasets/TMDB_movie_dataset_v11.csv"
data = pd.read_csv(file)
# print(data.head(10))
drop1 = data.drop(columns=['id','original_language', 'original_title','release_date','revenue','runtime','adult','backdrop_path','budget','homepage','imdb_id','overview','poster_path','tagline','production_companies','production_countries','spoken_languages','keywords'])
drop1 = drop1.dropna(subset=['title'])
dataR = drop1.fillna({'genres': 'drama'})
print(dataR.head())
print(dataR.isnull().sum())
# print(drop1.duplicated().sum())
dataR.to_csv('new_loan_data.csv', mode='w', header=True, index=False)
