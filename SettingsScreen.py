from kivy.config import ConfigParser
from kivy.uix.screenmanager import Screen
from kivy.uix.settings import Settings


class SettingsScreen(Screen):
    def __init__(self, root, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.name = "settings"
        self.root = root
        self.add_widget(AppSettings(self.root))


class AppSettings(Settings):
    def __init__(self, root, **kwargs):
        super(AppSettings, self).__init__(**kwargs)
        self.root = root
        self.config = ConfigParser()
        self.config.read('defaultconfig.ini')
        self.add_json_panel('Settings', self.config, 'settings.json')

    def on_close(self, *args):
        self.root.to_splash()
