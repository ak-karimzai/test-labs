from Services.GuideService import GuideService
from Logs.log import logger

class GuideController:
    def __init__(self, url):
        self.guideService = GuideService(url)

    def get_guide(self, id):
        try:
            logger.info("Guide was received")
            return self.guideService.get_guide(id)
        except:
            logger.warning("Guide wasn't received")
            return None

    def get_guides(self):
        try:
            logger.info("Guides was received")
            return self.guideService.get_guides()
        except:
            logger.warning("Guides wasn't received")
            return None

    def create_guide(self, createGuideDto):
        try:
            logger.info("Guide was created")
            return self.guideService.create_guide(createGuideDto)
        except:
            logger.warning("Guide wasn't created")
            return None

    def update_guide(self, updateGuideDto):
        try:
            logger.info("Guide was updated")
            return self.guideService.update_guide(updateGuideDto)
        except:
            logger.warning("Guide wasn't updated")
            return None

    def delete_guide(self, id):
        try:
            logger.info("Guide was deleted")
            return self.guideService.delete_guide(id)
        except:
            logger.warning("Guide wasn't deleted")
            return None