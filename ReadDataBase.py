"""
ReadDataBase:
        read and write the information

Authors:
        Carlos Arturo Cruz Useche - 1001048369
        Diego Alejandro Campos Méndez - 1005753729
        Karen Fonseca Sánchez - 1020825523


"""
# anotense ahi ☝️


import json


class ReadDataBase:
    def __init__(self, directory: str = 'dataBase/', students: str = 'students.json', matters: str = 'matters.json'):
        self.__directory = directory
        self.__studentsFileLoc = self.__directory + students
        self.__mattersFileLoc = self.__directory + matters
        with open(self.__studentsFileLoc, 'r') as studentsFile:
            self.__studentsData = json.load(studentsFile)
            studentsFile.close()
        with open(self.__mattersFileLoc, 'r') as mattersFile:
            self.__mattersData = json.load(mattersFile)
            mattersFile.close()

    # devuelve la lista de id´s de los estudiantes
    @property
    def students(self):
        return self.__studentsData.keys()

    # devuelve el listado de codigos de las materias
    @property
    def matters(self):
        return self.__mattersData.keys()

    # guarda una nueva materia
    def saveNewMatter(self, _id: str, data: dict):
        self.__mattersData[_id] = data

    # devuelve el dicionario de un estuiante por su id
    def getStudentById(self, _id: str):
        return self.__studentsData.get(_id)

    # devuelve el dicionario de una materia por su codigo(id)
    def getMatterById(self, _id: str):
        return self.__mattersData.get(_id)

    # actualiza a un estudiante por su id
    def updateStudentBuId(self, _id: str, data: dict):
        self.__studentsData[_id] = data

    # actualiza el numero de estudiantes en una clase por su id
    def updateMatterNumStudentsById(self, _id: str, numStudents: int):
        self.__mattersData[_id]['numStudents'] = numStudents

    # actualiza el numero de cupos
    def updateMatterMaxStudentsById(self, _id: str, maxStudents: int):
        self.__mattersData[_id]['maxStudents'] = maxStudents

    def packing(self):
        with open(self.__studentsFileLoc, 'w') as studentFile:
            json.dump(self.__studentsData, studentFile, indent=4)
            studentFile.close()
        with open(self.__mattersFileLoc, 'w') as mattersFile:
            json.dump(self.__mattersData, mattersFile, indent=4)
            mattersFile.close()
