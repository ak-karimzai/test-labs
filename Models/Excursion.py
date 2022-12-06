from peewee import PrimaryKeyField, ForeignKeyField, CharField, IntegerField
from Models.BaseModel import BaseModel
from Models.Guide import GuideModelDB


class ExcursionModelDB(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(null=False)
    description = CharField()
    guideId = ForeignKeyField(GuideModelDB, to_field="id")
    price = IntegerField(null=False)