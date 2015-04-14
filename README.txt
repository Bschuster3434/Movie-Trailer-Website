Movie Trailer Website
by Brian Schuster
Created on April 9th, 2015
-----------------------------------------------------------------
EXPLANATION OF WEBSITE FUNCTION

This website is a dynamically created movie poster website,
created for the 'Programming Foundations with Python' course
on Udacity.com.

The original site is designed to present of a list of pre-defined
movies and allow you to 'click' on a movie poster and show a film.
I will be modifying this base template in the following ways:

- Adding multiple categories of films via a menu at the top, and
  populating each group with their own genre (documentary, drama,
  animated films)
- Adding a link to the amazon page to allow for the purchase of
  the film from amazon.com
- Adding a UI Page to allow for dynamically adding films to the
  list without having to interact with the programming language
  directly (requires the code to be re-compiled)
  
-----------------------------------------------------------------
SYSTEM REQUIREMENTS

 - Windows 7
 - Python 2.7.9
   - Download Link: https://www.python.org/downloads/
 - MAMP for Windows Alpha 3
   - Download Link: https://www.mamp.info/en/mamp_windows.html
 - Installation of GitHub for Windows (or a comparable git dist)
   - Download Link: https://windows.github.com/
   
-----------------------------------------------------------------
IMPLEMENTATION STEPS

1) Install the latest version of python onto you Windows machine
  - Read this guide for additional information: 
	   https://docs.python.org/2/using/windows.html
2) Install 'MAMP for Windows Alpha 3'
3) Install GitHub or a comparable git distribution
4) In your local install of MAMP, locate '../MAMP/htdocs/'. This is
   the working directory for the MAMP webserver.
5) Open the directory in your terminal program and run the
   following command: 
       git clone https://github.com/Bschuster3434/Movie-Trailer-Website.git
   Alternatively, you can download the ZIP from the link from here:
       https://github.com/Bschuster3434/Movie-Trailer-Website
6) In the MAMP GUI, open preferences and change the
      'Start page url' to '/www' then click 'OK'
7) After the server restarts, click 'Open start page' to go to the
      website