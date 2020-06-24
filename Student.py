from Matter import Matter


"""
Student:
        Create the student data in the program

Authors:
        Carlos Arturo Cruz Useche - 1001048369
        Diego Alejandro Campos Méndez - 1005753729
        Karen Fonseca Sánchez - 1020825523
        Henry Salomón Suárez López - 1030595912


"""

# en wishes, 'p' es en progreso, 'n' es no se pudo inscribir y 'y' es si se pudo inscribir


class Student:
    def __init__(self, _id: str, data: dict):
        self.__schedule = data.get('schedule')
        self.__matters = data.get('matters')
        self.__name = data.get('name')
        self.__id = _id
        self.__wishesMatters = data.get('wishes')
        self.__creditsUsed = data.get('credits')
        self.__papi = data.get('PAPI')
        self.__house = data.get('house')
        self.__tookSurvey = data.get('tookSurvey')

    def __str__(self):
        return 'Id: ' + self.Id + '\nName: ' + self.name + '\nSchedule: ' + self.schedule

    # devuelve el nombre del estudiante
    @property
    def name(self) -> str:
        return self.__name

    # devuelve el id del estudiante
    @property
    def Id(self) -> str:
        return self.__id

    # devuelve las materias que el estudiante desea inscribir
    @property
    def wishes(self) -> list:
        return self.__wishesMatters.keys()

    # devuelve un diccionario con la informacion del estudiante
    @property
    def data(self):
        return {
            'schedule': self.__schedule,
            'name': self.__name,
            'matters': self.__matters,
            'wishes': self.__wishesMatters,
            'credits': self.__creditsUsed,
            'PAPI': self.__papi,
            'house': self.__house,
            'tookSurvey': self.__tookSurvey
        }

    @property
    def schedule(self) -> str:
        schedule = ''
        for day in self.__schedule.keys():
            schedule += day
            for hour in self.__schedule.get(day):
                schedule += '\t' + hour
            schedule += '\n'
        return schedule

    @property
    def priority(self) -> float:
        priority = 5 - self.papi
        if not self.__tookSurvey:
            priority += 0.5
        return priority

    @property
    def papi(self) -> float:
        return self.__papi

    @property
    def house(self):
        return self.__house

    def addMatter(self, matter: Matter) -> bool:
        matterName = matter.name
        daysPass = {}
        for day in matter.days:
            if self.__schedule.get(day) is None:
                self.__schedule[day] = {}
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
                    self.__wishesMatters[matter.Id]['isInscribe'] = 'n'
                    return False
        # devuelve true si pudo inscribir la materia
        self.__matters.append(matterName)
        self.__wishesMatters.get(matter.Id)['isInscribe'] = 'y'
        self.__creditsUsed += matter.value
        return True

    def deleteAllScheduleMatter(self, daysPass: dict):
        for day in daysPass.keys():
            for hour in daysPass.get(day):
                del self.__schedule[day][hour]
                # elimina las apariciones de la materia mencionada
