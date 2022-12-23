from peewee import AutoField, CharField, IntegerField
from Models.BaseModel import BaseModel


class GuideModelDB(BaseModel):
    id = AutoField(null=False)
    firstName = CharField(null=False, unique=True)
    lastName = CharField()
    patronymic = CharField()
    qualification = CharField()
    biography = CharField()
    experience = IntegerField()
