from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        self.name = "splash"
        # Default widget to fill all the space of the splash screen, replace with your own Layout
        self.add_widget(Label(text="Splash Screen"))
