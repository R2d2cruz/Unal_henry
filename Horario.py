#n_estudiantes = 50
#materias = {"materia1":35,"materia2":30, ...}
#n_materias = len(materias)

class estudiante:
    def __init__(self):
        self.horario = {6:"", 7:"", 8:"", 9:"", 10:"", 11:"", 12:"", 13:"", 14:"", 15:"", 16:"", 17:"", 18:"", 19:"", 20:"", 21:""}

    def agregar_materia(self, materia, inicio, final):
        for i in range(inicio, final):
            self.horario[i] = materia