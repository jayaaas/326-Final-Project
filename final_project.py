#Movie class
#contains file that has all movies in database (need to find movie database)

#__init__
'''initializes movie class'''

#clean_up function
''' cleans up data for each movie, makes it easier to access and parse through data
args: file that has data for each movie 
returns: cleaned up version of information about movie 
'''

assert(movie_data) == "Soul Surfer, Drama, PG, 1.75 hours"
assert(movie_data) == "Barbie, Fantasy, PG-13, 2 hours"
assert(movie_data) == "Old Dads, Comedy, R, 1.75 hours"

#check_movie function
'''check for movie within dataset to ensure it fits criteria that user asks for
args: genre, rating, duration
returns: name of movie'''

assert("comedy", "R", 1.75) == "Hot Tub Time Machine"
assert("fantasy", "PG", 1.5) == "Shrek"
assert("family", "G", 2) == "Cars"
assert("horror", "PG-13", 1.5) == "The Boogeyman"

#get_matches function
'''finds a list of matches to display to user
returns: list of movies that matches what the user put in'''

assert(user_inputs) == ["Murder Mystery, Grown Ups, The Do-Over, Blended, Just Go With It"]
assert(user_inputs) == ["Shrek, Cars, Mall Cop, The Lorax, Planes, Wall-e"]

#filter_movies
'''helps user filter out results
args: result of get_matches
returns: more specific list of movies'''

assert(get_matches) == ["Grown-Ups, Blended"]
assert(get_matches) == ["Cars, Planes"]