from domain.Client import Client
from controller.UndoController import *


class ClientController:
    def __init__(self, ClientValidator, clientRepo, rentalController, undoController):
        self.__validator = ClientValidator
        self.__repository = clientRepo
        self.__rental = rentalController
        self.__undo = undoController

    def create(self, clientID, clientName):
        client = Client(clientID, clientName)
        self.__validator.validate(client)
        self.__repository.add(client)

        undo = FunctionCall(self.remove, clientID)
        redo = FunctionCall(self.create, clientID, clientName)
        oper = Operation(undo, redo)
        self.__undo.addOperation(oper)
        return client

    def remove(self, clientID):
        cl = 0
        for client in self.__repository.getAll():
            if client.id == int(clientID):
                cl = client.name
                self.__repository.remove(client)

        undo = FunctionCall(self.add, cl)
        redo = FunctionCall(self.remove, clientID)
        oper = Operation(undo, redo)
        self.__undo.addOperation(oper)
        return True

    def update(self, id, name):
        undo = FunctionCall(self.update, id, self.searchById(id)[0].name)
        client = Client(id, name)
        self.__validator.validate(client)
        self.__repository.update(client)

        redo = FunctionCall(self.update, id, name)
        oper = Operation(undo, redo)
        self.__undo.addOperation(oper)
        return True

    def add(self, name):
        client = Client(len(self.getAll()) * 29 + 55 * 22, name)
        self.__validator.validate(client)
        self.__repository.add(client)

        undo = FunctionCall(self.remove, self.searchByName(name)[0].id)
        redo = FunctionCall(self.create, self.searchByName(name)[0].id, name)
        oper = Operation(undo, redo)
        self.__undo.addOperation(oper)
        return True

    def getClientCount(self):
        return len(self.__repository)

    def findByID(self, clientID):
        return self.__repository.find(clientID)

    def searchById(self, id):
        outputList = []
        for client in self.__repository.getAll():
            if client.id == id:
                outputList.append(client)

        return outputList

    def searchByName(self, name):
        outputList = []
        for client in self.__repository.getAll():
            if client.name.lower() == name.lower() or name.lower() in client.name.lower():
                outputList.append(client)

        return outputList

    def getAll(self):
        return self.__repository.getAll()

