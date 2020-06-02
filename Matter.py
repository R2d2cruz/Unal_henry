


class Matter:
    def __init__(self, name: str, days: Dict):
        self.__days = days
        self.name = name


    @property
    def days(self):
        return self.__days.keys()

    def getHoursByDay(self, day: str):
        return self.__days.get(day)