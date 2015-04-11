import cgi

form = cgi.FieldStorage()
movie_name = form.getvalue('movie_name')
print movie_name