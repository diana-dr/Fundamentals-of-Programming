class Driver:
    def __init__(self, id, name):
        self._name = name
        self._id = id

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    def __str__(self):
        return "ID: " + str(self._id) + " Name: " + self._name