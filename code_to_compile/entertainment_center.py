import fresh_tomatoes
import csv

# Creating Movie Object for use with 'fresh_tomatoes.py'
# The class was originally apart of its own file, but the
# only significant function was __init__, so I deleted
# the file and added it below.

class Movie():
	""" This class provides a way to store movie related information."""

	def __init__(self, movie_title, poster_image, trailer_youtube, genre, amazon_link):
		# Creating the variables that I will need to create the 'Fresh Tomatoes' Website
		self.title = movie_title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.genre = genre
		self.amazon_link = amazon_link
		

# Creating the list variable for the movies
movies = []

# Opening the csv file and reading the list of movies into a list.
# This list came pre-populated with some of my favorite movies, but
# has also been extended using the UI form in 'add_movie.html'
with open('additional_movies.csv', 'rb') as f:
	csv_reader = csv.reader(f)
	# Eliminating the Header Row with the [1:]
	new_movie_records = [row for row in csv_reader][1:] 

# The following loop is taking the csv file and parsing it into the
# python movie object created in 'media'. The csv will always have
# the same order, so the numeric place of the correct data element
# will be preserved.
for record in new_movie_records:
	next_movie = Movie(movie_title = record[0],
		poster_image = record[1],
		trailer_youtube = record[2],
		amazon_link = record[3],
		genre = record[4].strip())
	movies.append(next_movie)

# Opening fresh_tomatoes to create the html file
fresh_tomatoes.open_movies_page(movies)