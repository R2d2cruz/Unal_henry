from Matter import Matter

#n_estudiantes = 50
#materias = {"materia1":35,"materia2":30, ...}
#n_materias = len(materias)

# days = {"lunes": "hour"}

class Student:
    def __init__(self):
        self.schedule = {}

    def addMatter(self, matter: Matter):
        matterName = matter.name
        for day in matter.days:
            for hour in matter.getHoursByDay(day):
                if self.schedule.get(day).get(hour) is None:
                    self.schedule[day][hour] = matterName
                else:
                    return False

        return True
