from Controller import *
from Repository import *
from UI import UI


def main():
    repo = OrderTextFileRepo()
    repo1 = DriverTextFileRepo()
    ctrl = Controller(repo)
    ctrl1 = DriverController(repo1, repo)
    ui = UI(ctrl, ctrl1)
    ui.start()

main()