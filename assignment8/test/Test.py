import unittest
from domain.Movie import Movie
from domain.MovieValidator import MovieValidator
from domain.Client import Client
from domain.ValidatorException import ValidatorException
from domain.ClientValidator import ClientValidator
from domain.RentalValidator import RentalValidator
from domain.Rental import Rental
import datetime
from repository.Repository import Repository


class MovieControllerTest(unittest.TestCase):
    def setUp(self):
        self.v = MovieValidator()
        self.movie = Repository()
        self.c = Movie("1", "aaa", "bbb", "ccc")

    def testMovie(self):
        self.movie.add([1, "aaa", "bbb", "ccc"])
        self.assertTrue(self.v.validate, self.movie)
        self.assertEqual(len(self.movie.getAll()), 1)
        self.movie.add([])
        self.assertTrue(self.v.validate, self.c)
        self.c.genre = "aaa"
        self.assertTrue(self.v.validate, self.c.genre == "aaa")
        self.c.genre = ""
        self.assertRaises(ValidatorException, self.v.validate, self.c)
        self.c.description = "bbb"
        self.assertTrue(self.v.validate, self.c.description == "bbb")
        self.c.description = ""
        self.assertRaises(ValidatorException, self.v.validate, self.c)
        self.assertEqual(len(self.movie), 2)


class ClientTestCase(unittest.TestCase):

    def setUp(self):
        self.v = ClientValidator()
        self.c = Client("1", "aaa")
        self.client = Repository()

    def testClient(self):
        self.assertTrue(self.v.validate, self.c)
        self.c.name = "bbb"
        self.assertTrue(self.v.validate, self.c.name == "bbb")
        self.c.name = ""
        self.assertRaises(ValidatorException, self.v.validate, self.c)
        z = Client("1", "Anna")
        self.client.add(z)
        self.client.remove(z)
        self.assertEqual(len(self.client.getAll()), 0)


class RentalTestCase(unittest.TestCase):

    def setUp(self):
        self.v = RentalValidator()
        self.c = Rental("1", "2", "3", datetime.date(2019, 11, 20), datetime.date(2019, 11, 27), datetime.date(2019, 11, 23))

    def testRental(self):
        self.assertTrue(self.v.validate, self.c)
        self.c.dueDate = datetime.date(2019, 11, 20)
        self.assertRaises(ValidatorException, self.v.validate, self.c)
        self.c.rentedDate = datetime.date(2017, 11, 11)
        self.assertRaises(ValidatorException, self.v.validate, self.c)



