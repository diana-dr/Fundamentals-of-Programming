from domain.Client import Client
from repository.RepositoryException import RepositoryError
from repository.Repository import Repository


class ClientTextFileRepo(Repository):
    def __init__(self, fileName = "clients.txt"):
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
                f.write(str(m.id) + ";" + m.name + "\n")
        except IOError as e:
            raise RepositoryError(str(e))
        finally:
            f.close()

    def _loadFile(self):
        f = open(self._fileName, "r")
        line = f.readline().strip()
        while len(line) > 2:
            tok = line.split(";")
            client = Client(int(tok[0]), tok[1])
            Repository.store(self, client)
            line = f.readline().strip()
