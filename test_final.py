#Use Exercise 4 and module 4 as a model, rps and test_rps files

import pytest

from final_project import Movie
from final_project import Database

def test_movie_class():
    movie = Movie("Popeye", "Adventure", "PG", "Robert Altman", 1980, 5.3)
    assert movie.title == "Popeye", f"Correct is 'Popeye' but got {movie.title}"
    assert movie.genre == "Adventure", f"Correct is 'Adventure' but got {movie.genre}"
    assert movie.rating == "PG", f"Correct is 'PG' but got {movie.rating}"
    assert movie.director == "Robert Altman", f"Correct is 'Robert Altman' but got {movie.director}"
    assert movie.year == 1980, f"Correct is '1980' but got {movie.year}"
    assert movie.score == 5.3, f"Correct is '5.3' but got {movie.score}"

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