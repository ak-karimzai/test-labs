from peewee import AutoField, CharField, ForeignKeyField, DateTimeField, TimeField
from Models.BaseModel import BaseModel
from Models.Excursion import ExcursionModelDB


class ScheduleModelDB(BaseModel):
    id = AutoField(null=False)
    excursionId = ForeignKeyField(ExcursionModelDB, field="id")
    day = CharField(null=False)
    time = TimeField(null=False)
