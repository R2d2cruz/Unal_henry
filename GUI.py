<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


class MainWindow(Screen):
    def on_pre_enter(self):
        Window.size = (393, 700)
    pass


class OptionsWindow(Screen):
    def on_pre_enter(self):
        Window.size = (393, 700)
    pass


class cremat(Screen,grid):
    def on_pre_enter(self):
        Window.size = (393, 700)
    pass


class creest(Screen):
    def on_pre_enter(self):
        Window.size = (393, 700)
    pass


class edimat(Screen):
    def on_pre_enter(self):
        Window.size = (393, 700)
    pass


class ediest(Screen):
    def on_pre_enter(self):
        Window.size = (393, 700)
    pass


class vermat(Screen):
    def on_pre_enter(self):
        Window.size = (393, 700)
    pass


class verest(Screen):
    def on_pre_enter(self):
        Window.size = (393, 700)
    pass


class crearhor(Screen):
    def on_pre_enter(self):
        Window.size = (393, 700)
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("GUI.kv")


class GUI(App):
    title = 'Horario UN'
    def build(self):
        return kv
=======
=======
>>>>>>> Interfaz gráfica
=======
>>>>>>> Interfaz gráfica
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen


<<<<<<< HEAD
<<<<<<< HEAD
# install kivy-deps.glew kivy-deps.sdl2

=======
>>>>>>> Interfaz gráfica
=======
>>>>>>> Interfaz gráfica
class MyGrid(Widget):
    days = ObjectProperty(None)
    name = ObjectProperty(None)
    numbstud = ObjectProperty(None)
    maxstud = ObjectProperty(None)
    mattcode = ObjectProperty(None)
    owl = ObjectProperty(None)
    credits = ObjectProperty(None)
    slack = ObjectProperty(None)

    def ChrgMatter(self):
        print("Días:", self.days.text, "Nombre:", self.name.text, "Número de estudiantes:", self.numbstud.text,"Número máximo de estudiantes:",
              self.maxstud.text,"Código de la materia:", self.mattcode.text,"Profesor:", self.owl.text,"Valor en créditos:", self.credits.text,"Holgura en sobrecupos:", self.slack.text,)

    def NewMatter(self):
        self.days.text = ""
        self.name.text = ""
        self.numbstud.text = ""
        self.maxstud.text = ""
        self.mattcode.text = ""
        self.owl.text = ""
        self.credits.text = ""
        self.slack.text = ""


class GUI(App):
    def build(self):
        return MyGrid()
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> Interfaz gráfica


# if __name__ == "__main__":
#     GUI().run()
=======
=======
>>>>>>> Interfaz gráfica


if __name__ == "__main__":
    GUI().run()
<<<<<<< HEAD
>>>>>>> Interfaz gráfica
=======
>>>>>>> Interfaz gráfica
