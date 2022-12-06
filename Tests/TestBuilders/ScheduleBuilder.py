from Entities.Schedule import Schedule

class ScheduleBuilder:
    def __init__(self, id, excursionId, day, time):
        self.id = id
        self.excursionId = excursionId
        self.day = day
        self.time = time

    def build(self):
        return Schedule(
            id=self.id,
            excursionId=self.excursionId,
            day=self.day,
            time=self.time
        )
