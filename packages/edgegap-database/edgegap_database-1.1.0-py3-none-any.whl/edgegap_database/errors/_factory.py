from sqlalchemy.exc import IntegrityError, DatabaseError

from ._exceptions import DatabaseUniqueViolationExceptions, DatabaseException


class DatabaseExceptionFactory:
    @staticmethod
    def handle(e: Exception):
        match e:
            case IntegrityError():
                raise DatabaseUniqueViolationExceptions(exception=e) from e
            case DatabaseError():
                raise DatabaseException(exception=e) from e
            case _:
                raise e
