"""
Matter:
        Create the matter for the career

Authors:
        Carlos Arturo Cruz Useche - 1001048369

"""
# anotense ahi ☝️


class Matter:
    def __init__(self, _id: str, data: dict):
        self.__days = data.get('days')
        self.__name = data.get('name')
        self.__numStudents = data.get('numStudents')
        self.__maxStudents = data.get('maxStudents')
        self.__id = _id
        self.__owl = data.get('owl')

    @property
    def days(self):
        return self.__days.keys()

    @property
    def Id(self):
        return self.__id

    @property
    def numStudents(self):
        return self.__numStudents

    @property
    def name(self):
        return self.__name

    def getHoursByDay(self, day: str):
        return self.__days.get(day)

    def addStudent(self):
        if self.__numStudents < self.__maxStudents:
            self.__numStudents += 1
            return True
        return False

    def overCoop(self, overCoops: int = 1):
        self.__maxStudents += overCoops
