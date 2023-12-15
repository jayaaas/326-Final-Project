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
    assert("The Shining") == "The Shining is a Drama film directed by Stanley Kubrick in 1980 with a rating of R and a score of 8.4."
    assert("Indiana Jones and the Raiders of the Lost Ark") == "Indiana Jones and the Raiders of the Lost Ark is a Action film directed by Steven Spielberg in 1981 with a rating of PG and a score of 8.4"
    assert("Lucas") == "Lucas is a Comedy film directed by David Seltzer in 1986 with a rating of PG-13 and a score of 6.9."
    assert("One Crazy Summer") == "One Crazy Summer is a Comedy film directed by Savage Steve Holland in 1986 with a rating of PG and a score of 6.4"
    
#unit test display_info
def database_test_display_info():
    database.display_info()
    assert("comedy", "R", 1.75) == "Hot Tub Time Machine"
    assert("fantasy", "PG", 1.5) == "Shrek"
    assert("family", "G", 2) == "Cars"
    assert("horror", "PG-13", 1.5) == "The Boogeyman"



test_movie_class()
database_test_put_info()
database_test_choose_movie()
database_test_display_info()


print("No errors. Functions get what they should.")