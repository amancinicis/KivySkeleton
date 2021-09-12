from kivy.config import ConfigParser
from kivy.uix.screenmanager import Screen
from kivy.uix.settings import Settings


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.name = "settings"
        self.add_widget(AppSettings())


class AppSettings(Settings):
    def __init__(self, **kwargs):
        super(AppSettings, self).__init__(**kwargs)
