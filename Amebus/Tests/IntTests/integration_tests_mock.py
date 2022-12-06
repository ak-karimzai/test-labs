import unittest
from unittest.mock import Mock

from peewee import SqliteDatabase

from Amebus.Models.Excursion import ExcursionModelDB
from Amebus.Models.Guide import GuideModelDB
from Amebus.Models.Schedule import ScheduleModelDB
from Amebus.Services.ExcursionService import ExcursionService
from Amebus.Services.GuideService import GuideService
from Amebus.Services.ScheduleService import ScheduleService
from Amebus.Tests.TestBuilders.ExcursionBuilder import ExcursionBuilder
from Amebus.Tests.TestBuilders.GuideBuilder import GuideBuilder
from Amebus.Tests.TestBuilders.ScheduleBuilder import ScheduleBuilder
from Amebus.db_settings import database_proxy


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
        self.excursionService = ExcursionService('mockamebus.db')
        self.guideService = GuideService('mockamebus.db')
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
        self.guideService = GuideService('mockamebus.db')
        self.excursionService = ExcursionService('mockamebus.db')
        self.mockCreateExcursion = Mock(
            return_value=ExcursionBuilder(id=1, name='Red Square Excursion', guideId=1, price=2000).build())
        self.excursionService.excursionRepository.create = self.mockCreateExcursion

        self.scheduleService = ScheduleService('mockamebus.db')
        self.mockCreateSchedule = Mock(
            return_value=ScheduleBuilder(id=1, excursionId=1, day='Monday', time='12:20').build())
        self.scheduleService.scheduleRepository.create = self.mockCreateSchedule


def creation_mock():
    database = SqliteDatabase('mockamebus.db')
    database_proxy.initialize(database)
    database.drop_tables([ExcursionModelDB, GuideModelDB, ScheduleModelDB])
    database.create_tables([ExcursionModelDB, GuideModelDB, ScheduleModelDB])


if __name__ == '__main__':
    unittest.main()