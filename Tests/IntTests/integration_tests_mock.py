import unittest, pytest, allure
from unittest.mock import Mock

from peewee import SqliteDatabase

from Models.Excursion import ExcursionModelDB
from Models.Guide import GuideModelDB
from Models.Schedule import ScheduleModelDB
from Services.ExcursionService import ExcursionService
from Services.GuideService import GuideService
from Services.ScheduleService import ScheduleService
from Tests.TestBuilders.ExcursionBuilder import ExcursionBuilder
from Tests.TestBuilders.GuideBuilder import GuideBuilder
from Tests.TestBuilders.ScheduleBuilder import ScheduleBuilder
from db_settings import database_proxy


class TestExcursionAndGuideService(unittest.TestCase):
    def test_create_user_and_subject_positive(self):
        # arrange
        guide = GuideBuilder(id=1, firstName="Andrey").build()
        excursion = ExcursionBuilder(id=1, name='Red Square Excursion', guideId=1, price=2000).build()

        # act
        new_guide = self.guideService.create_guide(guide)
        new_excursion = self.excursionService.create_excursion(excursion)
        # assert
        self.mockCreate.assert_called()
        self.assertEqual(guide.firstName, new_guide.firstName)
        self.assertEqual(excursion.name, new_excursion.name)
        self.assertEqual(str(excursion.guideId), str(new_excursion.guideId))
        self.assertEqual(excursion.price, new_excursion.price)

    def setUp(self):
        creation_mock()
        self.excursionService = ExcursionService('mockdb')
        self.guideService = GuideService('mockdb')
        self.mockCreate = Mock(
            return_value=ExcursionBuilder(id=1, name='Red Square Excursion', guideId=1, price=2000).build())
        self.excursionService.excursionRepository.create = self.mockCreate


class TestUserAndSubjectAndRecordService(unittest.TestCase):
    def test_create_user_and_subject_and_record_positive(self):
        # arrange
        guide = GuideBuilder(id=1, firstName="Andrey").build()
        excursion = ExcursionBuilder(id=1, name='Red Square Excursion', guideId=1, price=2000).build()
        schedule = ScheduleBuilder(id=1, excursionId=1, day='Monday', time='12:20').build()

        # act
        new_guide = self.guideService.create_guide(guide)
        new_excursion = self.excursionService.create_excursion(excursion)
        new_schedule = self.scheduleService.create_schedule(schedule)

        # assert
        self.assertEqual(guide.firstName, new_guide.firstName)
        self.assertEqual(str(excursion.guideId), str(new_excursion.guideId))
        self.assertEqual(excursion.name, new_excursion.name)
        self.assertEqual(excursion.price, new_excursion.price)
        self.assertEqual(schedule.day, new_schedule.day)
        self.assertEqual(schedule.time, new_schedule.time)

    def setUp(self):
        creation_mock()
        self.guideService = GuideService('mockdb')
        self.excursionService = ExcursionService('mockdb')
        self.mockCreateExcursion = Mock(
            return_value=ExcursionBuilder(id=1, name='Red Square Excursion', guideId=1, price=2000).build())
        self.excursionService.excursionRepository.create = self.mockCreateExcursion

        self.scheduleService = ScheduleService('mockdb')
        self.mockCreateSchedule = Mock(
            return_value=ScheduleBuilder(id=1, excursionId=1, day='Monday', time='12:20').build())
        self.scheduleService.scheduleRepository.create = self.mockCreateSchedule


def creation_mock():
    database = SqliteDatabase('mockdb')
    database_proxy.initialize(database)
    database.drop_tables([ExcursionModelDB, GuideModelDB, ScheduleModelDB])
    database.create_tables([ExcursionModelDB, GuideModelDB, ScheduleModelDB])


if __name__ == '__main__':
    unittest.main()