from domain.ValidatorException import ValidatorException


class ClientValidator:

    def validate(self, client):
        _errors = []
        if type(client.id) != int or client.id <= 0:
            _errors.append("Wrong Id type or value!")
        if len(client.name) == 0:
            _errors.append("The name field can not be empty!")
        if len(_errors) != 0:
            raise ValidatorException(_errors)
