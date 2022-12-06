from Amebus.Entities.Excursion import Excursion

class ExcursionMotherBuilder:
    def init(self, id, name, guideId, price):
        self.excursionBuilder = ExcursionBuilder(id, name, guideId, price)

    def createExcursionArt(self):
        return self.excursionBuilder.withDescription("Art excursion").build()

    def createExcursionHistorical(self):
        return self.excursionBuilder.withDescription("Historical excursion").build()


class ExcursionBuilder:
    def __init__(self, id, name, guideId, price):
        self.id = id
        self.name = name
        self.guideId = guideId
        self.price = price
        self.description = ""

    def withDescription(self, new_description):
        self.description = new_description
        return self

    def build(self):
        return Excursion(
            id = self.id,
            name = self.name,
            guideId = self.guideId,
            price = self.price,
            description = self.description
        )