import numpy as np
import pandas as pd

data = pd.read_csv('ratings.csv')
data.head(10)

movie_titles_genre = pd.read_csv("movies.csv")
movie_titles_genre.head(10)

data = data.merge(movie_titles_genre,on='movieId', how='left')
data.head(10)

Average_ratings = pd.DataFrame(data.groupby('title')['rating'].mean())
Average_ratings.head(10)

Average_ratings['Total Ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())
Average_ratings.head(10)

movie_user = data.pivot_table(index='userId',columns='title',values='rating')

movie_user.head(10)



correlations = movie_user.corrwith(movie_user['Toy Story (1995)'])
correlations.head()

recommendation = pd.DataFrame(correlations,columns=['Correlation'])
recommendation.dropna(inplace=True)
recommendation = recommendation.join(Average_ratings['Total Ratings'])
recommendation.head()


recc = recommendation[recommendation['Total Ratings']>100].sort_values('Correlation',ascending=False).reset_index()



recc = recc.merge(movie_titles_genre,on='title', how='left')
recc.head(10)
res = []
res.append(recommendation[recommendation['Total Ratings']>100].sort_values('Correlation',ascending=False).reset_index())
print(res)
