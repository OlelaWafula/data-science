import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# Left Join - Merging two tables and returns all rows in the left table 
# only rows from right table where the keys match

# Load movies data
movies = pd.read_csv('tmdb_movies.csv')
print(movies.head())
print(movies.shape)

# Load tagline data
taglines = pd.read_csv('tmdb_taglines.csv')
print(taglines.head())
print(taglines.shape)

# Merge movies and taglines using Left Join
movies_taglines = movies.merge(taglines, on='id', how='left')
print(movies_taglines.head())
print(movies_taglines.shape)

# Counting missing rows with left join
"""
*The Movie Database is supported by volunteers going out into the world, 
collecting data, and entering it into the database. This includes 
financial data, such as movie budget and revenue. 
*If you wanted to know which movies are still missing data, you could use 
a left join to identify them. Practice using a left join by merging the 
movies table and the financials table.
"""
# Load financials data
financials = pd.read_csv('financials.csv')

# Merge the movies table with the financials table with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isnull().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)

# Enriching a dataset
"""
*Setting how='left' with the .merge()method is a useful technique for 
enriching or enhancing a dataset with additional information from a 
different table. 
*In this exercise, you will start off with a sample of movie data from 
the movie series Toy Story. Your goal is to enrich this data by adding 
the marketing tag line for each movie. 
*You will compare the results of a left join versus an inner join.
"""
# Load toy_story DataFrame
toy_story = pd.read_csv('toy_story.csv')

# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines, on='id', how='left')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines, on='id', how='inner')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# Other Joins

# Right Join - returns all rows in the right table only rows from left 
# table where the keys match

# Load Data movie_to_genres
movie_to_genres = pd.read_csv('tmdb_movie_to_genres.csv')

tv_genre = movie_to_genres[movie_to_genres['genre']=='TV Movie']
print(tv_genre)

# Merge with right join
tv_movies = movies.merge(tv_genre, how='right', left_on='id', 
                         right_on='movie_id')
print(tv_movies.head())

# Outer Join - Returns all of the rows from both tables regardless 
# if there is a match between the tables 

# Load data
family = pd.read_csv('tmdb_family.csv')
comedy = pd.read_csv('tmdb_comedy.csv')

# Merge with outer join
family_comedy = family.merge(comedy, how='outer', 
                             suffixes=('_fam', '_com'))
print(family_comedy)

# EXERCISE 

# Right join to find unique movies
"""
*Most of the recent big-budget science fiction movies can also be 
classified as action movies. 
*You are given a table of science fiction movies called scifi_movies 
and another table of action movies called action_movies. 
*Your goal is to find which movies are considered only science fiction 
movies. 
*Once you have this table, you can merge the movies table in to see 
the movie names. Since this exercise is related to science fiction 
movies, use a right join as your superhero power to solve this problem.
"""
# Load Data 
scifi_movies = pd.read_csv('tmdb_scifi_movies.csv')
action_movies = pd.read_csv('tmdb_action_movies.csv')

# Merge action_movies to the scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act','_sci'))

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(scifi_only, how='inner', left_on='id', right_on='movie_id')

# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)

# Popular genres with right join
"""
*What are the genres of the most popular movies? To answer this question, you need to merge data from the movies and movie_to_genres tables. In a table called pop_movies, the top 10 most popular movies in the movies table have been selected. 
*To ensure that you are analyzing all of the popular movies, merge it with the movie_to_genres table using a right join. 
*To complete your analysis, count the number of different genres. Also, the two tables can be merged by the movie ID. However, in pop_movies that column is called id, and in movies_to_genres it's called movie_id.
"""
# Load data
pop_movies = pd.read_csv('tmdb_pop_movies.csv')

# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = movie_to_genres.merge(pop_movies, how='right', 
                                      left_on='movie_id', 
                                      right_on='id')

# Count the number of genres
genre_count = genres_movies.groupby('genre').agg({'id':'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()

# Using outer join to select actors
"""
*One cool aspect of using an outer join is that, because it returns all rows from both merged tables and null where they do not match, you can use it to find rows that do not have a match in the other table. 

*To try for yourself, you have been given two tables with a list of actors from two popular movies: Iron Man 1 and Iron Man 2. Most of the actors played in both movies. Use an outer join to find actors who did not act in both movies.

*The Iron Man 1 table is called iron_1_actors, and Iron Man 2 table is called iron_2_actors. 
"""
# Load Data 
iron_1_actors = pd.read_csv('iron_1_actors.csv')
iron_2_actors = pd.read_csv('iron_2_actors.csv')

# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                     on='id',
                                     how='outer',
                                     suffixes=('_1', '_2'))

# Create an index that returns true if name_1 or name_2 are null
m = ((iron_1_and_2['name_1'].isnull()) | 
     (iron_1_and_2['name_2'].isnull()))

# Print the first few rows of iron_1_and_2
print(iron_1_and_2[m].head())

# Merging a table to itself - Self Join

# Load sequels data
sequels = pd.read_csv('sequels.csv')

# Self Join - using inner Join
original_sequels = sequels.merge(sequels, how='inner', left_on='sequel',
                                  right_on='id', suffixes=('_org', '_seq'))
print(original_sequels.head())

# Link each movie to its sequel using subsetting
print(original_sequels[:,['title_org', 'title_seq']].head())

# Self Join - using left Join
original_sequels = sequels.merge(sequels, how='left', left_on='sequel',
                                  right_on='id', suffixes=('_org', '_seq'))

# Circumstances of Self Join:
"""
*working with tables that have hierarchical relationships e.g. employee & manager.
*working with tables that have sequential relationships e.g. logistics
* Working with Graph data
"""

# EXERCISE 

# Self join
"""
*Merging a table to itself can be useful when you want to compare values in a column to other values in the same column. 

*In this exercise, you will practice this by creating a table that for each movie will list the movie director and a member of the crew on one row. 

*You have been given a table called crews, which has columns id, job, and name. First, merge the table to itself using the movie ID. This merge will give you a larger table where for each movie, every job is matched against each other. 

*Then select only those rows with a director in the left table, and avoid having a row where the director's job is listed in both the left and right tables. This filtering will remove job combinations that aren't with the director.
"""
# Load crews data
crews = pd.read_csv('crews.csv')

# Merge the crews table to itself
crews_self_merged = crews.merge(crews, on='id', how='inner',
                                suffixes=('_dir','_crew'))

# Create a boolean index to select the appropriate rows
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') & 
                  (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

# Print the first few rows of direct_crews
print(direct_crews.head())
