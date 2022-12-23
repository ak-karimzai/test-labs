from peewee import AutoField, ForeignKeyField, CharField, IntegerField
from Models.BaseModel import BaseModel
from Models.Guide import GuideModelDB


class ExcursionModelDB(BaseModel):
    id = AutoField(null=False)
    name = CharField(null=False)
    description = CharField()
    guideId = ForeignKeyField(GuideModelDB, field="id")
    price = IntegerField(null=False)