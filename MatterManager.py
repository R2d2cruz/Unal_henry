from Student import Student
from Matter import Matter
from ReadDataBase import ReadDataBase


class MatterManager:
    def __init__(self):
        self.reader = ReadDataBase()
        self.students = {}
        self.matters = {}
        self.createStudents()
        self.createMatters()

    # crea el diccionario de estudiantes con los codigos como llaves
    def createStudents(self):
        for student in self.reader.students:
            self.students[student] = Student(student, self.reader.getStudentById(student))

    # crea el diccionario de materias con los codigos como llaves
    def createMatters(self):
        for matter in self.reader.matters:
            self.matters[matter] = Matter(self.reader.getMatterById(matter))

    def update(self):
        pass

    # guarda los cambios
    def save(self):
        self.reader.packing()
