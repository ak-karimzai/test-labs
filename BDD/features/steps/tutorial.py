from behave import *
from peewee import SqliteDatabase

from Amebus.Controllers.GuideController import GuideController
from Amebus.Controllers.ExcursionController import ExcursionController
from Amebus.Models.Guide import GuideModelDB
from Amebus.Models.Excursion import ExcursionModelDB
from Amebus.Models.Schedule import ScheduleModelDB
from Amebus.db_settings import database_proxy

from Amebus.Dtos.GuideDto import CreateGuideDto
from Amebus.Dtos.ExcursionDto import CreateExcursionDto




@given('I put guide {firstName} {lastName} and his {experience} parameters')
def step_impl(context, firstName, lastName, experience):
    context.create_guide = CreateGuideDto(
        firstName=firstName,
        lastName=lastName,
        patronymic='',
        qualification='',
        biography="",
        experience=experience

    )

@when('I create request')
def step_impl(context):
    guideController = GuideController('amebus.db')
    context.created_guide = guideController.create_guide(context.create_guide)
    assert True is not False

@then('I should be guide named {firstName}')
def step_impl(context, firstName):
    assert context.created_guide.firstName == firstName


@given('I put excursion {name} {description} {guideId} {price} parameters')
def step_impl(context,name, description, guideId, price):
    context.create_excursion = CreateExcursionDto(
        name=name,
        description = description,
        guideId=int(guideId),
        price = int(price)
    )

@when('I create excursion request')
def step_impl(context):
    excursionController = ExcursionController('amebus.db')
    context.created_excursion = excursionController.create_excursion(context.create_excursion)
    assert True is not False

@then('I should have excursion with {name} {description} {guideId} {price}')
def step_impl(context, name, description, guideId, price):
    assert context.created_excursion.name == name
    assert context.created_excursion.description == description
    assert str(context.created_excursion.guideId) == str(guideId)
    assert context.created_excursion.price == int(price)


def creation():
    # Based on configuration, use a different database.
    database = SqliteDatabase('amebus.db')
    # Configure our proxy to use the db we specified in config.
    database_proxy.initialize(database)
    database.drop_tables([ExcursionModelDB, GuideModelDB, ScheduleModelDB])
    database.create_tables([ExcursionModelDB, GuideModelDB, ScheduleModelDB])

creation()