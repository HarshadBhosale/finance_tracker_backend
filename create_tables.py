from database import db, BaseModel

def create_not_existence_tables():
    for table in BaseModel.__subclasses__():
        if not db.table_exists(table.__name__):
            table.create_table()
