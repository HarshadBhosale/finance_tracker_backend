import database

def create_not_existence_tables():
    for table in database.BaseModel.__subclasses__():
        if not database.db.table_exists(table.__name__):
            table.create_table()
