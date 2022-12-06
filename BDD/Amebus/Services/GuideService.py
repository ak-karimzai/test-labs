from Amebus.Dtos.GuideDto import GuideDto
from Amebus.Entities.Guide import Guide
from Amebus.Logs.log import logger
from Amebus.Repositories.GuideRepository import GuideRepository


class GuideService:
    def __init__(self, url):
        self.guideRepository = GuideRepository(url)

    def get_guide(self, id):
        try:
            guide = self.guideRepository.findById(id)
            logger.info("Guide was received")
            return GuideDto(
                id=guide.id,
                firstName=guide.firstName,
                lastName=guide.lastName,
                patronymic=guide.patronymic,
                qualification=guide.qualification,
                biography = guide.biography,
                experience = guide.experience
            )
        except:
            logger.warning("Guide wasn't received")
            return None

    def get_guides(self):
        guides = self.guideRepository.findAll()
        result = []
        for guide in guides:
            result.append(GuideDto(
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

    def create_guide(self, createGuideDto):
        newGuide = Guide(
            firstName=createGuideDto.firstName,
            lastName=createGuideDto.lastName,
            patronymic=createGuideDto.patronymic,
            qualification=createGuideDto.qualification,
            biography=createGuideDto.biography,
            experience=createGuideDto.experience
        )
        try:
            guide = self.guideRepository.create(newGuide)
            logger.info("Guide was created")
            return GuideDto(
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

    def update_guide(self, updateGuideDto):
        updateGuide = Guide(
            id=updateGuideDto.id,
            firstName=updateGuideDto.firstName,
            lastName=updateGuideDto.lastName,
            patronymic=updateGuideDto.patronymic,
            qualification=updateGuideDto.qualification,
            biography=updateGuideDto.biography,
            experience=updateGuideDto.experience
        )
        try:
            guide = self.guideRepository.update(updateGuide)
            logger.info("Guide was updated")
            return GuideDto(
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

    def delete_guide(self, id):
        try:
            countDelete = self.guideRepository.delete(id)
            logger.info("Guide was deleted")
            return countDelete
        except:
            logger.warning("Guide wasn't deleted")
            return None
