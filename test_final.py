#Use Exercise 4 and module 4 as a model, rps and test_rps files

import pytest

from final_project import Movie
from final_project import Database

def test_movie_class():
    movie = Movie("Popeye", "Adventure", "PG", "Robert Altman", 1980, 5.3)
    assert movie.title == "Popeye"
    assert movie.genre == "Adventure"
    assert movie.rating == "PG"
    assert movie.director == "Robert Altman"
    assert movie.year == 1980
    assert movie.score == 5.3

def database_put_info_test():
    database = Database()
    movie = Movie("Popeye", "Adventure", "PG", "Robert Altman", 1980, 5.3)
    database.movies.append(movie)
    database.put_info()
    assert "Adventure" in database.genres
    assert "PG" in database.ratings
    assert "Robert Altman" in database.directors
    assert 1980 in database.years
    assert 5.3 in database.scores




test_movie_class()
database_put_info_test()


print("No errors. Functions get what they should.")