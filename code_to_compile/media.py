class Movie():
	""" This class provides a way to store movie related information """

	def __init__(self, movie_title, poster_image, trailer_youtube, genre, amazon_link):
		# Creating the variables that I will need to create the 'Fresh Tomatoes' Website
		self.title = movie_title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.genre = genre
		self.amazon_link = amazon_link
		