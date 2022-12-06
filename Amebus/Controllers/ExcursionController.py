from Services.ExcursionService import ExcursionService
from Logs.log import logger

class ExcursionController:
    def __init__(self, url):
        self.excursionService = ExcursionService(url)

    def get_excursion(self, id):
        try:
            logger.info("Excursion was received")
            return self.excursionService.get_excursion(id)
        except:
            logger.warning("Excursion wasn't received")
            return None

    def get_excursions(self):
        try:
            logger.info("Excursions was received")
            return self.excursionService.get_excursions()
        except:
            logger.warning("Excursions wasn't received")
            return None

    def create_excursion(self, createExcursionDto):
        try:
            logger.info("Excursion was created")
            return self.excursionService.create_excursion(createExcursionDto)
        except:
            logger.warning("Excursion wasn't created")
            return None

    def update_excursion(self, updateExcursionDto):
        try:
            logger.info("Excursion was updated")
            return self.excursionService.update_excursion(updateExcursionDto)
        except:
            logger.warning("Excursion wasn't updated")
            return None

    def delete_excursion(self, id):
        try:
            logger.info("Excursion was deleted")
            return self.excursionService.delete_excursion(id)
        except:
            logger.warning("Excursion wasn't deleted")
            return None