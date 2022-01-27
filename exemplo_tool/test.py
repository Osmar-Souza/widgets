from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
KV = """
MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "MDToolbar"

    FloatLayout:
        MDIconButton:
            icon: "record-circle"
            md_bg_color: app.theme_cls.primary_color
            #user_font_size: "64sp"
            pos_hint: {"center_x": 0.8, "center_y": .5}
            
        MDIconButton:
            icon: "pencil"
            md_bg_color: app.theme_cls.primary_color
            #user_font_size: "32sp"
            pos_hint: {"center_x": 0.8, "center_y": .7}

        MDIconButton:
            icon: "content-save"
            md_bg_color: app.theme_cls.primary_color
            #user_font_size: "32sp"
            pos_hint: {"center_x": 0.8, "y": .8}
            
        MDIconButton:
            icon: "home"
            md_bg_color: app.theme_cls.primary_color
            #user_font_size: "64sp"
            pos_hint: {"center_x": 0.3, "center_y": .5}
            
        MDIconButton:
            icon: "menu"
            md_bg_color: app.theme_cls.primary_color
            #user_font_size: "32sp"
            pos_hint: {"center_x": 0.3, "center_y": .7}

        MDIconButton:
            icon: "dots-vertical"
            md_bg_color: app.theme_cls.primary_color
            #user_font_size: "32sp"
            pos_hint: {"center_x": 0.3, "y": .8}
            
        MDIconButton:
            icon: "home"
            md_bg_color: app.theme_cls.primary_color
            #user_font_size: "64sp"
            pos_hint: {"center_x": 0.5, "center_y": .2}
            
        MDIconButton:
            icon: "menu"
            md_bg_color: app.theme_cls.primary_color
            #user_font_size: "32sp"
            pos_hint: {"center_x": 0.6, "center_y": .2}

        MDIconButton:
            icon: "dots-vertical"
            md_bg_color: app.theme_cls.primary_color
            #user_font_size: "32sp"
            pos_hint: {"center_x": 0.7, "y": .2}
"""
class MDBoxLayout(FloatLayout):
    pass

class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()