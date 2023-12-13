import pandas as pd

class Movie():
    """Class that stores data for an instance of the movie
    
    Attributes:
        title(str): name of the movie
        genre(str): genre of the movie
        rating(str): what the movie is rated
        director(str): who directed the movie
        year(int): year the movie was released
        score(float): score given to the movie
    """
    def __init__(self, title, genre, rating, director, year, score):
        '''Initialize all of the attributes of the class'''
        self.title = title
        self.genre = genre
        self.rating = rating
        self.director = director
        self.year = year
        self.score = score



class Database():
    """Class that stores data from the data file of movies

    """
    def __init__(self):
        self.movies = []
        self.genres = set()
        self.ratings = set()
        self.directors = set()
        self.years = set()
        self.scores = set()

    def put_info(self):
        """Adds the genre, rating, director, year, and score to the appropriate list to store it
    
        """
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
        ''' Gets values from the movies.csv file and stores them into variables.
        Only gets the data that we want from the file (title, genre, rating, director,
        year, and score) and disregards the other pieces of information. 

        Args:
            path: path to the file of movies
        
        Returns: a list of movies with movie objects in it.
        '''
        data = pd.read_csv(path)
        for _, row in data.iterrows():
            if "name" not in row or "genre" not in row or "rating" not in row or "director" not in row or "year" not in row or "score" not in row:
                print("Missing item")
                continue

            title = row["name"]
            genre = row["genre"]
            rating = row["rating"]
            director = row["director"]
            year = row["year"]
            score = row["score"]


            movie = Movie(title, genre, rating, director, year, score)
            self.movies.append(movie)

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
        ''' Ask the user what movie they want to search for and finds it within
        the list of movies created
        
        Returns: a movie object that matches what the user searched for 
        '''
        while True:
            user_input = input("What movie do you want information about?").strip()

            found_movie = None
            for movie in self.movies:
                if user_input.upper() == movie.title.upper():
                    found_movie = movie
                    break
            
            if found_movie:
                return found_movie
            else:
                return None


    
    def display_info(self, movie):
        ''' Displays information about movie in a readable way.
         
        Args:
            movie: movie object from the database
        '''
        print(movie)
        if movie:
            print(f"{movie.title} is a {movie.genre} film directed by {movie.director} in {movie.year} with a rating of {movie.rating} and a score of {movie.score}.")
        else:
            print("Movie not found in database")


    def user_pref(self):
        ''' Ask the user a number of questions to find out what preferences they
        have for the movie they want to watch.
    
        Returns: a tuple of all of the preferences the user has

        '''
        #asks the user questions to get their preferences for genres, ratings, etc
        while True:
                genre_pref = input(f"Choose a genre from {self.genres}: ")
                if genre_pref in self.genres:
                    break
                else:
                    print("Invalid. Enter a valid genre.")
        
        while True:
            try:
                rating_pref = input(f"Choose a rating from {self.ratings}: ")
                if rating_pref not in self.ratings:
                    raise ValueError("Invalid rating. Please choose from the given options.")
                break
            except ValueError as e:
                print(e)
                pass
                
    
        while True:
            try:
                director_pref = input(f"Choose a director from {self.directors}: ")
                if director_pref not in self.directors:
                    raise ValueError("Invalid director. Please choose from the given options.")
                break
            except ValueError:
                #raise an error
                pass
    
    #Maybe ask the user if they are looking for a specific score (like maybe someone only wants to see movies with a rating about 8 on IMDb).
    #For star, it could be optional (Ask the user IF they want to search for a specific celebrity and if so they can type the exact name they want).
 
        preferences = (genre_pref, rating_pref, director_pref)
        return preferences
        

    def get_matches(self):
        '''Finds a list of matches to user preference from the movie list

        Returns: list of movies that match what the user prefers'''
    
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

      #possibly take out director or add in something that shows them a few at a time, make it optional
        '''while True:
            try:
                director_pref = input(f"Choose a director {self.directors} or type None: ").strip()
                #if director_pref == None:
                if director_pref not in self.directors:
                    raise ValueError("Invalid director")
                break
            except ValueError as e:
                print(e)'''

        preferences = (genre_pref, rating_pref) # director_pref)
        matches = [movie for movie in self.movies if
                   preferences[0] == movie.genre and
                   preferences[1] == movie.rating] 
                   #preferences[2] == movie.director]
        return matches


#assert(user_inputs) == ["Murder Mystery, Grown Ups, The Do-Over, Blended, Just Go With It"]
#assert(user_inputs) == ["Shrek, Cars, Mall Cop, The Lorax, Planes, Wall-e"]

    def display_results(self, matches):
        ''' Displays the matches to user criteria in a readable way
    
        Args: 
            matches: result of get_matches, the movies that matches the user
                    preferences
        
        Returns: text of the movies that match criteria
        '''
    
        print("Here are the movies that match your preferences:\n")
        if not matches:
            print("No matches for your inputs")
        else:
            for i in range(min(10, len(matches))):
                print(f"{matches[i].title}\n")


def main(path):
    ''' main function - calls function that initiates program
    print statement that tells user what program does 
    Asks the user questions if they want the search or recommender
    '''

    database = Database()
    df = database.get_data(path)

    counter=0
    while True:
        user_choice = input("Which application do you want to use: search movie (S) or movie recommender(R)?").upper()

        if user_choice != "S" and user_choice != "R":
            print("Please type either 'S' or 'R'.")
            user_choice = input("Which application do you want to use: search movie (S) or movie recommender(R)?").upper()
        if user_choice == "S":
            chosen_movie = database.choose_movie()
            database.display_info(chosen_movie)
            
        else:
            matches = database.get_matches()
            database.display_results(matches)


if __name__ == "__main__":
    path = "movies.csv"
    main(path)

    
