import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-image:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-image', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
top_main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="index.html">Top Movie Choices by Brian (All)</a>
		  </div>
          '''

header_bar = '''
			<div class="nav navbar-nav navbar-center">
			<li><a href="drama.html">Drama</a></li>
			<li><a href="documentary.html">Documentary</a></li>
			<li><a href="animation.html">Animation</a></li>
		    </div>
			<div class="nav navbar-nav navbar-right"> 
			<li><a href="add_movie.html">Add Movie</a></li>
			</div>
			'''
		  
end_main_page_content = '''
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center">
	<div class="movie-image" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
	</div>
    <h2>{movie_title}</h2>
	<a href="{amazon_link}" class="btn btn-default" role="button">Purchase on Amazon!</a>
	</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
			amazon_link = movie.amazon_link
        )
    return content

def create_add_movie_page():
  #  Creating the html to load the 'Add Movie' Page
  return None
  
  
def open_movies_page(movies):
  # Create or overwrite the output file
  main_output = open('../www/index.html', 'w')
  drama_output = open('../www/drama.html', 'w')
  documentary_output = open('../www/documentary.html', 'w')
  animation_output = open('../www/animation.html', 'w')
 
  ###Going through the movie choices and creating lists for each movie genre (for content generation)
  drama = []
  documentary = []
  animation = []
  for movie in movies:
	if movie.genre.lower() == 'drama':
		drama.append(movie)
	elif movie.genre.lower() == 'documentary':
		documentary.append(movie)
	elif movie.genre.lower() == 'animation':
		animation.append(movie)

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  main_page_content = top_main_page_content + header_bar + end_main_page_content
  all_rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Creating Genre Pages
  drama_rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(drama))
  documentary_rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(documentary))
  animation_rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(animation))

  # Output the file
  main_output.write(main_page_head + all_rendered_content)
  main_output.close()
  drama_output.write(main_page_head + drama_rendered_content)
  drama_output.close()
  documentary_output.write(main_page_head + documentary_rendered_content)
  documentary_output.close()
  animation_output.write(main_page_head + animation_rendered_content)
  animation_output.close()