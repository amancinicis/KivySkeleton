from kivy.uix.screenmanager import Screen

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        self.name = "splash"
