import cgi

print "Content-type: text/html"

print """
<html>

<head><title>Printing Movie Name</title></head>

<body>

	<h3>Movie Name Entered:</h3>
"""

form = cgi.FieldStorage()
movie_name = form.getvalue("Movie Name", 'movie_name')

print """
</body>
</html>
"""