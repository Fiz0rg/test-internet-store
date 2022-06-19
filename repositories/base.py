from databases import Database


class BaseClass:
    """ Базовый класс для всех классов репозитория. """

    def __init__(self, database: Database):
        self.database = database
