from domain.Movie import Movie
from controller.UndoController import *


class MovieController:
    def __init__(self, validator, movieRepo, rentalController, undoController):
        self.__validator = validator
        self.__repository = movieRepo
        self.__rental = rentalController
        self.__undo = undoController

    def create(self, movieID, title, description, genre):
        movie = Movie(movieID, title, description, genre)
        self.__validator.validate(movie)
        self.__repository.add(movie)

        undo = FunctionCall(self.remove, movieID)
        redo = FunctionCall(self.create, movieID, title, description, genre)
        oper = Operation(undo, redo)
        self.__undo.addOperation(oper)

        return movie

    def add(self, title, description, genre):
        movie = Movie(len(self.getAll()) * 33 + 19 * 44, title, description, genre)
        self.__validator.validate(movie)
        self.__repository.add(movie)

        undo = FunctionCall(self.remove, self.searchByTitle(title)[0].id)
        redo = FunctionCall(self.create, self.searchByTitle(title)[0].id, title)
        oper = Operation(undo, redo)
        self.__undo.addOperation(oper)

        return True

    def update(self, id, title, description, genre):
        undo = FunctionCall(self.update, id, self.searchById(id)[0].title, self.searchById(id)[0].description,
                            self.searchById(id)[0].genre)
        movie = Movie(id, title, description, genre)
        self.__validator.validate(movie)
        self.__repository.update(movie)

        redo = FunctionCall(self.update, id, title, description, genre)
        oper = Operation(undo, redo)
        self.__undo.addOperation(oper)

        return True

    def remove(self, id):
        m = 0
        for movie in self.__repository.getAll():
            if movie.id == int(id):
                m = movie.title
                self.__repository.remove(movie)

        undo = FunctionCall(self.create, id, m)
        redo = FunctionCall(self.remove, id)
        oper = Operation(undo, redo)
        self.__undo.addOperation(oper)

        return True

    def getMovieCount(self):
        return len(self.__repository)

    def findByID(self, movieID):
        return self.__repository.find(movieID)

    def searchById(self, id):
        outputList = []
        for movie in self.__repository.getAll():
            if movie.id == id:
                outputList.append(movie)

        return outputList

    def searchByTitle(self, title):
        outputList = []
        for movie in self.__repository.getAll():
            if movie.title.lower() == title.lower() or title.lower() in movie.title.lower():
                outputList.append(movie)

        return outputList

    def searchByDescription(self, desc):

        outputList = []
        for movie in self.__repository.getAll():
            if movie.description.lower() == desc.lower() or desc.lower() in movie.description.lower():
                outputList.append(movie)

        return outputList

    def getAll(self):
        return self.__repository.getAll()


