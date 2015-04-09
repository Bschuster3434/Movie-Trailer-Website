import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life.",
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=4KPTXpQehio")
						
avatar = media.Movie("Avatar",
					 "A marine on an alien planet.",
					 "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

posv = media.Movie("Pirates of Silicon Valley",
				   "The story of the creation of the Personal Computer Revolution",
				   "http://upload.wikimedia.org/wikipedia/en/3/30/Movieposterposv.jpg",
				   "https://www.youtube.com/watch?v=lEyrivrjAuU")

queen_of_versailles = media.Movie("The Queen of Versailles", "Billionaire family falls into normalacy", "http://foreveryoungadult.com/_uploads/images/29540/thequeenofversailles__span.jpg", "https://www.youtube.com/watch?v=AdJYzgJ4CwI")
gone_girl = media.Movie("Gone Girl", "David Fincher's film based off the best selling book by Gillian Flynn", "http://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg", "https://www.youtube.com/watch?v=Ym3LB0lOJ0o")
jiro_dreams_of_sushi = media.Movie("Jiro Dreams of Sushi", "Documentary following Jiro Ono, sushi master and owner of Sukiyabashi Jiro", "http://upload.wikimedia.org/wikipedia/en/4/47/Jiro_sushi_poster.jpg", "https://www.youtube.com/watch?v=I1UDS2kgqY8")

movies = [toy_story, avatar, posv, queen_of_versailles, gone_girl, jiro_dreams_of_sushi]

fresh_tomatoes.open_movies_page(movies)
