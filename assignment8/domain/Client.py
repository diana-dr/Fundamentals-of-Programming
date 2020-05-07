class Client:
    def __init__(self, clientID, name):
        self._clientID = int(clientID)
        self._name = name

    @property
    def id(self):
        return int(self._clientID)

    @id.setter
    def id(self, newID):
        self._clientID = int(newID)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        self._name = newName

    def __str__(self):
        return "CLIENT ID: " + str(self._clientID) + " NAME: " + str(self._name)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return self.id == other.id
