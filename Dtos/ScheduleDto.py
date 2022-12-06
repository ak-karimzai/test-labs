class ScheduleDto:
    def __init__(self, id, excursionId, day, time):
        self.id = id
        self.excursionId = excursionId
        self.day = day
        self.time = time

class CreateScheduleDto:
    def __init__(self, excursionId, day, time):
        self.excursionId = excursionId
        self.day = day
        self.time = time