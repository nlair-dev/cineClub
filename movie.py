import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")


class Movie:
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title

    @staticmethod
    def _get_movies():
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def _write_movies(movies):
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        movies = self._get_movies()
        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f'Le film {self.title} est déjà dans la liste')
            return False

    def remove_from_movies(self):
        movies = self._get_movies()
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
        else:
            logging.warning("Le film n'est pas la liste.")


if __name__ == '__main__':
    m = Movie("Harry Potter")
    m.remove_from_movies()
