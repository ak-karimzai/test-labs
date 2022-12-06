from peewee import SqliteDatabase
import logging.config

from Dtos.GuideDto import CreateGuideDto
from Logs.log_config import log_config
from Controllers.ExcursionController import ExcursionController
from Controllers.GuideController import GuideController
from Controllers.ScheduleController import ScheduleController
from Dtos.ScheduleDto import ScheduleDto
from Models.Excursion import ExcursionModelDB
from Models.Guide import GuideModelDB
from Models.Schedule import ScheduleModelDB
from db_settings import database_proxy

class ConsoleApp:
    def __init__(self, url='amebud.db'):
        self.excursionController = ExcursionController(url)
        self.guideController = GuideController(url)
        self.scheduleController = ScheduleController(url)

    @staticmethod
    def menu():
        print("Консольное приложение:")
        print(" 1) Добавить гида")
        print(" 2) Найти гида")
        print(" 3) Найти всех гидов")
        #print(" 4) Обновить гида")
        #print(" 5) Удалить гида")
        print(" 7) Найти экскурсию'")
        print(" 8) Найти все экскурсии")
        #print(" 9) Добавить экскурсию")
        #print(" 10) Обновить экскурсию")
        #print(" 11) Удалить экскурсию")
        #print(" 12) Найти расписание")
        #print(" 13) Найти все расписания")
        #print(" 14) Добавить расписание")
        #print(" 15) Обновить расписание")
        #print(" 16) Удалить расписание")
        #print(" 17) Вывести все расписание экскурсии")
        print(" 0) Выйти")

    @staticmethod
    def print_excursion(excursion):
        print()
        print(f"id: {excursion.id}")
        print(f"name: {excursion.name}")
        print(f"description: {excursion.description}")
        print(f"guideId: {excursion.guideId}")
        print(f"price: {excursion.price}")

    @staticmethod
    def print_guide(guide):
        print()
        print(f"id: {guide.id}")
        print(f"firstName: {guide.firstName}")
        print(f"lastName: {guide.lastName}")
        print(f"patronymic: {guide.patronymic}")
        print(f"qualification: {guide.qualification}")
        print(f"biography: {guide.biography}")
        print(f"experience: {guide.experience}")

    @staticmethod
    def print_schedule(schedule):
        print()
        print(f"id: {schedule.id}")
        print(f"excursionId: {schedule.excursionId}")
        print(f"day: {schedule.day}")
        print(f"time: {schedule.time}")

    def get_guide(self):
        id = int(input("Введите id: "))
        self.print_guide(self.guideController.get_guide(id))

    def get_guides(self):
        try:
            guides = self.guideController.get_guides()
            for guide in guides:
                self.print_guide(guide)
        except:
            print("Ошибка")

    def get_excursion(self):
        id = int(input("Введите id: "))
        try:
            self.print_excursion(self.excursionController.get_excursion(id))
        except:
            print("Ошибка")

    def get_excursions(self):
        excursions = self.excursionController.get_excursions()
        for excursion in excursions:
            self.print_excursion(excursion)

    def add_guide(self):
        firstName = input("Введите имя: ")
        lastName = input("Введите фамилию: ")
        patronymic = input("Введите отчество: ")
        qualification = input("Ваша квалификация: ")
        biography = input("Введите вашу биографию: ")
        experience = input("Количество лет стажа: ")
        try:
            guide = self.guideController.create_guide(CreateGuideDto(
                firstName = firstName,
                lastName = lastName,
                patronymic = patronymic,
                qualification = qualification,
                biography = biography,
                experience = experience
            ))
            self.print_guide(guide)
        except:
            print("Ошибка")


    def run(self):
        while True:
            self.menu()
            choice = input("Выберите действие: ")
            if choice.isdigit() and 0 <= int(choice) <= 17:
                if int(choice) == 1:
                    self.add_guide()
                elif int(choice) == 2:
                    self.get_guide()
                elif int(choice) == 3:
                    self.get_guides()
                elif int(choice) == 7:
                    self.get_excursion()
                elif int(choice) == 8:
                    self.get_excursions()
                elif int(choice) == 0:
                    break
            else:
                print("Некорректный ввод.")


def start():
    console = ConsoleApp()
    console.run()

def creation():
    # Based on configuration, use a different database.
    database = SqliteDatabase('amebus.db')
    # Configure our proxy to use the db we specified in config.
    database_proxy.initialize(database)
    database.drop_tables([ExcursionModelDB, GuideModelDB, ScheduleModelDB])
    database.create_tables([ExcursionModelDB, GuideModelDB, ScheduleModelDB])


if __name__ == '__main__':
    creation()
    start()