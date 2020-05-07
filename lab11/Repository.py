from Order import Order
from Driver import Driver


class Repository:
    def __init__(self):
        self._objects = []

    def add(self, obj):
        """
        :param obj: the object we want to add in repo
        :return: adds the obj in repo
        """
        self._objects.append(obj)

    def getAll(self):
        """
        :return: all objects in repo
        """
        return self._objects[:]


class OrderTextFileRepo(Repository):
    def __init__(self, fileName = "orders.txt"):
        Repository.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def _loadFile(self):
        """
        :return: reads the data from the given text file and adds them in the repo
        """
        f = open(self._fileName, "r")
        line = f.readline().strip()
        while len(line) >= 2:
            tok = line.split(",")
            order = Order(int(tok[0]), int(tok[1]))
            Repository.add(self, order)
            line = f.readline().strip()


class DriverTextFileRepo(Repository):
    def __init__(self, fileName = "drivers.txt"):
        Repository.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def _loadFile(self):
        """
        :return: reads the drivers from the given text file and adds them in the repo
        """
        f = open(self._fileName, "r")
        line = f.readline().strip()
        while len(line) >= 2:
            tok = line.split(",")
            driver = Driver(int(tok[0]), tok[1])
            Repository.add(self, driver)
            line = f.readline().strip()

