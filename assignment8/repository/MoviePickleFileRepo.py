from repository.RepositoryException import RepositoryError
from repository.Repository import Repository
import pickle
from domain.Movie import Movie


class MoviePickleFileRepo(Repository):
    def __init__(self, fileName = "movies.pickle"):
        Repository.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def add(self, obj):
        Repository.add(self, obj)
        self._saveFile()

    def _saveFile(self):
        f = open(self._fileName, "wb")
        pickle.dump(self.getAll(), f)
        f.close()

    def _loadFile(self):
        try:
            f = open(self._fileName, "rb")
            res = pickle.load(f)
            while res != "":
                m = Movie(int(res.id), res.title, res.description, res.genre)
                Repository.store(self, m)
                res = pickle.load(f)
        except EOFError:
            return []
        except IOError as e:
            raise RepositoryError(str(e))
