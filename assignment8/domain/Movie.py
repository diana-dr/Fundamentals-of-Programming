class Movie:
    def __init__(self, movieID, title, description, genre):
        self._movieID = movieID
        self._title = title
        self._description = description
        self._genre = genre

    @property
    def id(self):
        return int(self._movieID)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, newTitle):
        self._title = newTitle

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, newDesc):
        self._description = newDesc

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, newGenre):
        self._genre = newGenre

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        return self.id == other.id

    def __str__(self):
        return "MOVIE ID: " + str(self._movieID) + " TITLE: " + str(self._title) + " DESCRIPTION: " + str(self._description) + " GENRE: " + str(self._genre)

    def __repr__(self):
        return str(self)