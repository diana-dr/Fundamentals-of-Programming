import datetime

class Rental:
    def __init__(self, rentalID, movie, client, rentedDate, dueDate, returnedDate):
        self._rentalID = rentalID
        self._movie = movie
        self._client = client
        self._rentedDate = rentedDate
        self._dueDate = dueDate
        self._returnedDate = returnedDate

    @property
    def id(self):
        return int(self._rentalID)

    @property
    def client(self):
        return int(self._client)

    @client.setter
    def client(self, newClient):
        self._client = int(newClient)

    @property
    def movie(self):
        return int(self._movie)

    @movie.setter
    def movie(self, newMovie):
        self._movie = int(newMovie)

    @property
    def rentedDate(self):
        return self._rentedDate

    @rentedDate.setter
    def rentedDate(self, newDate):
        self._rentedDate = newDate

    @property
    def dueDate(self):
        return self._dueDate

    @dueDate.setter
    def dueDate(self, newDate):
        self._dueDate = newDate

    @property
    def returnedDate(self):
        return self._returnedDate

    @returnedDate.setter
    def returnedDate(self, newDate):
        self._returnedDate = newDate

    def __len__(self):
        delta = self._returnedDate - self._rentedDate
        return delta.days + 1

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "rental ID: " + str(self._rentalID) + " \nmovie: " + str(self._movie) + " \nclient: " + str(self._client) + "\nperiod: " + self._rentedDate.strftime("%Y-%m-%d") + " to " + self._dueDate.strftime("%Y-%m-%d") + " returned: " + self._returnedDate.strftime("%Y-%m-%d")
