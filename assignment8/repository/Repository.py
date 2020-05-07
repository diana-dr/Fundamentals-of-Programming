from repository.RepositoryException import RepositoryError


class Repository:
    def __init__(self):
        self._objects = []

    def store(self, obj):
        if self.find(obj.id) is not None:
            raise RepositoryError("Object having the id: " + str(obj.id) + " already in repository!")
        self._objects.append(obj)

    def update(self, obj):
        if obj not in self._objects:
            raise RepositoryError("This object is not contained in the repository!")
        for i in range(len(self._objects)):
            if self._objects[i] == obj:
                self._objects[i] = obj
                return True
        return False

    def find(self, obj):
        for o in self._objects:
            if o.id == obj:
                return o
        return None

    def add(self, obj):
        if obj in self._objects:
            raise RepositoryError("This object is already in repository!")
        self._objects.append(obj)

    def remove(self, obj):
        if obj not in self._objects:
            raise RepositoryError("This object is not in repository!")
        self._objects.remove(obj)

    def search(self, obj):
        outputList = []
        for o in self.getAll():
            if o.name.lower() == obj.lower() or obj.lower() in o.name.lower():
                outputList.append(o.name)
        for i in outputList:
            return str(i)

    def searchM(self, obj):
        outputList = []
        for o in self.getAll():
            if o.title.lower() == obj.lower() or obj.lower() in o.title.lower():
                outputList.append(o.title)
        for i in outputList:
            return str(i)

    def getAll(self):
        return self._objects[:]

    def __len__(self):
        return len(self._objects)

    def __str__(self):
        r = ""
        for e in self._objects:
            r += str(e)
        return r