from typing import Optional
from kivy.uix.checkbox import CheckBox
from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, DictProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from MatterManager import MatterManager

ValidDays: list = list()
ValidHours: list = list()


class DataManager(object):
    def __init__(self):
        self.matterManager = MatterManager()

    @staticmethod
    def verificationName(name: str, mini: int = 0, maxi: int = 6) -> Optional[str]:
        if name is None:
            return None
        if not (mini < len(name.split(' ')) < maxi):
            return None
        if name.isalpha():
            return None
        name.lower()
        for word in name.split(' '):
            if word != ' ':
                alterableWord = word
                alterableWord[0].upper()
                name.replace(word, alterableWord)
            else:
                break
        return name

    @staticmethod
    def verificationPapi(papi: float) -> bool:
        return 0 <= papi <= 5

    @staticmethod
    def verificationId(_id: str) -> bool:
        if _id is str:
            try:
                m = int(_id)
            except Exception:
                return False
        return True

    @staticmethod
    def verificationSchedule(days: dict) -> bool:
        for day in days.keys():
            if day not in ValidDays:
                return False
            for hour in days.get(day).keys():
                if hour not in ValidHours:
                    return False
        return True

    def verificationMatters(self, matters: list) -> bool:
        for matterId in matters:
            if not self.verificationId(matterId):
                return False
        return True

    def createStudent(self, name: str, _id: str, papi: float, house: str, tookSurvey: bool = False, value: int = 0,
                      wishesMatters=None, matters: str = None, schedule=None) -> bool:
        if schedule is None:
            schedule = {}
            scheduleOk = True
        else:
            scheduleOk = self.verificationSchedule(schedule)
        if matters is None or len(matters) == 0:
            mattersList = []
            mattersOk = True
        else:
            mattersList = matters.splitlines()
            mattersOk = self.verificationMatters(mattersList)
        if wishesMatters is None or len(wishesMatters) == 0:
            wishesMattersList = {}
            wishesOk = True
        else:
            wishesMattersList = wishesMatters.splitLines()
            wishesOk = self.verificationMatters(wishesMattersList)
        name = self.verificationName(name)
        nameOk = name is not None
        papiOk = self.verificationPapi(papi)
        idOk = self.verificationId(_id)
        if nameOk and papiOk and mattersOk and wishesOk and idOk and scheduleOk:
            self.matterManager.createStudent(name, _id, papi, house, tookSurvey, value, wishesMatters=wishesMattersList,
                                             matters=mattersList, schedule=schedule)
            return True
        return False

    def createMatter(self, name: str, _id: str, value: int, owl: str, maxStu: int, days=None) -> bool:
        if days is None:
            days = {}
            daysOk = True
        else:
            daysOk = self.verificationSchedule(days)
        name = self.verificationName(name, mini=-1)
        nameOk = name is not None
        owl = self.verificationName(owl)
        owlOk = owl is not None
        idOk = self.verificationId(_id)
        if nameOk and owlOk and idOk and daysOk:
            dataManager.matterManager.createMatter(name, _id, value, owl, maxStu, days=days)
            return True
        return False

    def save(self):
        self.matterManager.saveAll()


# noinspection PyTypeChecker
dataManager: DataManager = None


class MainWindow(Screen):
    def on_pre_enter(self):
        Window.size = (393, 700)


class OptionsWindow(Screen):

    def on_pre_enter(self):
        Window.size = (393, 700)


class cremat(Screen):
    days = ObjectProperty(None)
    namematt = ObjectProperty(None)
    maxstud = ObjectProperty(None)
    mattcode = ObjectProperty(None)
    owl = ObjectProperty(None)
    credits = ObjectProperty(None)

    def ChrgMatter(self):
        print("Días:", self.days.text, "Nombre:", self.namematt.text, "Número máximo de estudiantes:",
              self.maxstud.text, "Código de la materia:", self.mattcode.text, "Profesor:", self.owl.text,
              "Valor en créditos:", self.credits.text)
        if dataManager.createMatter(self.namematt.text, self.mattcode.text, int(self.credits.text),
                                    self.owl.text, int(self.maxstud.text)):
            dataManager.save()

    def on_pre_enter(self):
        Window.size = (393, 700)


class cremathor(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.horario = {'lunes': [], 'martes': [], 'miercoles': [], 'jueves': [], 'viernes': []}

    def presshor(self, day, hour):
        if hour not in self.horario.get(day):
            self.horario[day].append(hour)
        else:
            self.horario[day].remove(hour)
        print(self.horario)

    def on_pre_enter(self):
        Window.size = (393, 700)


class creest(Screen):
    schedule: ObjectProperty(None)
    nameStudents: ObjectProperty(None)
    idStudents: ObjectProperty(None)
    wishesMatters: ObjectProperty(None)
    creditsUsed: ObjectProperty(None)
    matters: ObjectProperty(None)
    papi: ObjectProperty(None)
    college: ObjectProperty(None)
    tookSurvey = BooleanProperty(False)

    def tooksurvey(self, *args):
        if args[1]:
            self.tookSurvey = True
        else:
            self.tookSurvey = False

    def ChrgStud(self):
        print("Horario:", self.schedule.text, "Nombre:", self.nameStudents.text, "Codigo del estudiante:",
              self.idStudents.text,
              "Materias deseadas:", self.wishesMatters.text, "Creditos usados:", self.creditsUsed.text,
              "Materias:",
              self.matters.text, "PAPI:", self.papi.text, "Facultad:", self.college.text,
              "Realiza la encuesta:",
              self.tookSurvey)
        if dataManager.createStudent(self.nameStudents.text, self.idStudents.text, float(self.papi.text),
                                     self.college.text, self.tookSurvey):
            dataManager.save()

    def on_pre_enter(self):
        Window.size = (393, 700)


class edimat(Screen):
    def on_pre_enter(self):
        Window.size = (393, 700)


class ediest(Screen):
    def on_pre_enter(self):
        Window.size = (393, 700)


class vermat(Screen):
    def on_pre_enter(self):
        Window.size = (393, 700)


class verest(Screen):
    def on_pre_enter(self):
        Window.size = (393, 700)


class crearhor(Screen):
    def on_pre_enter(self):
        Window.size = (393, 700)


class WindowManager(ScreenManager):
    pass


class Constructor:
    def __init__(self):
        self.kv = Builder.load_file("GUI.kv")
        self.gui = GUI(self.kv)
        global dataManager
        dataManager = DataManager()
        global ValidDays
        ValidDays = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
        global ValidHours
        for i in range(7, 23):
            ValidHours.append(str(i) + ':00')

    def run(self):
        self.gui.run()


class GUI(App):
    title = 'Horario UN'

    def __init__(self, kv, **kwargs):
        super().__init__(**kwargs)
        self.kv = kv

    def build(self):
        return self.kv

# if __name__ == "__main__":
#     GUI().run()
