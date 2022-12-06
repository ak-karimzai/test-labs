from Amebus.Services.ScheduleService import ScheduleService
from Amebus.Logs.log import logger

class ScheduleController:
    def __init__(self, url):
        self.scheduleService = ScheduleService(url)

    def get_schedule(self, id):
        try:
            logger.info("Schedule was received")
            return self.scheduleService.get_schedule(id)
        except:
            logger.warning("Schedule wasn't got")
            return None

    def get_schedules(self):
        try:
            logger.info("Schedules was received")
            return self.scheduleService.get_schedules()
        except:
            logger.warning("Schedules wasn't got")
            return None

    def create_schedule(self, createScheduleDto):
        try:
            logger.info("Schedules was created")
            return self.scheduleService.create_schedule(createScheduleDto)
        except:
            logger.warning("Schedules wasn't created")
            return None

    def update_schedule(self, updateScheduleDto):
        try:
            logger.info("Schedules was updated")
            return self.scheduleService.update_schedule(updateScheduleDto)
        except:
            logger.warning("Schedules wasn't updated")
            return None

    def get_schedules_by_excursion_id(self, excursionId):
        try:
            logger.info("Schedules was received")
            return self.scheduleService.get_schedules_by_excursionId(excursionId)
        except:
            logger.warning("Schedules wasn't received")
            return None

    def delete_schedule(self, id):
        try:
            logger.info("Schedules was deleted")
            return self.scheduleService.delete_schedule(id)
        except:
            logger.warning("Schedules wasn't deleted")
            return None