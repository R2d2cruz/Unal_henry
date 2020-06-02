


class Matter:
    def __init__(self, name: str, days: Dict, maxStudents: int):
        self.__days = days
        self.name = name
        self.__numStudents = 0
        self.__maxStudents = maxStudents


    @property
    def days(self):
        return self.__days.keys()

    def getHoursByDay(self, day: str):
        return self.__days.get(day)

    @property
    def numStudents(self):
        return self.__students

    def addStudent(self):
        if self.__numStudents < self.__maxStudents:
            self.__numStudents += 1
            return True
        return False