from random import *
from MatterManager import MatterManager


class Generator:

    firstName = ['Arnold', 'Harrison', 'Sara', 'Daniel', 'Aaron']
    secondName = ['Connor', 'Craig', 'Ford', 'Schwarzenegger', 'MacLaud']
    thirdName = ['Fox', 'Doblas', 'Croos', 'Junior']

    mattersNames = ['Ecuaciones Diferenciales', 'Electromagnetismo', 'Mediciones Electromagneticas', 'Probabilidad',
                    'Metodos numericos', 'Calculo Integral']

    validDays = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
    validHours = []

    def __init__(self):
        self.validNames: dict = self.createNames()
        for i in range(7, 23):
            self.validHours.append(str(i) + ':00')
        self.matterManager = MatterManager()

    def run(self):
        self.createMatters(5)
        self.createStudents(13)

    def createNames(self) -> dict:
        names = {}
        for name in self.firstName:
            for secondName in self.secondName:
                for thirdName in self.thirdName:
                    entireName = name + ' ' + secondName + ' ' + thirdName if thirdName != '' else name + ' ' + secondName
                    names[entireName] = False
        return names

    def createMatters(self, nextId: int):
        for matter in self.mattersNames:
            _id = nextId
            nextId += 1
            value = randint(2, 6)
            hours = value
            schedule = self.createEmptySchedule()
            owl = self.choiceRandomPerson()
            self.assignHours(schedule, hours)
            maxStu = randint(15, 40)
            self.matterManager.createMatter(matter, str(_id), value, owl, maxStu, schedule)

    def createStudents(self, nextId: int):
        while self.getNumberNotUsesNames() > 0:
            studentName = self.choiceRandomPerson()
            studentId = self.getIdStr(nextId)
            papi = (randint(10, 50)) / 10
            house = '007'
            tookSurvey = choice([True, True, False])
            insanity = randint(12, 21)
            wishes = {}
            while insanity > 1:
                while True:
                    matterCode = choice(self.matterManager.mattersCodes)
                    if matterCode not in wishes.keys():
                        pass

    def createEmptySchedule(self) -> dict:
        schedule = {}
        for day in self.validDays:
            schedule[day] = []
        return schedule

    def assignHours(self, schedule: dict, hours: int):
        while 0 < hours:
            day = choice(self.validDays)
            hour = choice(self.validHours)
            if hour not in schedule.get(day):
                schedule[day].append(hour)
            hours -= 1

    def choiceRandomPerson(self) -> str:
        for name in self.validNames.keys():
            if not self.validNames.get(name):
                self.validNames[name] = True
                return name

    def getNumberNotUsesNames(self) -> int:
        i = 0
        for name in self.validNames.keys():
            if not self.validNames.get(name):
                i += 1
        return i

    @staticmethod
    def getIdStr(_id: int) -> str:
        strId = str(_id)
        newId = ((len(strId) - 4) * '0') + strId
        return newId
