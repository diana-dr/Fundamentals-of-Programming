from domain.ValidatorException import ValidatorException
import datetime


class RentalValidator:

    def validate(self, rental):
        _errorList = []
        now = datetime.date.today()
        if rental.rentedDate < now:
            _errorList.append("The rental starts in the past!")
        if rental.rentedDate == rental.dueDate:
            _errorList.append("Rental must be at least one day!")
        if len(_errorList) != 0:
            raise ValidatorException(_errorList)
