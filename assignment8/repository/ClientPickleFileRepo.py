from repository.RepositoryException import RepositoryError
from repository.Repository import Repository
import pickle
from domain.Client import Client


class ClientPickleFileRepo(Repository):
    def __init__(self, fileName = "clients.pickle"):
        Repository.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def add(self, obj):
        Repository.add(self, obj)
        self._saveFile()

    def remove(self, obj):
        Repository.remove(self, obj)
        self._saveFile()

    def _saveFile(self):
        f = open(self._fileName, "wb")
        pickle.dump(self.getAll(), f)
        f.close()

    def _loadFile(self):
        try:
            f = open(self._fileName, "rb")
            res = pickle.load(f)
            for c in res:
                Repository.add(self, c)
        except EOFError:
            return []
        except IOError as e:
            raise RepositoryError(str(e))
