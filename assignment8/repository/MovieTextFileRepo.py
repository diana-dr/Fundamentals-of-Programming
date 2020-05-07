from domain.Movie import Movie
from repository.RepositoryException import RepositoryError
from repository.Repository import Repository


class MovieTextFileRepo(Repository):
    def __init__(self, fileName = "movies.txt"):
        Repository.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def add(self, obj):
        Repository.add(self, obj)
        self._saveFile()

    def _saveFile(self):
        f = open(self._fileName, "w")
        for m in self.getAll():
            f.write(str(m.id) + ";" + m.title + ";" + m.description + ";" + m.genre + "\n")
        f.close()

    def _loadFile(self):
        try:
            f = open(self._fileName, "r")
            line = f.readline().strip()
            while len(line) > 2:
                tok = line.split(";")
                movie = Movie(int(tok[0]), tok[1], tok[2], tok[3])
                Repository.store(self, movie)
                line = f.readline().strip()
        except IOError as e:
            raise RepositoryError(str(e))
        finally:
            f.close()


