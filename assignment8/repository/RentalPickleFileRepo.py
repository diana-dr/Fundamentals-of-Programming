from repository.RepositoryException import RepositoryError
from repository.Repository import Repository
import pickle
from domain.Rental import Rental
from datetime import date


class RentalPickleFileRepo(Repository):
    def __init__(self, fileName = "rentals.pickle"):
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
                r = Rental(int(res.id), int(res.movie), int(res.client), res.rentedDate, res.dueDate, res.returnedDate)
                Repository.store(self, r)
                res = pickle.load(f)
        except EOFError:
            return []
        except IOError as e:
            raise RepositoryError(str(e))
