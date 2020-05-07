class UndoController:
    def __init__(self):
        self._operations = []
        self._index = -1
        self._CF = False

    def addOperation(self, operation):
        if self._CF:
            return

        self._operations = self._operations[:self._index + 1]
        self._index += 1
        self._operations.append(operation)

    def undo(self):
        if self._index < 0:
            return False

        self._CF = True
        self._operations[self._index].undo()
        self._CF = False
        self._index -= 1
        return True

    def redo(self):
        if self._index >= len(self._operations):
            return False

        self._index += 1
        self._operations[self._index].redo()
        return True

    @property
    def operations(self):
        return self._operations


class Operation:
    def __init__(self, undoFunction, redoFunction):
        self._undoFunction = undoFunction
        self._redoFunction = redoFunction

    def undo(self):
        self._undoFunction.call()

    def redo(self):
        self._redoFunction.call()


class FunctionCall:
    def __init__(self, function, *params):
        self._func = function
        self._params = params

    def call(self):
        self._func(*self._params)