import datetime
from domain.ValidatorException import ValidatorException
from repository.RepositoryException import RepositoryError
import random
import pickle
from domain.Client import Client
from domain.Movie import Movie
from domain.Rental import Rental


class UI:
    def __init__(self, client, movie, rental, undo):
        self._client = client
        self._movie = movie
        self._rental = rental
        self._undo = undo

        self.menuOptions = {
            0: "0. Exit",
            1: "1. Add client",
            2: "2. Add movie",
            3: "3. Remove client",
            4: "4. Remove movie",
            5: "5. Update client",
            6: "6. Update movie",
            7: "7. List clients",
            8: "8. List movies",
            9: "9. Rent a movie",
            10: "10. Return movie",
            11: "11. Search movie",
            12: "12. Search client",
            13: "13. Statistics ",
            14: "14. Undo",
            15: "15. Redo"
        }

    def addClients(self):
        firsNames = ["Mike", "Jake", "Michael", "Andrei", "Dan", "Dragos", "Razvan", "Bogdan", "Luke", "Catalin",
                           "Calum", "Alex", "Cristian", "Cristiana", "Michelle", "Renata", "Flavia", "Virginia",
                           "Andreea", "Cornelia", "Carmen", "Maria", "Tanya", "Joanna", "Beatrice"]

        lastNames = ["Popescu", "Tell", "Lennon", "Jackson", "Einstein", "Tesla", "Edison", "Musk", "Jobs",
                     "Marian", "Ionescu", "Dragos", "Iliescu", "Dumbravean", "Corlaci"]

        for i in range(10):
            firstName = random.choice(firsNames)
            lastName = random.choice(lastNames)
            clientName = firstName + " " + lastName
            self._client.add(clientName)

    def addMovies(self):
        titles0 = [
            "Avengers:", "Black", "Jurassic World:", "Incredibles", "Venom", "Mission:", "Deadpool", "Ant-Man and",
            "Operation", "Star Wars:", "Beauty and", "The Fate of", "Despicable Me", "Welcome to", "Spider-Man:",
            "Wolf Warrior", "Guardians of", "Thor:", "Wonder", "Captain America:", "Rogue One:", "Zootopia"]
        titles1 = [
            "Civil War", "A Star Wars Story", "2", "3", "The Last Jedi", "he Beast", "the Furious", "the Jungle",
            "Homecoming", "the Galaxy Vol. 2", "Ragnarok", "Woman", "Infinity War", "Panther", "Fallen Kingdom",
            "Impossible – Fallout", "the Wasp", "Red Sea"]
        descriptions = [
            "A man suffering from Alzheimer's embarks on a final road trip with his granddaughter.",
            "A grumpy Grinch plots to ruin Christmas for the village of Whoville.",
            "A chronicle of the years leading up to Queen's legendary appearance at the Live Aid (1985) concert.",
            "A couple find themselves in over their heads when they foster three children.",
            "A musician helps a young singer find fame, even as age and alcoholism send his own career into "
            "a downward spiral."
            "An unusual set of circumstances brings unexpected success to a pop star.",
            "A young couple's decision to get engaged threatens to break them apart.",
            "A woman in Harlem desperately scrambles to prove her fiancé innocent of a "
            "crime while carrying their first child."]
        genres = [
            "drama", "comedy", "musical", "thriller", "action", "Sci-Fi", "horror", "mystery", "crime", "animation"]

        for i in range(10):
            title0 = random.choice(titles0)
            title1 = random.choice(titles1)
            desc = random.choice(descriptions)
            genre = random.choice(genres)
            title = title0 + " " +title1
            self._movie.add(title, desc, genre)

    def writeToBinaryFile(self):
        rentals = []
        rental = Rental(1414, 1035, 1078, datetime.date(2019, 10, 23), datetime.date(2019, 10, 30),
                        datetime.date(2019, 10, 27))
        rentals.append(rental)

        clients = []
        names = ["Mike", "Jake", "Maria", "Andrei", "Dan", "Ana", "Diana"]
        for i in range(20):
            clients.append(Client(i*134+51, random.choice(names)))

        movies = []
        titles0 = ["Avengers", "A Star Wars Story", "Jurassic World", "Incredibles", "Venom", "The Last Jedi",
                   "Deadpool"]
        descriptions = ["A man suffering from Alzheimer's embarks on a final road trip with his granddaughter.",
                        "A couple find themselves in over their heads when they foster three children.",
                        "A young couple's decision to get engaged threatens to break them apart."]
        genres = ["drama", "comedy", "musical", "thriller", "action", "Sci-Fi"]

        for i in range(10):
            title = random.choice(titles0)
            desc = random.choice(descriptions)
            genre = random.choice(genres)
            movies.append(Movie(i*156+46, title, desc, genre))

        f = open("movies.pickle", "wb")
        for m in movies:
            pickle.dump(m, f)
        f.close()

        f = open("clients.pickle", "wb")
        for c in clients:
            pickle.dump(c, f)
        f. close()

        f = open("rentals.pickle", "wb")
        for r in rentals:
            pickle.dump(r, f)
        f.close()

    def showMenu(self):
        for val in self.menuOptions.values():
            print(val)

    def readString(self, text):
        inputData = input(text)
        return inputData.lstrip()

    def addClient(self):
        name = self.readString("Input name: ")
        self._client.add(name)
        if not self._movie.add(name):
            raise ValueError("The client could not be added!")

    def addMovie(self):
        title = self.readString("Input title: ")
        description = self.readString("Input description: ")
        genre = self.readString("Input genre: ")
        if not self._movie.add(title, description, genre):
            raise ValueError("The movie could not be added!")

    def removeClient(self):
        id = self.readString("Input ID: ")
        if not id.isnumeric():
            raise TypeError("Not an integer!")
        else:
            id = int(id)
        if self._client.searchById(id) is None:
            raise ValueError("ID not found!")
        else:
            self._client.remove(id)

    def removeMovie(self):
        id = self.readString("Input ID: ")
        if id.isnumeric():
            id = int(id)
        else:
            raise TypeError("Not an integer!")
        if self._movie.searchById(id) is None:
            raise ValueError("ID not found!")
        else:
            self._movie.remove(id)

    def updateClient(self):
        id = self.readString("Input the ID of the client you want to replace: ")
        if id.isnumeric():
            id = int(id)
        else:
            raise TypeError("Not an integer!")
        newName = self.readString("Input new name: ")

        if self._client.searchById(id) is None:
            raise ValueError("The client could not be found!")
        else:
            if not self._client.update(id, newName):
                raise ValueError("Cannot do the update!")

    def updateMovie(self):
        id = self.readString("Input the ID of the movie you want to replace: ")
        if id.isnumeric():
            id = int(id)
        else:
            raise TypeError("Not an integer!")
        newTitle = self.readString("Input new title: ")
        newDescription = self.readString("Input new description: ")
        newGenre = self.readString("Input new genre: ")

        if self._movie.searchById(id) is None:
            raise ValueError("The movie could not be found!")
        else:
            if not self._movie.update(id, newTitle, newDescription, newGenre):
                raise ValueError("Cannot do the update!")

    def listClients(self):
        clients = self._client.getAll()
        for client in clients:
            print(str(client))

    def listMovies(self):
        movies = self._movie.getAll()
        for movie in movies:
            print(str(movie))

    def searchMovie(self):
        movie = self.readString("Search: ")
        result = self._movie.searchByTitle(movie)
        result1 = self._movie.searchByDescription(movie)
        for res in result:
            print("Results by title: " + str(res))
        for re in result1:
            print("Result by description: " + str(re))

    def searchClient(self):
        client = self.readString("Search: ")
        result = self._client.searchByName(client)
        for res in result:
            print(res)

    def rentMovie(self):
        name = self.readString("Client name: ")

        result = self._client.searchByName(name)
        if len(result) == 0:
            print("No match for the client name.")
            return

        rentals = self._rental.getAll()
        for r in rentals:
            if r.client == self._client.searchByName(name)[0].id and r.dueDate < r.returnedDate:
                print("Can not rent you a movie!")
                return

        movie = self.readString("Movie title: ")
        res = self._movie.searchByTitle(movie)
        if len(res) == 0:
            print("No match for the movie title.")
            return

        rentedDate = datetime.date.today()
        dueDate = datetime.date.today() + datetime.timedelta(7)
        returnedDate = datetime.date(2018, 12, 31)

        self._rental.createRental(self._client.searchByName(name)[0].id, self._movie.searchByTitle(movie)[0].id,
                                  rentedDate, dueDate, returnedDate)

    def returnMovie(self):
        name = self.readString("Client name: ")
        result = self._client.searchByName(name)
        if len(result) == 0:
            print("No match for the client name.")
            return

        movie = self.readString("Movie title: ")
        res = self._movie.searchByTitle(movie)
        if len(res) == 0:
            print("No match for the movie title.")
            return

        rentals = self._rental.getAll()
        for r in rentals:
            if r.client == self._client.searchByName(name)[0].id:
                if r.movie == self._movie.searchByTitle(movie)[0].id:
                    r.returnedDate = datetime.date.today()
            else:
                print("The movie could not be returned.")

    def printMostRentedMovies(self):
        if len(self._rental.getAll()) == 0:
            print("There are no rented movies!")
        else:
            print("Statistics 1.")
            print("Most rented movies. The list of movies, sorted by the number of times they were rented.")
            print("Times".ljust(10) + " Movie".ljust(40))
            new = self._rental.mostRentedMovies()
            for m in new:
                print(str(m))
            print("-" * 70)

    def printMostActiveClients(self):
        if len(self._rental.getAll()) == 0:
            pass
        else:
            print("Statistics 2.")
            print("Most active clients. The list of clients, sorted by the number of movie rental days they have.")
            print("Days".ljust(10) + " Client".ljust(40))
            new = self._rental.mostActiveClients()
            for c in new:
                print(str(c))
            print("-" * 70)

    def printAllRentals(self):
        if len(self._rental.getAll()) == 0:
            pass
        else:
            print("Statistics 3.")
            print("All rentals.")
            new = self._rental.allRentals()
            for r in new:
                print(str(r))
            print("-" * 70)

    def printDelayRentals(self):
        if len(self._rental.getAll()) == 0:
            pass
        else:
            print("Statistics 4.")
            print("Late rentals. All the movies that are currently rented, for which the due date for "
                  "return has passed, sorted by the number of days of delay.")
            print("Delay".ljust(10) + " Movie".ljust(40))
            new = self._rental.delayRentals()
            for r in new:
                print(str(r))
            print("-" * 70)

    def showStatistics(self):
        self.printMostRentedMovies()
        self.printMostActiveClients()
        self.printAllRentals()
        self.printDelayRentals()

    def undo(self):
        if not self._undo.operations:
            print("There is no command to undo!")

        self._undo.undo()

    def redo(self):
        if not self._undo.operations:
            print("There is no command to redo!")

        self._undo.redo()

    def run(self):
        while True:
            print("MENU: ")
            self.showMenu()
            option = self.readString("CHOOSE: ")
            if option.isnumeric():
                option = int(option)
            try:
                if option == 0:
                    exit()
                elif option == 1:
                    self.addClient()
                elif option == 2:
                    self.addMovie()
                elif option == 3:
                    self.removeClient()
                elif option == 4:
                    self.removeMovie()
                elif option == 5:
                    self.updateClient()
                elif option == 6:
                    self.updateMovie()
                elif option == 7:
                    self.listClients()
                elif option == 8:
                    self.listMovies()
                elif option == 9:
                    self.rentMovie()
                elif option == 10:
                    self.returnMovie()
                elif option == 11:
                    self.searchMovie()
                elif option == 12:
                    self.searchClient()
                elif option == 13:
                    self.showStatistics()
                elif option == 14:
                    self.undo()
                elif option == 15:
                    self.redo()
                else:
                    print("Invalid command!")
            except ValueError as e:
                print(e)
            except RepositoryError as e:
                print(e)
            except ValidatorException as e:
                print(e)
