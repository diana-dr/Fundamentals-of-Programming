from UI import *
from controller.MovieController import MovieController
from controller.ClientController import ClientController
from controller.RentalController import RentalController
from repository.Repository import *
from domain.ClientValidator import ClientValidator
from domain.MovieValidator import MovieValidator
from domain.RentalValidator import RentalValidator
from controller.UndoController import UndoController
from repository.MovieTextFileRepo import MovieTextFileRepo
from repository.ClientTextFileRepo import ClientTextFileRepo
from repository.RentalTextFileRepo import RentalTextFileRepo
from repository.RentalPickleFileRepo import RentalPickleFileRepo
from repository.MoviePickleFileRepo import MoviePickleFileRepo
from repository.ClientPickleFileRepo import ClientPickleFileRepo


def readSettings():
    settings ={}
    f = open("settings.properties", "r")
    s = f.read()

    lines = s.split("\n")

    for line in lines:
        tokens = line.split("=")
        settings[tokens[0].strip()] = tokens[1].strip()

    f.close()

    return settings


def main():
    settings = readSettings()

    if settings["repository"] == "inmemory":
        undo = UndoController()
        rental = RentalController(RentalValidator(), Repository(), Repository(), Repository())
        client = ClientController(ClientValidator(), Repository(), rental, undo)
        movie = MovieController(MovieValidator(), Repository(), rental, undo)
        ui = UI(client, movie, rental, undo)
        ui.addClients()
        ui.addMovies()
        ui.run()
    elif settings["repository"] == "textfiles":
        undo = UndoController()
        rental = RentalController(RentalValidator(), RentalTextFileRepo(), MovieTextFileRepo(), ClientTextFileRepo())
        client = ClientController(ClientValidator(), ClientTextFileRepo(), rental, undo)
        movie = MovieController(MovieValidator(), MovieTextFileRepo(), rental, undo)
        ui = UI(client, movie, rental, undo)
        ui.run()
    elif settings["repository"] == "binaryfiles":
        undo = UndoController()
        rental = RentalController(RentalValidator(), RentalPickleFileRepo(), MoviePickleFileRepo(), ClientPickleFileRepo())
        client = ClientController(ClientValidator(), ClientPickleFileRepo(), rental, undo)
        movie = MovieController(MovieValidator(), MoviePickleFileRepo(), rental, undo)
        ui = UI(client, movie, rental, undo)
        ui.writeToBinaryFile()
        ui.run()
    else:
        return


main()

