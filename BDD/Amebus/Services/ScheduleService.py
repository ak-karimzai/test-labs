from Amebus.Dtos.ScheduleDto import ScheduleDto
from Amebus.Entities.Schedule import Schedule
from Amebus.Repositories.ExcursionRepository import ExcursionRepository
from Amebus.Repositories.ScheduleRepository import ScheduleRepository
from Amebus.Logs.log import logger

class ScheduleService:
    def __init__(self, url):
        self.scheduleRepository = ScheduleRepository(url)
        self.excursionRepository = ExcursionRepository(url)

    def get_schedule(self, id):
        try:
            schedule = self.scheduleRepository.findById(id)
            logger.info("Schedule was received")
            return ScheduleDto(
                id=schedule.id,
                excursionId=schedule.excursionId,
                day=schedule.day,
                time=schedule.time
            )
        except:
            logger.warning("Schedule wasn't received")
            return None

    def get_schedules(self):
        try:
            schedules = self.scheduleRepository.findAll()
            result = []
            for schedule in schedules:
                result.append(ScheduleDto(
                    id=schedule.id,
                    excursionId=schedule.excursionId,
                    day=schedule.day,
                    time=schedule.time
                ))
            logger.info("Schedule was received")
            return result
        except:
            logger.warning("Schedule wasn't received")
            return None

    def create_schedule(self, createScheduleDto):
        newSchedule = Schedule(
            excursionId=createScheduleDto.excursionId,
            day=createScheduleDto.day,
            time=createScheduleDto.time
        )
        try:
            schedule = self.scheduleRepository.create(newSchedule)
            logger.info("Schedule was created")
            return ScheduleDto(
                id=schedule.id,
                excursionId=schedule.excursionId,
                day=schedule.day,
                time=schedule.time
            )
        except:
            logger.warning("Schedule wasn't created")
            return None

    def update_schedule(self, updateScheduleDto):
        updateSchedule = Schedule(
            id=updateScheduleDto.id,
            excursionId=updateScheduleDto.excursionId,
            day=updateScheduleDto.day,
            time=updateScheduleDto.time
        )
        try:
            schedule = self.scheduleRepository.update(updateSchedule)
            logger.info("Schedule was updated")
            return ScheduleDto(
                id=schedule.id,
                excursionId=schedule.excursionId,
                day=schedule.day,
                time=schedule.time
            )
        except:
            logger.warning("Schedule wasn't updated")
            return None

    def get_schedules_by_excursionId(self, excursionId):
        schedules = self.scheduleRepository.findByExcursionId(excursionId)
        result = []
        for schedule in schedules:
            result.append(ScheduleDto(
                id=schedule.id,
                excursionId=schedule.excursionId,
                day=schedule.day,
                time=schedule.time
            ))
        logger.info("Schedule was received")
        return result

    def delete_schedule(self, id):
        try:
            countDelete = self.scheduleRepository.delete(id)
            logger.info("Schedule was deleted")
            return countDelete
        except:
            logger.warning("Schedule wasn't deleted")
            return None