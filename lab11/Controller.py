from Order import Order


class Controller:
    def __init__(self, repo):
        self._repo = repo

    def addOrder(self, id, distance):
        o = Order(id, distance)
        self._repo.add(o)

    def getAll(self):
        return self._repo.getAll()


class DriverController:
    def __init__(self, repo, order):
        self._repo = repo
        self._order = order

    def getAll(self):
        return self._repo.getAll()

    def computeIncome(self, idn):
        ok = 0
        for a in self.getAll():
            if a.id == idn:
                ok = 1
        if ok == 0:
            raise ValueError("Driver not in repo!")
        s = 0
        for p in self._repo.getAll():
            if p.id == idn:
                m = p.name
        for a in self._order.getAll():
            if a.id == idn:
                s = s + a.distance

        p = s * 2.5

        return "Income: " + str(p) + " ID: " + str(idn) + " Driver: " + m