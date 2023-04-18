import peewee
import Database.Models.base_model
import uuid


class Files(Database.Models.base_model.BaseModel):
    id = peewee.UUIDField(unique=True, default=uuid.uuid4)
    file = peewee.BlobField()
