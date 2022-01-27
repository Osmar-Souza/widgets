from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.lang import Builder

class NovosApp(MDApp):
    def build(self):
        self.theme_cls.Theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file('novos.kv')
NovosApp().run()