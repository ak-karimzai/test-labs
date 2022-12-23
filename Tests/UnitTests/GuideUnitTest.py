import unittest, pytest, allure
from peewee import SqliteDatabase, IntegrityError

from Models.Excursion import ExcursionModelDB
from Models.Guide import GuideModelDB
from Models.Schedule import ScheduleModelDB
from Repositories.GuideRepository import GuideRepository
from Tests.TestBuilders.GuideBuilder import GuideBuilder
from db_settings import database_proxy


class AddGuideTestSuite(unittest.TestCase):
    def test_create_guide_positive(self):
        #arrange
        guide = GuideBuilder(id=1, firstName='Andrey').build()
        new_guide = self.guideRepository.create(guide)

        #assert
        self.assertEqual(str(guide.firstName), str(new_guide.firstName))
        self.assertEqual(guide.firstName, new_guide.firstName)

    def test_create_guide_negative(self):
        #arrange
        guide = GuideBuilder(id=1, firstName='Andrey').build()

        #act
        self.guideRepository.create(guide)
        new_guide = self.guideRepository.create(guide)

        #assert
        self.assertIsNone(new_guide)


    def setUp(self):
        creation_mock()
        self.guideRepository = GuideRepository('mockdb')


class DeleteGuideTestSuite(unittest.TestCase):
    def test_delete_guide_positive(self):
        # arrange
        guide = GuideBuilder(id=1, firstName='Andrey').build()

        # act
        new_guide = self.guideRepository.create(guide)
        countDelete = self.guideRepository.delete(new_guide.id)
        guide = self.guideRepository.findById(new_guide.id)

        # assert
        self.assertEqual(1, countDelete)
        self.assertIsNone(guide)

    def test_delete_guide_negative(self):
        # arrange
        id = 0

        # act
        delete_guide = self.guideRepository.delete(id)
        guide = self.guideRepository.findById(id)

        # assert
        self.assertIsNone(delete_guide)
        self.assertIsNone(guide)

    def setUp(self):
        creation_mock()
        self.guideRepository = GuideRepository('mockdb')


class FindGuideTestSuite(unittest.TestCase):
    def test_find_guide_positive(self):
        # arrange
        guide = GuideBuilder(id=1, firstName='Andrey').build()

        # act
        new_guide = self.guideRepository.create(guide)
        guideFind = self.guideRepository.findById(new_guide.id)

        # assert
        self.assertEqual(guideFind.id, new_guide.id)
        self.assertEqual(str(guideFind.firstName), str(new_guide.firstName))

    def test_find_guide_negative(self):
        # arrange
        id = 0

        # act
        guide = self.guideRepository.findById(id)

        # assert
        self.assertIsNone(guide)

    def setUp(self):
        creation_mock()
        self.guideRepository = GuideRepository('mockdb')

def creation_mock():
    database = SqliteDatabase('mockdb')
    database_proxy.initialize(database)
    database.drop_tables([ExcursionModelDB, GuideModelDB, ScheduleModelDB])
    database.create_tables([ExcursionModelDB, GuideModelDB, ScheduleModelDB])

if __name__ == '__main__':
    #creation_mock()
    unittest.main()