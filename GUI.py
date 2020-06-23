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


if __name__ == "__main__":
    GUI().run()
