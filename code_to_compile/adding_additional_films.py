import media
import fresh_tomatoes
import csv

#Creating Movie Objects
###movie_title,  poster_image, trailer_youtube, genre, amazon_link

walle = media.Movie(movie_title = "WALL-E",
	poster_image = "http://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
	trailer_youtube = "https://www.youtube.com/watch?v=ZisWjdjs-gM",
	genre = "Animation",
	amazon_link = "http://www.amazon.com/gp/product/B003QTSMXE/ref=pd_cbs_mov_aiv_1")

movies = [walle]

##Adding additional films

with open('additional_movies.csv', 'rb') as f:
	csv_reader = csv.reader(f)
	new_movie_records = [row for row in csv_reader][1:]

for record in new_movie_records:
	next_movie = media.Movie(movie_title = record[0],
		poster_image = record[1],
		trailer_youtube = record[2],
		genre = record[3],
		amazon_link = record[4])
	movies.append(next_movie)
	

fresh_tomatoes.open_movies_page(movies)