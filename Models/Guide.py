from peewee import PrimaryKeyField, CharField, IntegerField
from Models.BaseModel import BaseModel


class GuideModelDB(BaseModel):
    id = PrimaryKeyField(null=False)
    firstName = CharField(null=False, unique=True)
    lastName = CharField()
    patronymic = CharField()
    qualification = CharField()
    biography = CharField()
    experience = IntegerField()
