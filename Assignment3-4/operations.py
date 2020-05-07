import copy
from domain import *


def insertTransaction(params, transactionList):
    day, value, tpe, description = params.split(' ')
    if not (day.isnumeric() and value.isnumeric()):
        raise ValueError("The value and the day need to be integers.")
    transactionList.append(createTransaction(day, value, tpe, description))
    return True


def addTransaction(params, transactionList):
    value, tpe, description = params.split(' ')
    if not value.isnumeric():
        raise ValueError("The value needs to be an integer.")
    now = datetime.datetime.now()
    transactionList.append(createTransaction(now.day, value, tpe, description))
    return True


def removeInOut(lst, transactionList):
    if len(transactionList) != 0:
        transactionList[:] = filter(lambda a: getType(a) != lst[0], transactionList)
    else:
        raise ValueError("Can't remove anymore. Empty list.")


def removeDay(lst, transactionList):
    if len(transactionList) != 0:
        transactionList[:] = filter(lambda a: getDay(a) != int(lst[0]), transactionList)
    else:
        raise ValueError("Can't remove anymore. Empty list.")


def removeDayToDay(lst, transactionList):
    if len(transactionList) != 0:
        transactionList[:] = filter(lambda a: getDay(a) < int(lst[0]) or getDay(a) > int(lst[2]), transactionList)
    else:
        raise ValueError("Can't remove anymore. Empty list.")


def removeTransaction(params, transactionList):
    lst = params.split(' ')
    if len(lst) == 1 and type(lst[0]) == str and (lst[0] == "in" or lst[0] == "out"):
        removeInOut(lst, transactionList)
        return True
    elif len(lst) == 1 and lst[0].isnumeric() and 0 < int(lst[0]) <= 30:
        removeDay(lst, transactionList)
        return True
    elif len(lst) == 3 and (lst[1] == 'to' and lst[0].isnumeric() and lst[2].isnumeric() and 0 < int(lst[0]) < int(lst[2]) <= 30):
        removeDayToDay(lst, transactionList)
        return True
    else:
        raise ValueError("Wrong parameters.")


def replaceTransaction(params, transactionList):
    lst = params.split(' ')
    if not (lst[0].isnumeric() and lst[4].isnumeric()):
        raise ValueError("The first and the last parameters need to be integers.")
    if len(lst) == 5 and lst[3] == 'with':
        for m in transactionList:
            if getDay(m) == int(lst[0]) and getType(m) == lst[1] and getDescription(m) == lst[2]:
                m[1] = int(lst[4])
            else:
                raise ValueError("There is no transaction that matches your parameters.")


def listTransaction(params, transactionList,):
    if len(params) == 0:
        return listToString(transactionList)
    else:
        lst = params.split(' ')
        if (len(lst) == 1 and type(lst[0]) == str and (lst[0] == "in" or lst[0] == "out")):
            return listToString(listType(lst, transactionList))
        elif (len(lst) == 2 and (lst[0] == '<' or lst[0] == '=' or lst[0] == '>')):
            return listToString(listFromValue(lst, transactionList))
        elif (len(lst) == 2 and lst[0] == 'balance' and 0 < int(lst[1]) <= 30):
            return listBalance(lst, transactionList)
        else:
            raise ValueError("Wrong parameters.")


def listType(lst, transactionList):
    _list = transactionList
    _list = filter(lambda a: getType(a) == lst[0], _list)
    return _list


def listBalance(lst, transactionList):
    s = 0
    p = 0
    for m in transactionList:
        if(getDay(m) <= int(lst[1])):
            if(getType(m) == 'in'):
                s += getValue(m)
            else:
                p += getValue(m)
    return s-p


def listFromValue(lst, transactionList):
    _list = transactionList
    if not lst[1].isnumeric():
        raise ValueError("The second parameter needs to be an integer.")
    if lst[0] == '<':
        _list = filter(lambda a: getValue(a) < int(lst[1]), _list)
        return _list
    elif lst[0] == '=':
        _list = filter(lambda a: getValue(a) == int(lst[1]), _list)
        return _list
    elif lst[0] == '>':
        _list = filter(lambda a: getValue(a) > int(lst[1]), _list)
        return _list
    return "There is no transaction that matches your parameters."


def sum(lst, transactionList):
    s = 0
    for m in transactionList:
        if getType(m) == lst[0]:
            s += getValue(m)
    return s


def max(lst, transactionList):
    mx = 0
    for m in transactionList:
        if getType(m) == lst[0] and getDay(m) == int(lst[1]):
            if getValue(m) > mx:
                mx = getValue(m)
    return mx


def filter_(lst, transactionList):
    if len(lst) == 1:
        filterType(lst, transactionList)
        return True
    elif len(lst) == 2:
        filterTypeValue(lst, transactionList)
        return True
    else:
        raise ValueError("Wrong parameters.")


def filterType(lst, transactionList):
    if lst[0] == 'out' or lst[0] == 'in':
        transactionList[:] = filter(lambda a: getType(a) == lst[0], transactionList)
    else:
        raise ValueError("The parameter needs to be a type.")


def filterTypeValue(lst, transactionList):
    if (lst[0] == 'out' or lst[0] == 'in') and lst[1].isnumeric():
        transactionList[:] = filter(lambda a: getType(a) == lst[0] and getValue(a) < int(lst[1]), transactionList)
    else:
        raise ValueError("The parameters need to be a type and an integer.")


def undo(transactionList, undoList):
    transactionList.clear()
    transactionList.extend(copy.deepcopy(undoList.pop()))


def toString(m):
    return "Day: " + str(m[0]) + ", amount of money: " + str(m[1]) + ", transaction type: " + str(m[2]) + ", description: " + str(m[3])


def listToString(transactionList):
    string = ''
    for transaction in transactionList:
        string += toString(transaction)
        string += '\n'
    return string

