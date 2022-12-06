class ExcursionDto:
    def __init__(self, id, name, description, guideId, price):
        self.id = id
        self.name = name
        self.description = description
        self.guideId = guideId
        self.price = price


class CreateExcursionDto:
    def __init__(self, name, description, guideId, price):
        self.name = name
        self.description = description
        self.guideId = guideId
        self.price = price