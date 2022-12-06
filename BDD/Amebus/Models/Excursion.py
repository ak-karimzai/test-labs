from peewee import PrimaryKeyField, ForeignKeyField, CharField, IntegerField
from Amebus.Models.BaseModel import BaseModel
from Amebus.Models.Guide import GuideModelDB


class ExcursionModelDB(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(null=False)
    description = CharField()
    guideId = ForeignKeyField(GuideModelDB, to_field="id")
    price = IntegerField(null=False)