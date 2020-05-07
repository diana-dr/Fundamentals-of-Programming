from copy import deepcopy
from tests import *


def addTransactionUI(params, transactionList, undoList):
    if len(params) == 0:
        raise ValueError("Wrong number of parameters.")
    list = params.split(' ')
    if len(list) != 3:
        raise ValueError("Wrong number of parameters.")
    addTransaction(params, transactionList)


def insertTransactionUI(params, transactionList, undoList):
    if len(params) == 0:
        raise ValueError("Wrong number of parameters.")
    list = params.split(' ')
    if len(list) != 4:
        raise ValueError("Wrong number of parameters.")
    insertTransaction(params, transactionList)


def removeTransactionUI(params, transactionList, undoList):
    if len(params) == 0:
        raise ValueError("Wrong number of parameters.")
    if not removeTransaction(params, transactionList):
        raise ValueError("Wrong parameters.")


def replaceTransactionUI(params, transactionList, undoList):
    if len(params) == 0:
        raise ValueError("Wrong number of parameters.")
    if not replaceTransaction(params, transactionList):
        raise ValueError("Wrong parameters.")


def listTransactionUI(params, transactionList, undoList):
    print(listTransaction(params, transactionList))


def sumUI(params, transactionList, undoList):
    if len(params) == 0:
        raise ValueError("Wrong number of parameters.")
    lst = params.split(' ')
    if lst[0] != 'in' and lst[0] != 'out':
        raise ValueError("Wrong parameters. You need to insert a type.")
    if len(lst) != 1:
        raise ValueError("Wrong number of parameters.")
    else:
        print(sum(lst, transactionList))


def maxUI(params, transactionList, undoList):
    if len(params) == 0:
        raise ValueError("Wrong number of parameters.")
    lst = params.split(' ')
    if (lst[0] != 'in' and lst[0] != 'out') or (not lst[1].isdigit()):
        raise ValueError("Wrong parameters. You need to insert a type and a day.")
    if len(lst) != 2:
        raise ValueError("Wrong number of parameters.")
    else:
        print(max(lst, transactionList))


def filterUI(params, transactionList, undoList):
    undoList.append(copy.deepcopy(transactionList))
    if len(params) == 0:
        raise ValueError("Wrong number of parameters.")
    lst = params.split(' ')
    if len(lst) > 2:
        raise ValueError("Wrong number of parameters.")
    filter_(lst, transactionList)


def undoUI(params, transactionList, undoList):
    if not undoList:
        raise IndexError("No more undo's.")
    undo(transactionList, undoList)


def readCommand():
    cmd = input("Hello John! What can I help you with ?: ")
    cmd.strip()
    if cmd.find(' ') == -1:
        command = cmd
        params = []
    else:
        command = cmd[0:cmd.find(' ')]
        params = cmd[cmd.find(' ')+1:]
    return command, params


def run():
    commandsMenu = {'add': addTransactionUI,
                    'insert': insertTransactionUI,
                    'remove': removeTransactionUI,
                    'replace': replaceTransactionUI,
                    'list': listTransactionUI,
                    'sum': sumUI,
                    'max': maxUI,
                    'filter': filterUI,
                    'undo': undoUI}

    transactionList = []
    undoList = []
    test(transactionList)
    while True:
        undoList.append(copy.deepcopy(transactionList))
        menu()
        cmd = readCommand()
        command = cmd[0]
        params = cmd[1]
        try:
            transactionList.sort()
            if command == 'exit':
                return
            elif command in commandsMenu:
                commandsMenu[command](params, transactionList, undoList)
            else:
                print("Invalid command")
        except Exception as e:
            print(e)


def menu():
    print("Menu: ")
    print("  add = add new transaction to the list")
    print("  insert = insert a transaction to a given day")
    print("  remove = remove transactions from the list")
    print("  replace = replace the value of a transaction")
    print("  list = list the transactions having different properties")
    print("  sum = write the total amount from in/out transactions")
    print("  max = write the maximum in/out transaction on a given day")
    print("  exit")