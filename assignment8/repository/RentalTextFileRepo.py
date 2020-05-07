from domain.Rental import Rental
from repository.RepositoryException import RepositoryError
from repository.Repository import Repository
from datetime import date


class RentalTextFileRepo(Repository):
    def __init__(self, fileName = "rentals.txt"):
        Repository.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def add(self, obj):
        Repository.add(self, obj)
        self._saveFile()

    def _saveFile(self):
        try:
            f = open(self._fileName, "w")
            for m in self.getAll():
                f.write(str(m.id) + ";" + str(m.movie) + ";" + str(m.client) + ";" + str(m.rentedDate)
                        + ";" + str(m.dueDate) + ";" + str(m.returnedDate) + "\n")
            f.close()
        except IOError as e:
            raise RepositoryError(str(e))

    def _loadFile(self):
        f = open(self._fileName, "r")
        line = f.readline().strip()
        while len(line) > 2:
            tok = line.split(";")
            d1 = tok[3].split("-")
            d2 = tok[4].split("-")
            d3 = tok[5].split("-")
            rental = Rental(int(tok[0]), int(tok[1]), int(tok[2]), date(int(d1[0]), int(d1[1]), int(d1[2])),
                            date(int(d2[0]), int(d2[1]), int(d2[2])), date(int(d3[0]), int(d3[1]), int(d3[2])))
            Repository.store(self, rental)
            line = f.readline().strip()

