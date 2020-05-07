class RepositoryError(Exception):
    def __init__(self, msg):
        self._msg = msg

    @property
    def message(self):
        return self._msg