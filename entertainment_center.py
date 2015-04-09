import media
import fresh_tomatoes

#Creating Movie Objects
###movie_title,  poster_image, trailer_youtube, genre, amazon_link
pirates_of_silicon_valley = media.Movie(movie_title = "Pirates of Silicon Valley",
	poster_image = "http://upload.wikimedia.org/wikipedia/en/3/30/Movieposterposv.jpg",
	trailer_youtube = "https://www.youtube.com/watch?v=lEyrivrjAuU",
	genre = "Drama",
	amazon_link = "http://www.amazon.com/Pirates-Silicon-Valley-Noah-Wyle/dp/B0009NSCS0/ref=sr_1_1?ie=UTF8&qid=1428574874&sr=8-1&keywords=Pirates+of+Silicon+Valley")
				   
the_social_network = media.Movie(movie_title = "The Social Network",
	poster_image = "http://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
	trailer_youtube = "https://www.youtube.com/watch?v=lB95KLmpLR4",
	genre = "Drama",
	amazon_link = "http://www.amazon.com/Social-Network-Jesse-Eisenberg/dp/B004HWR406/ref=sr_1_1?ie=UTF8&qid=1428575594&sr=8-1&keywords=The+Social+Network")

queen_of_versailles = media.Movie(movie_title = "The Queen of Versailles", 
	poster_image = "http://foreveryoungadult.com/_uploads/images/29540/thequeenofversailles__span.jpg", 
	trailer_youtube = "https://www.youtube.com/watch?v=AdJYzgJ4CwI",
	genre = "Documentary",
	amazon_link = "http://www.amazon.com/Queen-Versailles-Jackie-Siegel/dp/B00A6N7GMG/ref=sr_1_1?ie=UTF8&qid=1428575684&sr=8-1&keywords=the+queen+of+versailles")

jiro_dreams_of_sushi = media.Movie(movie_title = "Jiro Dreams of Sushi", 
	poster_image = "http://upload.wikimedia.org/wikipedia/en/4/47/Jiro_sushi_poster.jpg", 
	trailer_youtube = "https://www.youtube.com/watch?v=I1UDS2kgqY8",
	genre = "Documentary",
	amazon_link = "http://www.amazon.com/Jiro-Dreams-Sushi-Ono/dp/B008ODZEQ0/ref=sr_1_1?ie=UTF8&qid=1428575756&sr=8-1&keywords=jiro+dreams+of+sushi")
								   
up = media.Movie(movie_title = "Up",
	poster_image = "http://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
	trailer_youtube = "https://www.youtube.com/watch?v=ORFWdXl_zJ4",
	genre = "Animated",
	amazon_link = "http://www.amazon.com/Up-Ed-Asner/dp/B005ZMTXMY/ref=sr_1_1?ie=UTF8&qid=1428575943&sr=8-1&keywords=Up")
	
walle = media.Movie(movie_title = "WALL-E",
	poster_image = "http://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
	trailer_youtube = "https://www.youtube.com/watch?v=ZisWjdjs-gM",
	genre = "Animated",
	amazon_link = "http://www.amazon.com/gp/product/B003QTSMXE/ref=pd_cbs_mov_aiv_1")

movies = [pirates_of_silicon_valley, the_social_network, queen_of_versailles, jiro_dreams_of_sushi, up, walle]

fresh_tomatoes.open_movies_page(movies)
