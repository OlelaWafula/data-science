import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Merging on indexes
"""
Merging DataFrames on indexes.
"""
# Load movies data
movies = pd.read_csv('tmdb_movies.csv', index_col=['id'])
taglines = pd.read_csv('tmdb_taglines.csv', index_col=['id'])
print(movies.head())

# Merge on index
movies_taglines = movies.merge(taglines, on='id', how='left')
print(movies_taglines.head())

# Multi index merge

# Load data
samuel = pd.read_csv('samuel.csv', index_col=['movie_id', 'cast_id'])
casts = pd.read_csv('casts.csv', index_col=['movie_id', 'cast_id'])
movies_to_genres = pd.read_csv('tmdb_movies_genre.csv', index_col=['movie_id'])
print(samuel.head())
print(casts.head())
print(movies_to_genres.head())

# Merge on multi index
samuel_casts = samuel.merge(casts, on=['movie_id', 'cast_id'])
print(samuel_casts.head())
print(samuel_casts.shape)

# Index merge with left_on and right_on - when index names are different
movies_genres = movies.merge(movies_to_genres, left_on='id',
                             left_index=True, right_on=['movie_id'], right_index=True)
print(movies_genres.head())

# EXERCISE 

# Index merge for movie ratings
"""
*To practice merging on indexes, you will merge movies and a table called ratings that holds info about movie ratings. 

*Make sure your merge returns all of the rows from the movies table and not all the rows of ratings table need to be included in the result.
"""
# Load data 
ratings = pd.read_csv('ratings.csv', index_col=['id'])
print(ratings.head())

# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings, how='left', on=['id'])

# Print the first few rows of movies_ratings
print(movies_ratings.head())

# Do sequels earn more?
"""
*In this exercise, you'll find out which movie sequels earned the most compared to the original movie. 

*To answer this question, you will merge a modified version of the sequels and financials tables where their index is the movie ID. 

*You will need to choose a merge type that will return all of the rows from the sequels table and not all the rows of financials table need to be included in the result. 

*From there, you will join the resulting table to itself so that you can compare the revenue values of the original movie to the sequel. 

*Next, you will calculate the difference between the two revenues and sort the resulting dataset.
"""
# Load data
sequels = pd.read_csv('sequels.csv', index_col=['id'])
financials = pd.read_csv('financials.csv', index_col=['id'])
print(sequels.head())
print(financials.head())

# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel', 
                             right_on='id', right_index=True,
                             suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq 
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff 
titles_diff = orig_seq[['title_org','title_seq','diff']]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values(by='diff', ascending=False).head())