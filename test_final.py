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
    
#unit test get_data
def database_test_get_data(path):
    database.get_data(path)
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
    assert("Lucas") == "Lucas is a Comedy film directed  by David Seltzer in 1986 with a rating of PG-13 and a score of 6.9."
    assert("One Crazy Summer") == "One Crazy Summer is a Comedy film directed by Savage Steve Holland in 1986 with a rating of PG and a score of 6.4"
    
#unit test display_info
def database_test_display_info(movie):
    database.display_info(movie)
    assert("Hot Tub Time Machine") == "Hot Tub Time Machine is a Comedy film directed by Steve Pink in 2010 with a rating of R and a score of 6.4."
    assert("Shrek") == "Shrek is a Animation film directed by Andrew Adamson in 2001 with a rating of PG and a score of 7.9."
    assert("Cars") == "Cars is a Animation film directed by John Lasseter in 2006 with a rating of G and a score of 7.1."

#unit test user_pref
def database_test_user_pref():
    database.choose_movie()
    assert("Adventure") == genre_pref 
    assert("PG") == rating_pref

#unit test get_matches
def database_test_get_matches():
    database.choose_movie()
    assert "preferences" == ("Adventure", "PG")
