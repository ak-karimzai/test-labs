from peewee import Model
from ..db_settings import database_proxy


class BaseModel(Model):
    class Meta:
        database = database_proxy  # Use proxy for our DB.