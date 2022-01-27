from kivy.lang import Builder
from kivymd.app import MDApp

class NavigationApp(MDApp):
    def build(self):
        self.theme_cls.Theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file('navigation.kv')
NavigationApp().run()