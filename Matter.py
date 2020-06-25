"""
Matter:
        Create the matter for the career

Authors:
        Carlos Arturo Cruz Useche - 1001048369
        Diego Alejandro Campos Méndez - 1005753729
        Karen Fonseca Sánchez - 1020825523
        Henry Salomón Suárez López - 1030595912
"""


class Matter:
    def __init__(self, _id: str, data: dict):
        self.__days: dict = data.get('days')
        self.__name: str = data.get('name')
        self.__numStudents: int = data.get('numStudents')
        self.__maxStudents: int = data.get('maxStudents')
        self.__id: str = _id
        self.__owl: str = data.get('owl')
        self.__value: float = data.get('value')
        self.students: list = data.get('students')

    @property
    def days(self) -> list:
        return list(self.__days.keys())

    @property
    def Id(self) -> str:
        return self.__id

    @property
    def numStudents(self) -> int:
        return self.__numStudents

    @property
    def name(self) -> str:
        return self.__name

    @property
    def value(self) -> float:
        return self.__value

    # Devuelve la intesidad horaria por dia
    def getHoursByDay(self, day: str) -> list:
        return self.__days.get(day)

    # Añadir estudiante al curso
    def addStudent(self, studentId: str):
        self.__numStudents += 1
        self.students.append(studentId)

    def vacancy(self) -> bool:
        return self.__numStudents < self.__maxStudents

    # añadir sobrecupos a la materia
    def overCoop(self, overCoops: int = 1):
        self.__maxStudents += overCoops
