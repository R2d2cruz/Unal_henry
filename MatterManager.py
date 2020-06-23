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
from queue import PriorityQueue


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
        # idea
        #obtiene lista de tuplas de papas y código de studiantes ordenadas de mayor a menor
        #ordererstudents = []
        studentsQueue = PriorityQueue()
        for student in self.students:
            studentsQueue.put((self.__students.get(student).priority, student))
        
        while not studentsQueue.empty():
            studentId = studentsQueue.get()[1]
            student = self.__students.get(studentId)
            for matterId in student.wishes:
                matter = self.__matters.get(matterId)
                if matter.hasSpace() and student.addMatter(matter):
                    matter.addStudent()
                    print("La materia fue inscrita")
                else:
                    print("La materia no pudo ser inscrita :(")
                
            #ordererstudents.append(studentsQueue.get())
        
        #Inscribe materias de acuerdo a los primeros lugares de la lista
        #for i in ordererstudents:
            #self.__students.get(i[1]).addMatter(self.__matters.get(matter))
            #print(studentsQueue[1])
                    
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
    def createStudent(self, name: str, _id: str, papi: float, house: str, value: int = 0,wishesMatters: list = [], matters: list = [], schedule: dict = {}):
        wishes = {}
        for matter in wishesMatters:
            wishes[matter] = {
                'name': self.__matters.get(matter).name,
                'isInscribe': 'P'
            }
        data = {
            'schedule': schedule,
            'name': name,
            'matters': matters,
            'wishes': wishes,
            'credits': value,
            'PAPI': papi,
            'house': house
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
