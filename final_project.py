import pandas as pd

class Movie():
    ''' A class that stores data for an instance of the movie.
    
    Attributes:
        title(str): Name of the movie
        genre(str): Genre of the movie
        rating(str): Rating of the movie.
        director(str): Director of the movie.
        year(int): Year the movie was released.
        score(float): Score given to the movie.
    '''
    def __init__(self, title, genre, rating, director, year, score):
        '''Initialize all of the attributes of the Movie class'''
        self.title = title
        self.genre = genre
        self.rating = rating
        self.director = director
        self.year = year
        self.score = score

class Database():
    '''Class that stores data from the data file of movies.
    
    Attributes: 

    '''
    #come back to this docstring
    def __init__(self):
        '''Initialize all of the attributes of the  Database class.
        '''
        #coem back to docstring
        self.movies = []
        self.genres = set()
        self.ratings = set()
        self.directors = set()
        self.years = set()
        self.scores = set()

    def put_info(self):
        '''Adds the genre, rating, director, year, and score to the appropriate list to store it.
        '''
        #Checks if each attribute about movie is in that specific set
        for movie in self.movies:
            if movie.genre not in self.genres:
                self.genres.add(movie.genre) 
            if movie.rating not in self.ratings:
                self.ratings.add(movie.rating)
            if movie.director not in self.directors:
                self.directors.add(movie.director)
            if movie.year not in self.years:
                self.years.add(movie.year)
            if movie.score not in self.scores:
                self.scores.add(movie.score)

        
    def get_data(self, path):
        ''' Gets values from the movies.csv file and stores them into variables. Only gets the data that we want from the file (title, genre, rating, director, year, and score) and disregards the other pieces of information. 
        Args:
            path (str): The path to the file of movies.
        
        Returns: A list of movies with movie objects in it.
        '''
        #opens and reads the file
        data = pd.read_csv(path)
        for _, row in data.iterrows():
            #checks to make sure every piece of data we want is in the file
            if "name" not in row or "genre" not in row or "rating" not in row or "director" not in row or "year" not in row or "score" not in row:
                print("Missing item")
                continue

            title = row["name"]
            genre = row["genre"]
            rating = row["rating"]
            director = row["director"]
            year = row["year"]
            score = row["score"]

            #instantiates the Movie class to get all the info about one movie and add it to a list 
            movie = Movie(title, genre, rating, director, year, score)
            self.movies.append(movie)

            #adds each specific thing to the set if it's not already there
            if genre:
                self.genres.add(genre)
            if rating:
                self.ratings.add(rating)
            if director:
                self.directors.add(director)
            if year:
                self.years.add(year)
            if score:
                self.scores.add(score)

        self.put_info()

        return self.movies

    def choose_movie(self):
        ''' Ask the user what movie they want to search for and finds it within the list of movies created.
        
        Returns: A movie object that matches what the user searched for.
        '''
        while True:
            user_input = input("What movie do you want information about?").strip()

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
            else:
                print("Invalid. Enter a valid genre.")
        
        while True:
            rating_pref = input(f"Choose a genre from {self.ratings}: ")
            if rating_pref in self.ratings:
                break
            else:
                print("Invalid. Enter a valid rating.")
                
        while True:
            director_pref = input(f"Choose a genre from {self.directors}: ")
            if director_pref in self.directors:
                break
            else:
                print("Invalid. Enter a valid director.")
 
        preferences = (genre_pref, rating_pref, director_pref)
        return preferences
        
    def get_matches(self):
        ''' Finds a list of matches to the user's preferences from the movie list.

        Returns: A list of movies that match what the user prefers.
        '''
        while True:
            genre_pref = input(f"Choose a genre from {self.genres}: ").strip()
            if genre_pref in self.genres:
                break
            else:
                print("Invalid genre")
        
        while True:
            try:
                rating_pref = input(f"Choose a rating {self.ratings}: ").strip()
                if rating_pref not in self.ratings:
                    raise ValueError("Invalid rating")
                break
            except ValueError as e:
                print(e)

        #gets the users preferences and makes sure it matches up with a movie
        preferences = (genre_pref, rating_pref)
        matches = [movie for movie in self.movies if
                   preferences[0] == movie.genre and
                   preferences[1] == movie.rating] 
        return matches

#assert(user_inputs) == ["Murder Mystery, Grown Ups, The Do-Over, Blended, Just Go With It"]
#assert(user_inputs) == ["Shrek, Cars, Mall Cop, The Lorax, Planes, Wall-e"]

    def display_results(self, matches):
        ''' Displays the matches to user criteria in a readable way.
    
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