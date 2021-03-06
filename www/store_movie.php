<html>
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
		.header {
			margin-bottom: 50px;
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
<!DOCTYPE html>
<html lang="en">
  <body>
      <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="index.html">Top Movie Choices by Brian (All)</a>
		  </div>
		  	<div class="nav navbar-nav navbar-center">
			<li><a href="drama.html">Drama</a></li>
			<li><a href="documentary.html">Documentary</a></li>
			<li><a href="animation.html">Animation</a></li>
		    </div>
			<div class="nav navbar-nav navbar-right"> 
			<li><a href="add_movie.html">Add Movie</a></li>
			</div>
		</div>
      </div>
    </div>
		<!-- Form that grabs content -->
	<div class="container">
	<div class ="page-header">
		<h2>Thank You For Your Submission!</h2>
		<p>Your Submission Will Be Added Soon!</p>
			<?php
			
			//Opening the movie file in order to append the information from the 'add_movie.html' submission form
			
			$movie_file = fopen("../code_to_compile/additional_movies.csv","a+");
			
			fwrite($movie_file,"\r\n".$_POST["movie_name"].",".$_POST["poster_image"].",".$_POST["youtube_trailer"].",".$_POST["amazon_link"].",".$_POST["genre"]);
	
			fclose($movie_file);

			?>
		
	</div>

	</div>
	
	
  </body>
</html>