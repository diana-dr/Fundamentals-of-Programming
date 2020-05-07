import unittest
from Repository import *
from Driver import Driver
from Order import Order


class Test(unittest.TestCase):
    def setUp(self):
        self.d = Driver(1, "Alex")
        self.o = Order(1, 4)
        self._driver = Repository()
        self._order = Repository()

    def test(self):
        self.assertEqual(self.d.id, 1)
        self.assertEqual(self.d.name, "Alex")
        self.assertEqual(self.o.id, 1)
        self.assertEqual(self.o.distance, 4)
        self._driver.add([1, "Ion"])
        self.assertEqual(len(self._driver.getAll()), 1)
        self._driver.add([2, "Alin"])
        self.assertEqual(len(self._driver.getAll()), 2)
        self._order.add([1, 3])
        self._order.add([1, 10])
        self.assertEqual(len(self._order.getAll()), 2)


