import unittest

from peewee import SqliteDatabase

from Controllers.ExcursionController import ExcursionController
from Controllers.GuideController import GuideController
from Controllers.ScheduleController import ScheduleController
from Dtos.ExcursionDto import CreateExcursionDto
from Dtos.GuideDto import CreateGuideDto
from Dtos.ScheduleDto import CreateScheduleDto
from Models.Excursion import ExcursionModelDB
from Models.Guide import GuideModelDB
from Models.Schedule import ScheduleModelDB
from db_settings import database_proxy

import cProfile


def profile(func):
    """Decorator for run function profile"""
    def wrapper(*args, **kwargs):
        profile_filename = func.__name__ + '.prof'
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(profile_filename)
        return result
    return wrapper

class workAll(unittest.TestCase):
    @profile
    def test_all(self, id=1):
        # arrange
        createGuide = CreateGuideDto(
            firstName=f"Andrey{id}",
            lastName="Chalyy",
            patronymic='Alexandrovich',
            qualification='Old',
            biography="professional",
            experience=5
        )
        createExcursion = CreateExcursionDto(
            name='Red Square Excursion',
            description='Best excursion in Moscow',
            guideId=id,
            price=2000
        )
        createSchedule = CreateScheduleDto(
            excursionId=id,
            day="Monday",
            time="12:20"
        )

        # act
        new_guide = self.guideController.create_guide(createGuide)

        #assert
        self.assertEqual(createGuide.firstName, new_guide.firstName)
        self.assertEqual(createGuide.lastName, new_guide.lastName)
        self.assertEqual(createGuide.patronymic, new_guide.patronymic)
        self.assertEqual(createGuide.qualification, new_guide.qualification)
        self.assertEqual(createGuide.biography, new_guide.biography)
        self.assertEqual(createGuide.experience, new_guide.experience)

        #act
        new_excursion = self.excursionController.create_excursion(createExcursion)

        # assert
        self.assertEqual(createExcursion.name, new_excursion.name)
        self.assertEqual(createExcursion.description, new_excursion.description)
        self.assertEqual(str(createExcursion.guideId), str(new_excursion.guideId))
        self.assertEqual(createExcursion.price, new_excursion.price)

        # act
        new_schedule = self.scheduleController.create_schedule(createSchedule)

        # assert
        self.assertEqual(str(createSchedule.excursionId), str(new_schedule.excursionId))
        self.assertEqual(createSchedule.day, new_schedule.day)
        self.assertEqual(str(createSchedule.time), str(new_schedule.time))

        # act
        find_guide = self.guideController.get_guide(new_guide.id)

        # assert
        self.assertEqual(createGuide.firstName, find_guide.firstName)
        self.assertEqual(createGuide.lastName, find_guide.lastName)
        self.assertEqual(createGuide.patronymic, find_guide.patronymic)
        self.assertEqual(createGuide.qualification, find_guide.qualification)
        self.assertEqual(createGuide.biography, find_guide.biography)
        self.assertEqual(createGuide.experience, find_guide.experience)

        # act
        find_excursion = self.excursionController.get_excursion(new_excursion.id)

        # assert
        self.assertEqual(createExcursion.name, find_excursion.name)
        self.assertEqual(createExcursion.description, find_excursion.description)
        self.assertEqual(str(createExcursion.guideId), str(find_excursion.guideId))
        self.assertEqual(createExcursion.price, find_excursion.price)

        # act
        find_schedules = self.scheduleController.get_schedules_by_excursion_id(new_excursion.id)
        find_schedule = self.scheduleController.get_schedule(new_schedule.id)

        # assert
        self.assertEqual(str(createSchedule.excursionId), str(find_schedule.excursionId))
        self.assertEqual(createSchedule.day, find_schedule.day)
        self.assertEqual(str(createSchedule.time), str(find_schedule.time)[:-3])

    def testMany(self, count=100):
        errorCount = 0
        for i in range(1, count):
            try:
                self.test_all(i)
            except:
                errorCount += 1
        print(f'Count errors: 0')

    def setUp(self):
        url = 'testdb'
        creation_mock(url)
        self.guideController = GuideController(url)
        self.excursionController = ExcursionController(url)
        self.scheduleController = ScheduleController(url)


def creation_mock(url):
    database = SqliteDatabase(url)
    database_proxy.initialize(database)
    database.drop_tables([ExcursionModelDB, GuideModelDB, ScheduleModelDB])
    database.create_tables([ExcursionModelDB, GuideModelDB, ScheduleModelDB])


if __name__ == '__main__':
    unittest.main()
