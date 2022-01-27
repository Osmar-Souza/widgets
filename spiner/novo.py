from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import StringProperty

from kivymd.uix.list import OneLineIconListItem


KV = '''

<IconListItem>

    IconLeftWidget:
        icon: root.icon

MDScreen:
    MDIconButton:                
        icon: "menu"
        id: drop_item
        pos_hint: {'center_x': .5, 'center_y': .5}
        text: 'Select'
        on_release: app.menu.open()
'''

class IconListItem(OneLineIconListItem):
    icon = StringProperty()

class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        d_items = ['item-1',"item-2","item-3"]
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon":'account',
                # "height": dp(40),
                "height": dp(56), # it looks better with 56
                "text": i,
                "on_release": lambda x=i: self.set_item(x),
                # "IconleftWidget": "icon",
            } for i in d_items
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.drop_item,
            items=menu_items,
            position="center",
            width_mult=2.3,
        )
        self.menu.bind()

    def set_item(self, text_item):
        self.screen.ids.drop_item.text=text_item
        self.menu.dismiss()

    def build(self):
        return self.screen


Test().run()