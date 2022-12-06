from Amebus.Models.Schedule import ScheduleModelDB
from ..Entities.Schedule import Schedule
from ..Logs.log import logger
from ..db_settings import database_proxy, database_connect


class ScheduleRepository:
    def __init__(self, url):
        # Based on configuration, use a different database.
        self.database = database_connect(url)
        # Configure our proxy to use the db we specified in config.
        database_proxy.initialize(self.database)
        self.ScheduleModelDB = ScheduleModelDB


    def findById(self, id):
        try:
            schedule = self.ScheduleModelDB.get(ScheduleModelDB.id == id)
            logger.info("Schedule was received")
            return Schedule(
                id = schedule.id,
                excursionId = schedule.excursionId,
                day = schedule.day,
                time = schedule.time
            )
        except:
            logger.warning("Schedule wasn't received")
            return None

    def findAll(self):
        schedules = self.ScheduleModelDB.select()
        result = []
        for schedule in schedules:
            result.append(Schedule(
                id=schedule.id,
                excursionId=schedule.excursionId,
                day=schedule.day,
                time=schedule.time
            ))
        logger.info("Schedule was received")
        return result

    def create(self, newSchedule):
        try:
            schedule = self.ScheduleModelDB(
                excursionId=newSchedule.excursionId,
                day=newSchedule.day,
                time=newSchedule.time
            )
            schedule.save()
            logger.info("Schedule was created")
            return Schedule(
                id=schedule.id,
                excursionId=schedule.excursionId,
                day=schedule.day,
                time=schedule.time
            )
        except:
            logger.warning("Schedule wasn't created")
            return None

    def findByExcursionId(self, excursionId):
        schedules = self.ScheduleModelDB.select().where(ScheduleModelDB.excursionId == excursionId)
        result = []
        for schedule in schedules:
         schedule.append(Schedule(
             id=schedule.id,
             excursionId=schedule.excursionId,
             day=schedule.day,
             time=schedule.time
         ))
        logger.info("Schedule was received")
        return result

    def update(self, updateSchedule):
        try:
            schedule = self.ScheduleModelDB.get(ScheduleModelDB.id == id)
            schedule.excursionId = updateSchedule.excursionId
            schedule.day = updateSchedule.day
            schedule.time = updateSchedule.time
            schedule.save()
            logger.info("Schedule was updated")
            return Schedule(
                id=schedule.id,
                excursionId=schedule.excursionId,
                day=schedule.day,
                time=schedule.time
            )
        except:
            logger.warning("Schedule wasn't updated")
            return None

    def delete(self, id):
        try:
            schedule = self.ScheduleModelDB.get(ScheduleModelDB.id == id)
            logger.info("Schedule was deleted")
            return schedule.delete_instance()
        except:
            logger.warning("Schedule wasn't deleted")
            return 0