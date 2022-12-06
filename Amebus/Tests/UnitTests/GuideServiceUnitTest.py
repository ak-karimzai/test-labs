import unittest
from unittest.mock import Mock

from peewee import SqliteDatabase

from Amebus.Dtos.GuideDto import GuideDto, CreateGuideDto
from Amebus.Models.Excursion import ExcursionModelDB
from Amebus.Models.Guide import GuideModelDB
from Amebus.Models.Schedule import ScheduleModelDB
from Amebus.Services.GuideService import GuideService
from Amebus.Tests.TestBuilders.GuideBuilder import GuideBuilder
from Amebus.db_settings import database_proxy


class AddGuideTestSuite(unittest.TestCase):
    def test_create_guide_positive(self):
        #arrange
        guide = CreateGuideDto(
            firstName = "Andrey",
            lastName = "test",
            patronymic = "test",
            qualification = "test",
            biography = "test",
            experience = 0
            )
        #act
        new_guide = self.guideService.create_guide(guide)

        # assert
        self.mockCreate.assert_called()
        self.assertEqual(guide.firstName, new_guide.firstName)

    def test_create_guide_negative(self):
        #arrange
        guide = CreateGuideDto(
                firstName="Andrey",
                lastName="test",
                patronymic="test",
                qualification="test",
                biography="test",
                experience=0
            )
        self.guideService.guideRepository.create = self.stub

        #act
        new_guide = self.guideService.create_guide(guide)

        # assert
        self.assertIsNone(new_guide)

    def stub(self):
        return None

    def setUp(self):
        self.guideService = GuideService('tmp')
        self.mockCreate = Mock(return_value=GuideBuilder(id=1, firstName='Andrey').build())
        self.guideService.guideRepository.create = self.mockCreate


class FindGuideTestSuite(unittest.TestCase):
    def test_find_guide_positive(self):
        # arrange
        guide = GuideDto(
            id = 1,
            firstName="Andrey",
            lastName="test",
            patronymic="test",
            qualification="test",
            biography="test",
            experience=0
        )

        # act
        find_guide = self.guideService.get_guide(guide.id)
        # assert
        self.mockFind.assert_called()
        self.assertEqual(guide.id, find_guide.id)
        self.assertEqual(guide.firstName, find_guide.firstName)

    def test_find_guide_negative(self):
        # arrange
        guide = GuideDto(
            id=1,
            firstName="Andrey",
            lastName="test",
            patronymic="test",
            qualification="test",
            biography="test",
            experience=0
        )
        self.guideService.guideRepository.findById = self.stub

        # act
        find_guide = self.guideService.get_guide(guide.id)

        # assert
        self.assertIsNone(find_guide)

    def stub(self):
        return None

    def setUp(self):
        self.guideService = GuideService('tmp')
        self.mockFind = Mock(
            return_value=GuideBuilder(id=1, firstName='Andrey').build())
        self.guideService.guideRepository.findById = self.mockFind


class UpdateGuideTestSuite(unittest.TestCase):
    def test_update_guide_positive(self):
        # arrange
        guide = GuideDto(
            id=1,
            firstName="Andrey",
            lastName="test",
            patronymic="test",
            qualification="test",
            biography="test",
            experience=0
        )

        # act
        update_guide = self.guideService.update_guide(guide)

        # assert
        self.mockUpdate.assert_called()
        self.assertEqual(guide.id, update_guide.id)
        self.assertEqual(guide.firstName, update_guide.firstName)

    def test_update_guide_negative(self):
        # arrange
        guide = GuideDto(
            id=1,
            firstName="Andrey",
            lastName="test",
            patronymic="test",
            qualification="test",
            biography="test",
            experience=0
        )
        self.guideService.guideRepository.update = self.stub

        # act
        update_guide = self.guideService.update_guide(guide)

        # assert
        self.assertIsNone(update_guide)

    def stub(self):
        return None

    def setUp(self):
        self.guideService = GuideService('tmp')
        self.mockUpdate = Mock(
            return_value=GuideBuilder(id=1, firstName='Andrey').build())
        self.guideService.guideRepository.update = self.mockUpdate


class DeleteGuideTestSuite(unittest.TestCase):
    def test_delete_guide_positive(self):
        # arrange
        guide = GuideDto(
            id=1,
            firstName="Andrey",
            lastName="test",
            patronymic="test",
            qualification="test",
            biography="test",
            experience=0
        )

        # act
        delete_guide = self.guideService.delete_guide(guide)

        # assert
        self.mockDelete.assert_called()
        self.assertEqual(guide.id, delete_guide.id)

    def test_delete_guide_negative(self):
        # arrange
        guide = GuideDto(
            id=1,
            firstName="Andrey",
            lastName="test",
            patronymic="test",
            qualification="test",
            biography="test",
            experience=0
        )
        self.guideService.guideRepository.delete = self.stub

        # act
        delete_guide = self.guideService.delete_guide(guide)

        # assert
        self.assertIsNone(delete_guide)


    def stub(self):
        return 0

    def setUp(self):
        self.guideService = GuideService('tmp')
        self.mockDelete = Mock(
            return_value=GuideBuilder(id=1, firstName='Andrey').build())
        self.guideService.guideRepository.delete = self.mockDelete

if __name__ == '__main__':
    unittest.main()
