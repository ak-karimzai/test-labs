from peewee import PrimaryKeyField, CharField, ForeignKeyField, DateTimeField, TimeField
from Models.BaseModel import BaseModel
from Models.Excursion import ExcursionModelDB


class ScheduleModelDB(BaseModel):
    id = PrimaryKeyField(null=False)
    excursionId = ForeignKeyField(ExcursionModelDB, to_field="id")
    day = CharField(null=False)
    time = TimeField(null=False)
