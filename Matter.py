class Matter:
    def __init__(self, data: dict):
        self.__days = data.get("days")
        self.name = data.get("name")
        self.__numStudents = data.get("numStudents")
        self.__maxStudents = data.get("maxStudents")

    @property
    def days(self):
        return self.__days.keys()

    def getHoursByDay(self, day: str):
        return self.__days.get(day)

    @property
    def numStudents(self):
        return self.__numStudents

    def addStudent(self):
        if self.__numStudents < self.__maxStudents:
            self.__numStudents += 1
            return True
        return False

    def overCoop(self, overCoops: int = 1):
        self.__maxStudents += overCoops
