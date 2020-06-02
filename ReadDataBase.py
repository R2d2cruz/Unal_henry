import json


class ReadDataBase:
    def __init__(self, directory: str = "dataBase/", students: str = "students.json", matters: str = "matters.json"):
        self.__directory = directory
        self.__studentsFileLoc = self.__directory + students
        self.__mattersFileLoc = self.__directory + matters
        with open(self.__studentsFileLoc, "r") as studentsFile:
            self.__studentsData = json.load(studentsFile)
        with open(self.__mattersFileLoc, "r") as mattersFile:
            self.__mattersData = json.load(mattersFile)

    # devuelve la lista de id´s de los estudiantes
    @property
    def students(self):
        return self.__studentsData.keys()

    # devuelve el listado de codigos de las materias
    @property
    def matters(self):
        return self.__mattersData.keys()

    # devuelve el dicionario de un estuiante por su id
    def getStudentById(self, _id: str):
        return self.__studentsData.get(_id)

    # actualiza a un estudiante por su id
    def updateStudentBuId(self, _id: str, data: dict):
        self.__studentsData[_id] = data

    # actualiza el numero de estudiantes en una clase por su id
    def updateMatterNumStudentsById(self, _id: int, numStudents: int):
        self.__mattersData[_id]["numStudents"] = numStudents

    # actualiza el numero de cupos
    def updateMatterMaxStudentsById(self, _id: int, maxStudents: int):
        self.__mattersData[_id]["maxStudents"] = maxStudents
