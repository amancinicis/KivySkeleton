from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager


class MainLayout(BoxLayout):
    """
    Holds the main application layout
    """
    def __init__(self, **kwargs):
        self.orientation = "horizontal"
        super(MainLayout, self).__init__(**kwargs)
        self.navigation = NavigationLayout()
        self.add_widget(self.navigation)
        self.sm = ScreenManager()
        self.add_widget(self.sm)
        self.sm.add_widget(CounterScreen())
        self.sm.add_widget(SettingsScreen())
        self.buttons = []
        self.buttons.append(Button(text="Settings"))
        self.buttons[-1].bind(on_release=self.to_settings)
        self.navigation.add_widget(self.buttons[-1])
        self.buttons.append(Button(text="Counters"))
        self.buttons[-1].bind(on_release=self.to_counters)
        self.navigation.add_widget(self.buttons[-1])
        self.buttons.append(Button(text="Quit"))
        self.buttons[-1].bind(on_release=self.quit_app)
        self.navigation.add_widget(self.buttons[-1])

    def to_settings(self, *args):
        """
        Navigation to the settings screen
        :param args:
        :return:
        """
        self.sm.current = 'settings'

    def to_counters(self, *args):
        """
        Navigation to the counters screen
        :param args:
        :return:
        """
        self.sm.current = 'counters'

    def quit_app(self, *args):
        """
        Quits the whole app
        :param args:
        :return:
        """
        App.get_running_app().stop()


class NavigationLayout(BoxLayout):
    """
    Navigation between screens
    """
    def __init__(self, **kwargs):
        self.orientation = "vertical"
        self.size_hint_x = 0.3
        super(NavigationLayout, self).__init__(**kwargs)
        self.label = Label(text="Navigation")
        self.add_widget(self.label)


class MainApp(App):
    def build(self):
        root = MainLayout()
        return root


MainApp().run()
