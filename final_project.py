#Movie class
#contains file that has all movies in database (need to find movie database)
import pandas as pd

class Movie():

    def __init__(self, title, genre, rating, description, director):
        '''Initialize all of the attributes of the class'''
        self.title = title
        self.genre = genre
        self.rating = rating
        self.description  = description
        self.director = director

#clean_up function
    def get_data(path):
        ''' Gets values from the movies.csv file and stores them into variables.
        Only gets the data that we want from the file (title, genre, rating,
        description, and director) and disregards the other pieces of information. 
        
        Returns: a list of movies with movie objects in it.
'''
        movies = []
        data = pd.read_csv(path)

        for index, row in data.iterrows():
            title = row['title']
            genre = row['genre']
            rating = row['rating']
            description = row['description']
            director = row['director']

            movie = Movie(title, genre, rating, description, director)
            movies.append(movie)

        return movies

#assert(movie_data) == "Soul Surfer, Drama, PG, 1.75 hours"
#assert(movie_data) == "Barbie, Fantasy, PG-13, 2 hours"
#assert(movie_data) == "Old Dads, Comedy, R, 1.75 hours"

def choose_movie(movies):
    ''' Ask the user what movie they want to search for and finds it within
    the list of movies created
    
    Returns: a movie object that matches what the user searched for 
    '''
    while True:
        user_input = input("What movie do you want information about?").strip().upper()

        found_movie = None
        for movie in movies:
            if movie.title.upper() == user_input:
                found_movie = {
                    'title': movie.title,
                    'genre': movie.genre,
                    'rating': movie.rating,
                    'description': movie.description,
                    'director': movie.director
                }
                break
        
        if found_movie:
            return found_movie
        else:
            print("Movie not in database")


    
def display_info():
    ''' Displays information about movie in a readable way.
    
    '''

assert("comedy", "R", 1.75) == "Hot Tub Time Machine"
assert("fantasy", "PG", 1.5) == "Shrek"
assert("family", "G", 2) == "Cars"
assert("horror", "PG-13", 1.5) == "The Boogeyman"

def user_pref():
    ''' Ask the user a number of questions to find out what preferences they
    have for the movie they want to watch.
    
    Returns: a tuple of all of the preferences the user has
    '''

#get_matches function
def get_matches():
    '''Finds a list of matches to user preference from the movie list

    Returns: list of movies that match what the user prefers'''
    pass

#assert(user_inputs) == ["Murder Mystery, Grown Ups, The Do-Over, Blended, Just Go With It"]
#assert(user_inputs) == ["Shrek, Cars, Mall Cop, The Lorax, Planes, Wall-e"]

#filter_movies
def display_results():
    ''' Displays the matches to user criteria in a readable way
    
    args: result of get_matches
    returns: text of the movies that match criteria'''
    pass

assert(get_matches) == ["Grown-Ups, Blended"]
assert(get_matches) == ["Cars, Planes"]

def main():
    ''' main function 
    '''