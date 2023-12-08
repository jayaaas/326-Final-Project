#Movie class
#contains file that has all movies in database (need to find movie database)
import pandas as pd

class Movie():
    def __init__(self, title, genre, rating, director):
        '''Initialize all of the attributes of the class'''
        self.title = title
        self.genre = genre
        self.rating = rating
        self.director = director

#clean_up function
class Database():
    def __init__(self):
        self.movies = []
        self.genres = set()  #use set, make list of genres to keep track what goes with each movie, method to convert list to set
        self.ratings = []
        self.directors = []

    def put_info(self):
        for movie in self.movies:
            if movie.genre not in self.genres:
                self.genres.add(movie.genres)  #don't use append for sets, use add()
            if movie.rating not in self.ratings:
                self.ratings.append(movie.ratings)
            if movie.director not in self.directors:
                self.directors.append(movie.director)
        
    def get_data(self, path):
        ''' Gets values from the movies.csv file and stores them into variables.
        Only gets the data that we want from the file (title, genre, rating,
        description, and director) and disregards the other pieces of information. 
        
        Returns: a list of movies with movie objects in it.
        '''
        data = pd.read_csv(path)
        for _, row in data.iterrows():
            if "name" not in row or "genre" not in row or "rating" not in row or "director" not in row:
                print("Missing item")
                continue

            title = row["name"]
            genre = row["genre"]
            rating = row["rating"]
            director = row["director"]


            movie = Movie(title, genre, rating, director)
            self.movies.append(movie)

            if genre:
                self.genres.add(genre)
            if rating:
                self.ratings.append(rating)
            if director:
                self.ratings.append(director)

        self.put_info()
                #self.genres.add(genre)
                #self.ratings.add(rating)
                #self.directors.add(director)
        return self.movies


#assert(movie_data) == "Soul Surfer, Drama, PG, 1.75 hours"
#assert(movie_data) == "Barbie, Fantasy, PG-13, 2 hours"
#assert(movie_data) == "Old Dads, Comedy, R, 1.75 hours"

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
                    #print("found_movie", movie.title.upper())
                    found_movie = movie
                    break


                    #found_movie = {
                        #'title': movie.title,
                        #'genre': movie.genre,
                        #'rating': movie.rating,
                       # 'director': movie.director
                   # }
                  #  break
            
            if found_movie:
                return found_movie
            else:
                print("Movie not in database")
                return None


    
    def display_info(self, movie):
        ''' Displays information about movie in a readable way.
         print 

        '''
        print(movie)
        if movie:
            print(f"{movie.title} is a {movie.genre} film directed by {movie.director} with a rating of {movie.rating}.")
        else:
            print("Movie not found in database")


    #chosen_movie = choose_movie(movie)
    #title = chosen_movie.title
   # genre: chosen_movie.genre
    #rating: chosen_movie.rating
    #director: chosen_movie.director
    #print(f"{title} is a {genre} film directed by {director} with a rating of {rating}.")
    
# assert("comedy", "R", 1.75) == "Hot Tub Time Machine"
#assert("fantasy", "PG", 1.5) == "Shrek"
#assert("family", "G", 2) == "Cars"
#assert("horror", "PG-13", 1.5) == "The Boogeyman"

    def user_pref(self):
        ''' Ask the user a number of questions to find out what preferences they
        have for the movie they want to watch.
    
        Returns: a tuple of all of the preferences the user has

        '''
    #import list of genres, ratings and directors

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
            except ValueError:
                #raise an error
                #print statement abt what issue is 
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
        
    
#get_matches function
    def get_matches(self):
        '''Finds a list of matches to user preference from the movie list

        Returns: list of movies that match what the user prefers'''
    
        preference = self.user_pref()
        #i = Movie()
        matches = [movie for movie in self.movies if
                preference[0] == movie.genre and preference[1] == movie.rating and preference[2] == movie.director]
        return matches


#assert(user_inputs) == ["Murder Mystery, Grown Ups, The Do-Over, Blended, Just Go With It"]
#assert(user_inputs) == ["Shrek, Cars, Mall Cop, The Lorax, Planes, Wall-e"]

#filter_movies
    def display_results(self, matches):
        ''' Displays the matches to user criteria in a readable way
    
        args: result of get_matches
        returns: text of the movies that match criteria'''
    
        #matches = get_matches()
    
        print("Here are the movies that match your preferences:\n")
        for item in matches:
            # print(f"Title: {item.title}\nGenre: {item.genre}\nRating: {item.rating}\
                #\nDirector: {item.director}")
            print(f"{item.title}\n")


#assert(get_matches) == ["Grown-Ups, Blended"]
#assert(get_matches) == ["Cars, Planes"]

def main(path):
    ''' main function - calls function that initiates program
    print statement that tells user what program does 
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
            
    
                            
    #database.choose_movie()
    #user_pref(database)
    #user_pref(genre[genre])
    
if __name__ == "__main__":
    path = "movies.csv"
    main(path)
    
