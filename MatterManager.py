"""
MatterManager:
        Control the process to create and inscribe the students in the subjects for the career

Authors:
        Carlos Arturo Cruz Useche - 1001048369
        Diego Alejandro Campos Méndez - 1005753729
        Karen Fonseca Sánchez - 1020825523
        Henry Salomón Suárez López - 1030595912

"""
from typing import Optional

from Student import Student
from Matter import Matter
from ReadDataBase import ReadDataBase
from queue import PriorityQueue


class MatterManager:
    def __init__(self):
        self.__reader = ReadDataBase()
        self.__students = {}
        self.__matters = {}
        self.createStudents()
        self.createMatters()

    @property
    def students(self) -> list:
        return list(self.__students.keys())

    @property
    def mattersCodes(self) -> list:
        return list(self.__matters.keys())

    @property
    def nameMatters(self) -> list:
        mattersName = []
        for matter in self.__matters.keys():
            mattersName.append(self.__matters.get(matter).name)
        return mattersName

    # aqui va el algoritmo de organizacion de horario
    def orgSchedule(self):
        # idea
        # obtiene lista de tuplas de papas y código de studiantes ordenadas de mayor a menor
        # orderedStudents = []
        studentsQueue = PriorityQueue()
        for student in self.students:
            studentsQueue.put((self.__students.get(student).priority, student))
        
        while not studentsQueue.empty():
            studentId: str = studentsQueue.get()[1]
            student: Student = self.__students.get(studentId)
            wishes = PriorityQueue()
            for matterId in student.wishes:
                if student.getWishIsInscribe(matterId) != 'y':
                    wishes.put((student.getWishPriority(matterId), matterId))
            while not wishes.empty():
                matterId: str = wishes.get()[1]
                matter: Matter = self.__matters.get(matterId)
                if matter.vacancy() and student.addMatter(matter):
                    matter.addStudent(studentId)
                    print("La materia fue inscrita")
                else:
                    print("La materia no pudo ser inscrita :(")

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

    def matterById(self, _id: str) -> Optional[Matter]:
        if _id in self.__matters and self.__matters.get(_id) is not None:
            return self.__matters.get(_id)
        return None

    # crea un nuevo estudiante
    def createStudent(self, name: str, _id: str, papi: float, house: str, tookSurvey: bool, value: int = 0,
                      wishesMatters=None, matters=None, schedule=None):
        if schedule is None:
            schedule = {}
        if matters is None:
            matters = []
        if wishesMatters is None:
            wishesMatters = {}
        wishes = {}
        for matter in wishesMatters.keys():
            matterName = self.__matters.get(matter).name
            wishes[matter] = {
                'name': matterName,
                'isInscribe': 'p',
                'priority': wishesMatters.get(matter)
            }
        data = {
            'schedule': schedule,
            'name': name,
            'matters': matters,
            'wishes': wishes,
            'credits': value,
            'PAPI': papi,
            'house': house,
            'tookSurvey': tookSurvey
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
    def createMatter(self, name: str, _id: str, value: int, owl: str, maxStu: int, days=None):
        if days is None:
            days = {}
        data = {
            'days': days,
            'numStudents': 0,
            'maxStudents': maxStu,
            'name': name,
            'owl': owl,
            'value': value,
            'students': []
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
