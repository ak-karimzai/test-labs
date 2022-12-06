import sys
sys.path.append("..")

from Entities.Guide import Guide
from Logs.log import logger
from Models.Guide import GuideModelDB
from db_settings import database_proxy, database_connect


class GuideRepository:
    def __init__(self, url):
        # Based on configuration, use a different database.
        self.database = database_connect(url)
        # Configure our proxy to use the db we specified in config.
        database_proxy.initialize(self.database)
        self.GuideModelDB = GuideModelDB

    def findById(self, id):
        try:
            guide = self.GuideModelDB.get(GuideModelDB.id == id)
            logger.info("Guide was received")
            return Guide(
                id = guide.id,
                firstName = guide.firstName,
                lastName = guide.lastName,
                patronymic = guide.patronymic,
                qualification = guide.qualification,
                biography = guide.biography,
                experience = guide.experience
            )
        except:
            logger.warning("Guide wasn't received")
            return None


    def findAll(self):
        guides = self.GuideModelDB.select()
        result = []
        for guide in guides:
            result.append(Guide(
                id=guide.id,
                firstName=guide.firstName,
                lastName=guide.lastName,
                patronymic=guide.patronymic,
                qualification=guide.qualification,
                biography=guide.biography,
                experience=guide.experience
            ))
        logger.info("Guide was received")
        return result


    def create(self, newGuide):
        try:
            guide = self.GuideModelDB(
                firstName=newGuide.firstName,
                lastName=newGuide.lastName,
                patronymic=newGuide.patronymic,
                qualification=newGuide.qualification,
                biography=newGuide.biography,
                experience=newGuide.experience
            )
            guide.save()
            logger.info("Guide was created")
            return Guide(
                id=guide.id,
                firstName=guide.firstName,
                lastName=guide.lastName,
                patronymic=guide.patronymic,
                qualification=guide.qualification,
                biography=guide.biography,
                experience=guide.experience
            )
        except:
            logger.warning("Guide wasn't created")
            return None


    def update(self, updateGuide):
        try:
            guide = self.GuideModelDB.get(GuideModelDB.id == id)
            guide.firstName = updateGuide.firstName
            guide.lastName = updateGuide.lastName
            guide.patronymic = updateGuide.patronymic
            guide.qualification = updateGuide.qualification
            guide.biography = updateGuide.biography
            guide.experience = updateGuide.experience
            guide.save()
            logger.info("Guide was updated")
            return Guide(
                id=guide.id,
                firstName=guide.firstName,
                lastName=guide.lastName,
                patronymic=guide.patronymic,
                qualification=guide.qualification,
                biography=guide.biography,
                experience=guide.experience
            )
        except:
            logger.warning("Guide wasn't updated")
            return None

    def delete(self, id):
        try:
            guide = self.GuideModelDB.get(GuideModelDB.id == id)
            logger.info("Guide was deleted")
            return guide.delete_instance()
        except:
            logger.warning("Guide wasn't deleted")
            return None