from Matter import Matter


"""
Student:
        Create the student data in the program

Authors:
        Carlos Arturo Cruz Useche - 1001048369
        Diego Alejandro Campos Méndez - 1005753729


"""
# anotense ahi ☝️


# en wishes, 'p' es en progreso, 'n' es no se pudo inscribir y 'y' es si se pudo inscribir


class Student:
    def __init__(self, _id: str, data: dict):
        self.__schedule = data.get('schedule')
        self.__matters = data.get('matters')
        self.__name = data.get('name')
        self.__id = _id
        self.__wishesMatters = data.get('wishes')
        self.__creditsUsed = data.get('credits')

    # devuelve el nombre del estudiante
    @property
    def name(self):
        return self.__name

    # devuelve el id del estudiante
    @property
    def Id(self):
        return self.__id

    # devuelve las materias que el estudiante desea inscribir
    @property
    def wishes(self):
        return self.__wishesMatters.keys()

    # devuelve un diccionario con la informacion del estudiante
    @property
    def data(self):
        return {
            'schedule': self.__schedule,
            'name': self.__name,
            'matters': self.__matters,
            'wishes': self.__wishesMatters,
            'credits': self.__creditsUsed
        }

    def addMatter(self, matter: Matter):
        matterName = matter.name
        daysPass = {}
        for day in matter.days:
            for hour in matter.getHoursByDay(day):
                # se revisa cada hora de cada dia que tiene la materia
                if self.__schedule.get(day).get(hour) is None:
                    # si no hay materias ahi, añada la materia
                    self.__schedule[day][hour] = matterName
                    # en caso de que por alguna razon no se pueda guarda los dias y horas que ha guardado esa materia
                    daysPass[day] = hour
                else:
                    # si la materia tiene conflicto entonces eliminar todos las horas donde esta
                    self.deleteAllScheduleMatter(daysPass)
                    self.__wishesMatters[matter.Id]['isInscribe'] = 'y'
                    return False
        # devuelve true si pudo inscribir la materia
        self.__matters.append(matterName)
        self.__wishesMatters[matter.Id]['isInscribe'] = 'y'
        self.__creditsUsed += matter.value
        return True

    def deleteAllScheduleMatter(self, daysPass: dict):
        for day in daysPass.keys():
            for hour in daysPass.get(day):
                del self.__schedule[day][hour]
                # elimina las apariciones de la materia mencionada
