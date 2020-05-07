from operations import *

def testAddTransaction():
    l = []
    addTransaction('100 in food', l)
    assert len(l) == 1 and getValue(l[0]) == 100 and getType(l[0]) == 'in' and getDescription(l[0]) == 'food'
    addTransaction('550 out movie', l)
    assert len(l) == 2 and getValue(l[1]) == 550 and getType(l[1]) == 'out' and getDescription(l[1]) == 'movie'


def testInsertTransaction():
    l = []
    insertTransaction('10 100 in food', l)
    assert len(l) == 1 and getDay(l[0]) == 10 and getValue(l[0]) == 100 and getType(l[0]) == 'in' and getDescription(l[0]) == 'food'
    insertTransaction('10 550 out movie', l)
    assert len(l) == 2 and getDay(l[1]) == 10 and getValue(l[1]) == 550 and getType(l[1]) == 'out' and getDescription(l[1]) == 'movie'


def testRemove():
    l = [createTransaction(10, 100, 'in', 'food'), createTransaction(1, 550, 'out', 'movie'),
         createTransaction(5, 555, 'in', 'puzzle'), createTransaction(6, 1555, 'out', 'pizza'),
         createTransaction(15, 20, 'in', 'games'), createTransaction(17, 101, 'in', 'sweets')]
    removeInOut('out', l)
    assert len(l) == 6
    removeDay('10', l)
    assert len(l) == 5
    removeDayToDay('1 6', l)
    assert len(l) == 3
    removeTransaction('17', l)
    assert len(l) == 2
    assert getDay(l[1]) == 15


def testReplace():
    l = [createTransaction(10, 100, 'in', 'food')]
    replaceTransaction('10 in food with 500', l)
    assert len(l) == 1
    assert getValue(l[0]) == 500


def testSum():
    l = [createTransaction(10, 100, 'in', 'food'), createTransaction(1, 550, 'out', 'movie'),
         createTransaction(5, 555, 'in', 'puzzle'), createTransaction(6, 1555, 'out', 'pizza'),
         createTransaction(15, 20, 'in', 'games'), createTransaction(17, 101, 'in', 'sweets')]
    assert sum(['out'], l) == 2105


def testMax():
    l = [createTransaction(10, 100, 'in', 'food'), createTransaction(1, 550, 'out', 'movie'),
         createTransaction(10, 555, 'in', 'puzzle'), createTransaction(6, 1555, 'out', 'pizza'),
         createTransaction(15, 20, 'in', 'games'), createTransaction(17, 101, 'in', 'sweets')]
    assert max(['in', '10'], l) == 555


def test(transactionList):
    testAddTransaction()
    testInsertTransaction()
    testRemove()
    testReplace()
    testSum()
    testMax()
    transactionList.append([20, 67, 'in', 'pizza'])
    transactionList.append([10, 566, 'in', 'food'])
    transactionList.append([26, 10, 'out', 'movie'])
    transactionList.append([24, 90, 'out', 'icecream'])
    transactionList.append([11, 56, 'in', 'play'])
    transactionList.append([5, 68, 'in', 'clothes'])
    transactionList.append([10, 566, 'in', 'school'])
    transactionList.append([2, 180, 'out', 'make-up'])
    transactionList.append([4, 990, 'in', 'books'])
    transactionList.append([1, 500, 'out', 'puzzle'])