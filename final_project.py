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
        print(movies)
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

        print(found_movie)


    
def display_info(movie):
    ''' Displays information about movie in a readable way.
        print 

    '''

    chosen_movie = choose_movie(movie)
    title = chosen_movie.title
    genre: chosen_movie.genre
    rating: chosen_movie.rating
    description: chosen_movie.description
    director: chosen_movie.director
    print(f"{title} is a {genre} film directed by {director} with a rating of {rating}.\nDescription:\n{description}")
    
assert("comedy", "R", 1.75) == "Hot Tub Time Machine"
assert("fantasy", "PG", 1.5) == "Shrek"
assert("family", "G", 2) == "Cars"
assert("horror", "PG-13", 1.5) == "The Boogeyman"

def user_pref():
    ''' Ask the user a number of questions to find out what preferences they
    have for the movie they want to watch.
    
    Returns: a tuple of all of the preferences the user has

    '''
    #import list of genres, ratings and directors
    while True:
        try:
            genre_pref = input(f"Choose a genre from {genres}: ")
            if genre_pref not in genres:
                raise ValueError("Invalid genre. Please choose a from the given options.")
                break
        except ValueError:
            #raise an error
            break
        
    while True:
        try:
            rating_pref = input(f"Choose a rating from {ratings}: ")
            if rating_pref not in ratings:
                raise ValueError("Invalid rating. Please choose from the given options.")
            break
        except ValueError:
            #raise an error
            #print statement abt what issue is 
            pass
                
    while True:
        try:
            director_pref = input(f"Choose a director from {directors}: ")
            if director_pref not in directors:
                raise ValueError("Invalid director. Please choose from the given options.")
            break
        except ValueError:
            #raise an error
            pass
    
    #Maybe ask the user if they are looking for a specific score (like maybe someone only wants to see movies with a rating about 8 on IMDb).
    #For star, it could be optional (Ask the user IF they want to search for a specific celebrity and if so they can type the exact name they want).
 
    preferences = (genre_pref, rating_pref, director_pref)
    return preferences
        
    
#get_matches function
def get_matches():
    '''Finds a list of matches to user preference from the movie list

    Returns: list of movies that match what the user prefers'''
    
    preference = user_pref()
    i = Movie()
    matches = []
    for movie in i.movies:
        if preference[0] == movie[1] and preference[1] == movie[2] and preference[2] == movie[4]:
            matches.append(movie)
    
    return matches


#assert(user_inputs) == ["Murder Mystery, Grown Ups, The Do-Over, Blended, Just Go With It"]
#assert(user_inputs) == ["Shrek, Cars, Mall Cop, The Lorax, Planes, Wall-e"]

#filter_movies
def display_results(matches):
    ''' Displays the matches to user criteria in a readable way
    
    args: result of get_matches
    returns: text of the movies that match criteria'''
    
    matches = get_matches()
    
    print("Here are the movies that match your preferences:\n")
    for item in matches:
        print(f"Title: {item.title}\nGenre: {item.genre}\nRating: {item.rating}\
            \nDescription: {item.description}\\nDirector: {item.director}")


#assert(get_matches) == ["Grown-Ups, Blended"]
#assert(get_matches) == ["Cars, Planes"]

def main():
    ''' main function - calls function that initiates program
    print statement that tells user what program does 
    '''