#Use Exercise 4 and module 4 as a model, rps and test_rps files

import pytest

from final_project import Movie
from final_project import Database

movie = Movie("Popeye", "Adventure", "PG", "Robert Altman", 1980, 5.3)
database = Database()
database.movies.append(movie)

#unit test movie class
def test_movie_class():
    assert movie.title == "Popeye"
    assert movie.genre == "Adventure"
    assert movie.rating == "PG"
    assert movie.director == "Robert Altman"
    assert movie.year == 1980
    assert movie.score == 5.3

#unit test put_info
def database_test_put_info():
    database.put_info()
    assert "Adventure" in database.genres
    assert "PG" in database.ratings
    assert "Robert Altman" in database.directors
    assert 1980 in database.years
    assert 5.3 in database.scores
    
#unit test choose_movie
def database_test_choose_movie():
    database.choose_movie()
    #someone else has to add to this because i can't run the final project code
    
#unit test display_info
def database_test_display_info():
    database.display_info()
    assert("comedy", "R", 1.75) == "Hot Tub Time Machine"
    assert("fantasy", "PG", 1.5) == "Shrek"
    assert("family", "G", 2) == "Cars"
    assert("horror", "PG-13", 1.5) == "The Boogeyman"



test_movie_class()
database_test_put_info()


print("No errors. Functions get what they should.")