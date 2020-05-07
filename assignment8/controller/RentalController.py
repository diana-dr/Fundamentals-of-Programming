from domain.MovieRentalException import MovieRentalException
from domain.Rental import Rental
import datetime


class RentalController:
    def __init__(self, validator, rentalRepo, movieRepo, clientRepo):
        self.__validator = validator
        self.__repository = rentalRepo
        self.__movieRepo = movieRepo
        self.__clientRepo = clientRepo

    def createRental(self, movie, client, rentedDate, dueDate, returnedDate):
        rental = Rental(len(self.getAll()) * 45 + 66 * 84, movie, client, rentedDate, dueDate, returnedDate)
        self.__validator.validate(rental)
        self.__repository.add(rental)

        return rental

    def removeRental(self, rentalID, movieId, clientId, rentalDate, dueDate, returnedDate):
        rental = Rental(rentalID, movieId, clientId, rentalDate, dueDate, returnedDate)
        self.__validator.validate(rental)
        self.__repository.remove(rental)

    def getAll(self):
        return self.__repository.getAll()

    def filterRentals(self, client, movie):
        result = []
        for rental in self.__repository.getAll():
            if client is not None and rental.client != client:
                continue
            if movie is not None and rental.movie != movie:
                continue
            result.append(rental)
        return result

    def getRentalCount(self):
        return len(self.__repository)

    def mostRentedMovies(self):
        aux = {}
        for m in self.__repository.getAll():
            if m.movie.title not in aux.keys():
                aux[m.movie.title] = 0
            else:
                aux[m.movie.title] += 1
        result = []
        for val in aux:
            result.append(MovieRentalCount(self.__movieRepo.searchM(val), aux[val]))
        result.sort(reverse=True)
        return result

    def mostActiveClients(self):
        aux = {}
        for m in self.__repository.getAll():
            if m.client.name not in aux.keys():
                aux[m.client.name] = len(m)
            else:
                aux[m.client.name] += len(m)
        result = []
        for val in aux:
            result.append(ClientRentalCount(self.__clientRepo.search(val), aux[val]))
        result.sort(reverse=True)
        return result

    def allRentals(self):
        result = []
        for m in self.__repository.getAll():
            if m.movie.title in result:
                pass
            else:
                if m.rentedDate != 0 and m.returnedDate > datetime.date.today():
                    result.append(m.movie.title)
        result.sort(reverse=True)
        return result

    def lateRentals(self):
        aux = {}
        for r in self.__repository.getAll():
            if r.returnedDate > r.dueDate:
                delta = r.returnedDate - r.dueDate
                aux[r.movie.title] = delta.days
        result = []
        for val in aux:
            result.append(MovieRentalCount(self.__movieRepo.searchM(val), aux[val]))
        result.sort(reverse=True)
        return result


class ClientRentalCount():
    def __init__(self, client, count):
        self._client = client
        self._count = count

    @property
    def client(self):
        return self._client

    @property
    def count(self):
        return self._count

    def __str__(self):
        return str(self._count).ljust(10) + str(self._client)

    def __gt__(self, other):
        return self._count > other._count


class MovieRentalCount():
    def __init__(self, movie, count):
        self._movie = movie
        self._count = count

    @property
    def movie(self):
        return self._movie

    @property
    def count(self):
        return self._count

    def __str__(self):
        return str(self._count).ljust(10) + str(self._movie)

    def __gt__(self, other):
        return self._count > other._count