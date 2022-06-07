from databases import Database


class BaseClass:
    def __init__(self, database: Database):
        self.database = database
