from ..Entities.Excursion import Excursion
from ..Logs.log import logger
from ..Models.Excursion import ExcursionModelDB
from ..db_settings import database_proxy, database_connect


class ExcursionRepository:
    def __init__(self, url):
        # Based on configuration, use a different database.
        self.database = database_connect(url)
        # Configure our proxy to use the db we specified in config.
        database_proxy.initialize(self.database)
        self.ExcursionModelDB = ExcursionModelDB

    def findById(self, id):
        try:
            excursion = self.ExcursionModelDB.get(ExcursionModelDB.id == id)
            logger.info("Excursion was received")
            return Excursion(
                    id = excursion.id,
                    name = excursion.name,
                    description = excursion.description,
                    guideId = excursion.guideId,
                    price = excursion.price
                )
        except:
            logger.warning("Excursion wasn't received")
            return None


    def findAll(self):
        excursions = self.ExcursionModelDB.select()
        result = []
        for excursion in excursions:
            result.append(Excursion(
                    id = excursion.id,
                    name = excursion.name,
                    description = excursion.description,
                    guideId = excursion.guideId,
                    price = excursion.price
                ))
        logger.info("Excursions was received")
        return result

    def create(self, newExcursion):
        try:
            excursion = self.ExcursionModelDB(
                name=newExcursion.name,
                description=newExcursion.description,
                guideId=newExcursion.guideId,
                price=newExcursion.price
            )
            excursion.save()
            logger.info("Excursion was created")
            return Excursion(
                    id = excursion.id,
                    name = excursion.name,
                    description = excursion.description,
                    guideId = excursion.guideId,
                    price = excursion.price
                )
        except:
            logger.warning("Excursion wasn't created")
            return None


    def update(self, updateExcursion):
        try:
            excursion = self.ExcursionModelDB.get(ExcursionModelDB.id == id)
            excursion.name = updateExcursion.name
            excursion.description = updateExcursion.description
            excursion.guideId = updateExcursion.guideId
            excursion.price = updateExcursion.price
            excursion.save()
            logger.info("Excursion was updated")
            return Excursion(
                    id = excursion.id,
                    name = excursion.name,
                    description = excursion.description,
                    guideId = excursion.guideId,
                    price = excursion.price
                )
        except:
            logger.warning("Excursion wasn't updated")
            return None

    def delete(self, id):
        try:
            record = self.ExcursionModelDB.get(ExcursionModelDB.id == id)
            logger.info("Excursion was deleted")
            return record.delete_instance()
        except:
            logger.warning("Excursion wasn't deleted")
            return None