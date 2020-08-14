from PySide2 import QtWidgets, QtCore
from movie import get_movies, Movie


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film.")
        self.lw_movies = QtWidgets.QListWidget()
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_removeMovies = QtWidgets.QPushButton("Supprimer le(s) film(s).")

        self.main_layout.addWidget(self.le_movieTitle)
        self.main_layout.addWidget(self.btn_addMovie)
        self.main_layout.addWidget(self.lw_movies)
        self.main_layout.addWidget(self.btn_removeMovies)

    def populate_movies(self):
        movies = get_movies()
        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.movie = movie
            self.lw_movies.addItem(lw_item)

    def setup_connections(self):
        self.le_movieTitle.returnPressed.connect(self.add_movie)
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.btn_removeMovies.clicked.connect(self.remove_movie)

    def add_movie(self):
        movie_title = self.le_movieTitle.text()
        if movie_title:
            movie = Movie(movie_title)
            resultat = movie.add_to_movies()
            if resultat:
                lw_item = QtWidgets.QListWidgetItem(movie.title)
                lw_item.movie = movie
                self.lw_movies.addItem(lw_item)
                self.le_movieTitle.setText("")
                return True

        return False

    def remove_movie(self):
        for selected_item in self.lw_movies.selectedItems():
            movie = selected_item.movie
            movie.remove_from_movies()
            self.lw_movies.takeItem(self.lw_movies.row(selected_item))


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = App()
    win.show()

    app.exec_()
