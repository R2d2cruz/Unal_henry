from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from MatterManager import MatterManager


class DataManager(object):
    def __init__(self):
        self.matterManager = MatterManager()

    @staticmethod
    def verificationStudentName(name: str) -> bool:
        if not (0 < len(name.split(' ')) < 6):
            return False
        if not name.isalpha():
            return False
        name.lower()
        for word in name.split(' '):
            alterableWord = word
            alterableWord[0].upper()
            name.replace(word, alterableWord)
        return True

    @staticmethod
    def verificationPapi(papi: float) -> bool:
        return papi < 0 or papi > 5

    def createStudent(self, name: str, _id: str, papi: float, house: str, tookSurvey: bool, value: int = 0,
                      wishesMatters=None, matters=None, schedule=None) -> bool:
        if schedule is None:
            schedule = {}
        if matters is None:
            matters = []
        if wishesMatters is None:
            wishesMatters = {}
        nameOk = self.verificationStudentName(name)
        papiOk = self.verificationPapi(papi)
        if nameOk and papiOk:
            self.matterManager.createStudent(name, _id, papi, house, tookSurvey, value, wishesMatters=wishesMatters,
                                             matters=matters, schedule=schedule)
            return True
        return False

    def createMatter(self, name: str, _id: str, value: int, owl: str, maxStu: int, days=None) -> bool:
        if days is None:
            days = {}
        return False


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
    numbstud = ObjectProperty(None)
    maxstud = ObjectProperty(None)
    mattcode = ObjectProperty(None)
    owl = ObjectProperty(None)
    credits = ObjectProperty(None)

    def ChrgMatter(self):
        print("Días:", self.days.text, "Nombre:", self.namematt.text, "Número de estudiantes:", self.numbstud.text,
              "Número máximo de estudiantes:",
              self.maxstud.text, "Código de la materia:", self.mattcode.text, "Profesor:", self.owl.text,
              "Valor en créditos:", self.credits.text)

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
    tookSurvey: ObjectProperty(None)

    def ChrgStud(self):
        print("Días:", self.schedule.text, "Nombre:", self.nameStudents.text, "Número de estudiantes:",
              self.idStudents.text,
              "Número máximo de estudiantes:",
              self.wishesMatters.text, "Código de la materia:", self.creditsUsed.text, "Profesor:", self.matters.text,
              "Valor en créditos:", self.papi.text, "Valor en créditos:", self.college.text, "Valor en créditos:",
              self.tookSurvey.text)

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
