from Dtos.ExcursionDto import ExcursionDto
from Entities.Excursion import Excursion
from Repositories.ExcursionRepository import ExcursionRepository


class ExcursionService:
    def __init__(self, url):
        self.excursionRepository = ExcursionRepository(url)

    def get_excursion(self, id):
        excursion = self.excursionRepository.findById(id)
        return ExcursionDto(
                    id = excursion.id,
                    name = excursion.name,
                    description = excursion.description,
                    guideId = excursion.guideId,
                    price = excursion.price
                )


    def get_excursions(self):
        excursions = self.excursionRepository.findAll()
        result = []
        for excursion in excursions:
            result.append(ExcursionDto(
                    id = excursion.id,
                    name = excursion.name,
                    description = excursion.description,
                    guideId = excursion.guideId,
                    price = excursion.price
                ))
        return result

    def create_excursion(self, createExcursionDto):
        newExcursion = Excursion(
                    name = createExcursionDto.name,
                    description = createExcursionDto.description,
                    guideId = createExcursionDto.guideId,
                    price = createExcursionDto.price
                )
        try:
            excursion = self.excursionRepository.create(newExcursion)
            return ExcursionDto(
                    id = excursion.id,
                    name = excursion.name,
                    description = excursion.description,
                    guideId = excursion.guideId,
                    price = excursion.price
                )
        except:
            return None

    def update_excursion(self, updateExcursionDto):
        updateExcursion = Excursion(
                    id = updateExcursionDto.id,
                    name = updateExcursionDto.name,
                    description = updateExcursionDto.description,
                    guideId = updateExcursionDto.guideId,
                    price = updateExcursionDto.price
                )
        try:
            excursion = self.excursionRepository.update(updateExcursion)
            return ExcursionDto(
                    id = excursion.id,
                    name = excursion.name,
                    description = excursion.description,
                    guideId = excursion.guideId,
                    price = excursion.price
                )
        except:
            return None

    def delete_excursion(self, id):
        countDelete = self.excursionRepository.delete(id)
        return countDelete