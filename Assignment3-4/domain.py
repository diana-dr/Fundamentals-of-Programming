import datetime


def createTransaction(day, value, tpe, description):
    if int(day) <= 0 or int(day) > 31 or day == None:
        raise ValueError("Invalid day. Has to be between 1 and 30.")
    if int(value) <= 0 or value == None:
        raise ValueError("Invalid amount of money.")
    if not (tpe == 'in' or tpe == 'out'):
        raise ValueError("Invalid type.")
    if description == None:
        raise ValueError("Description needed.")
    return [int(day), int(value), tpe, description]


def getDay(m):
    return m[0]


def getValue(m):
    return m[1]


def getType(m):
    return m[2]


def getDescription(m):
    return m[3]
