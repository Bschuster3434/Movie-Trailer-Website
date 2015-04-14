import media
import fresh_tomatoes
import csv

# Creating Movie Objects
### Below are the variables necessary to create a full movie object
### movie_title,  poster_image, trailer_youtube, genre, amazon_link

# Creating the list variable for the movies
movies = []

# Opening the csv file and reading the list of movies into a list
with open('additional_movies.csv', 'rb') as f:
	csv_reader = csv.reader(f)
	# Eliminating the Header Row with the [1:]
	new_movie_records = [row for row in csv_reader][1:] 

# The following loop is taking the csv file and parsing it into the
# python movie object created in 'media'. The csv will always have
# the same order, so the numeric place of the correct data element
# will be preserved.
for record in new_movie_records:
	next_movie = media.Movie(movie_title = record[0],
		poster_image = record[1],
		trailer_youtube = record[2],
		amazon_link = record[3],
		genre = record[4].strip())
	movies.append(next_movie)

# Opening fresh_tomatoes to create the html file
fresh_tomatoes.open_movies_page(movies)