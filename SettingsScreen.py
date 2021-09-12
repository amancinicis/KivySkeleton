from kivy.config import ConfigParser
from kivy.uix.screenmanager import Screen
from kivy.uix.settings import Settings

# Refer to https://kivy.org/doc/stable/api-kivy.uix.settings.html for more information


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
        self.add_kivy_panel()
        # Sample config file
        self.config.read('defaultconfig.ini')
        #Adds this sample config file
        self.add_json_panel('Custom Settings', self.config, 'settings.json')


    def on_close(self, *args):
        self.root.to_splash()
