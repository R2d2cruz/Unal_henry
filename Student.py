from Matter import Matter

#n_estudiantes = 50
#materias = {"materia1":35,"materia2":30, ...}
#n_materias = len(materias)

# days = {"lunes": "hour"}


class Student:
    def __init__(self, _id: str, data: dict):
        self.schedule = data.get("schedule")
        self.matters = data.get("matters")
        self.__name = data.get("name")
        self.__id = _id

    @property
    def name(self):
        return self.name

    @property
    def Id(self):
        return self.__id

    def addMatter(self, matter: Matter):
        matterName = matter.name
        daysPass = {}
        for day in matter.days:
            for hour in matter.getHoursByDay(day):
                # se revisa cada hora de cada dia que tiene la materia
                if self.schedule.get(day).get(hour) is None:
                    # si no hay materias ahi, añada la materia
                    self.schedule[day][hour] = matterName
                    # en caso de que por alguna razon no se pueda guarda los dias y horas que ha guardado esa materia
                    daysPass[day] = hour
                else:
                    # si la materia tiene conflicto entonces eliminar todos las horas donde esta
                    self.deleteAllScheduleMatter(daysPass)
                    return False
        # devuelve true si pudo inscribir la materia
        self.matters.append(matterName)
        return True

    def deleteAllScheduleMatter(self, daysPass: dict):
        for day in daysPass.keys():
            for hour in daysPass.get(day):
                del self.schedule[day][hour]
                # elimina las apariciones de la materia mencionada
