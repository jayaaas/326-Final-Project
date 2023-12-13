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


#finish these below, I think they're all set up the same?
def database_get_data_test():
    database = Database()
    movie = Movie("Popeye", "Adventure", "PG", "Robert Altman", 1980, 5.3)
    database.movies.append(movie)
    database.get_data()
    pass


def database_choose_movie_test():
    database = Database()
    movie = Movie("Popeye", "Adventure", "PG", "Robert Altman", 1980, 5.3)
    database.movies.append(movie)
    database.choose_movie()
    pass

def database_display_info_test():
    database = Database()
    movie = Movie("Popeye", "Adventure", "PG", "Robert Altman", 1980, 5.3)
    database.movies.append(movie)
    database.display_info()
    pass

def database_user_pref_test():
    database = Database()
    movie = Movie("Popeye", "Adventure", "PG", "Robert Altman", 1980, 5.3)
    database.movies.append(movie)
    database.user_pref()
    pass

def database_get_matches_test():
    database = Database()
    movie = Movie("Popeye", "Adventure", "PG", "Robert Altman", 1980, 5.3)
    database.movies.append(movie)
    database.get_matches()
    pass


def database_display_results_test():
    database = Database()
    movie = Movie("Popeye", "Adventure", "PG", "Robert Altman", 1980, 5.3)
    database.movies.append(movie)
    database.display_results()
    pass



test_movie_class()
database_put_info_test()
database_get_data_test()
database_choose_movie_test()
database_display_info_test()
database_user_pref_test()
database_get_matches_test()
database_display_results_test()

print("No errors. Functions get what they should.")