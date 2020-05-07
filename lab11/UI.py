class UI:
    def __init__(self, order, driver):
        self._order = order
        self._driver = driver

    menuOptions = {
        0: "0.Exit",
        1: "1.Add order",
        2: "2.Display orders",
        3: "3.Compute income"
        }

    def showMenu(self):
        for a in self.menuOptions.values():
            print(a)

    def readString(self, text):
        a = input(text)
        return a.strip()

    def addOrder(self):
        id = int(self.readString("ID: "))
        ok = 0
        for a in self._repo.getAll():
            if a.id == int(id):
                ok = 1
        if ok == 0:
            raise ValueError("Driver not in repo!")
        dist = int(self.readString("Distance in km: "))
        if dist < 1:
            raise ValueError("Distance too short.")
        self._order.addOrder(id, dist)

    def listOrders(self):
        for a in self._order.getAll():
            print(a)

    def listDrivers(self):
        for a in self._driver.getAll():
            print(a)

    def computeIncome(self):
        id = int(self.readString("ID: "))
        print(self._driver.computeIncome(id))

    def start(self):
        while True:
            print("Menu: ")
            self.showMenu()
            option = self.readString("Choose: ")
            if option.isnumeric():
                option = int(option)
            try:
                if option == 0:
                    return
                elif option == 1:
                    self.addOrder()
                elif option == 2:
                    self.listOrders()
                elif option == 3:
                    self.computeIncome()
                elif option == 4:
                    self.listDrivers()
                else:
                    print("Invalid command!")
            except Exception as e:
                print(e)