class Order:
    def __init__(self, id, distance):
        self._id = id
        self._distance = distance

    @property
    def id(self):
        return int(self._id)

    @property
    def distance(self):
        return int(self._distance)

    def __str__(self):
        return "ID: " + str(self._id) + " Distance: " + str(self.distance)