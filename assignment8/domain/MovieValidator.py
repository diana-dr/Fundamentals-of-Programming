from domain.ValidatorException import ValidatorException


class MovieValidator:

    def validate(self, movie):
        errors = []

        if type(movie.id) != int or movie.id <= 0:
            errors.append("Wrong Id type or value!")
        if len(movie.title) == 0:
            errors.append("The field title can not be empty!")
        if len(movie.description) == 0:
            errors.append("The field description can not be empty!")
        if len(movie.genre) == 0:
            errors.append("The field genre can not be empty!")
        if len(errors) != 0:
            raise ValidatorException(errors)