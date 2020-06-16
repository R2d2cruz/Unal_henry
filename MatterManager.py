"""
MatterManager:
        Control the process to create and inscribe the students in the subjects for the career

Authors:
        Carlos Arturo Cruz Useche - 1001048369
        Diego Alejandro Campos Méndez - 1005753729
        Karen Fonseca Sánchez - 1020825523
        Henry Salomón Suárez López - 1030595912

"""

from Student import Student
from Matter import Matter
from ReadDataBase import ReadDataBase


class MatterManager:
    def __init__(self):
        self.__reader = ReadDataBase()
        self.__students = {}
        self.__sortedstudents = {}
        self.__matters = {}
        self.createStudents()
        self.createMatters()

    @property
    def students(self):
        return self.__students.keys()

    @property
    def mattersCodes(self):
        return self.__matters.keys()

    @property
    def nameMatters(self) -> list:
        mattersName = []
        for matter in self.__matters.keys():
            mattersName.append(self.__matters.get(matter).name)
        return mattersName

    # aqui va el algoritmo de organizacion de horario
    def orgSchedule(self):
        #for i in arange(5, 3, -0.01):
         #   for student in self.students:
          #      if student.papi == i:
           #         self.__sortedstudents[student] = Student(student, self.__reader.getStudentById(student))
            
        for student in self.students:
            for matter in self.__students.get(student).wishes:
                self.__students.get(student).addMatter(self.__matters.get(matter))
                    
                #else:
                #    return("la materia no tiene cupos suficientes")

    def studentById(self, _id: str) -> Student:
        return self.__students.get(_id)

    # retorna la id de un estudiante
    def studentByName(self, name: str) -> list:
        students = []
        for studentKey in self.__students.keys():
            student = self.__students.get(studentKey)
            studentName = student.name
            if studentName == name:
                students.append(student)
        return students

    # crea un nuevo estudiante
    def createStudent(self, name: str, _id: str, value: int = 0, wishes: list = [], matters: list = [], schedule: dict = {}):
        data = {
            "schedule": schedule,
            "name": name,
            "matters": matters,
            "wishes": wishes,
            "credits": value
        }
        self.__students[_id] = Student(_id, data)

    # crea el diccionario de estudiantes con los codigos como llaves
    def createStudents(self):
        for student in self.__reader.students:
            self.__students[student] = Student(student, self.__reader.getStudentById(student))

    # crea el diccionario de materias con los codigos como llaves
    def createMatters(self):
        for matter in self.__reader.matters:
            self.__matters[matter] = Matter(matter, self.__reader.getMatterById(matter))

    # crea una nueva materia
    def createMatter(self, name: str, _id: str, value: int, owl: str, maxStu: int, days: dict = {}):
        data = {
            'days': days,
            'numStudents': 0,
            'maxStudents': maxStu,
            'name': name,
            'owl': owl,
            'value': value
        }
        self.__matters[_id] = Matter(_id, data)
        self.__reader.saveNewMatter(_id, data)

    # guarda los cambios de un estudiante
    def saveIndividualStudentById(self, student: str):
        self.__reader.updateStudentBuId(student, self.__students.get(student).data)

    # guarda el nuevo numero de estudiantes inscritos en una materia
    def saveMatterNumStudents(self, matter: str):
        self.__reader.updateMatterNumStudentsById(matter, self.__matters.get(matter).numStudents)

    # guarda todos los cambios
    def saveAll(self):
        for student in self.__students.keys():
            self.__reader.updateStudentBuId(student, self.__students.get(student).data)
        for matter in self.__matters.keys():
            self.__reader.updateMatterNumStudentsById(matter, self.__matters.get(matter).numStudents)
        self.__reader.packing()
