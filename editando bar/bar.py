from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.utils import platform
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import ListProperty,StringProperty, ObjectProperty
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.label import Label
import os.path
import time

PATH = '.'
if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA,Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
    app_folder = os.path.dirname(os.path.abspath(__file__))
    PATH = "/sdcard/DCIM/teste"

class Gerenciador(ScreenManager):
    pass 
class Menu(Screen):
    def confirmacao(self,*args):
        box = BoxLayout(orientation='vertical',padding = 10 ,spacing = 10)
        botoes = BoxLayout(padding = 10 ,spacing = 10)

        pop = Popup(title='Deseja mesmo sair?',content=box,size_hint=(None,None),
                    size=(150,150))

        sim =Botao(text="Sim",on_release=MDApp.get_running_app().stop)
        nao =Botao(text="Não",on_release=pop.dismiss)

        botoes.add_widget(sim)   #inserido o botao
        botoes.add_widget(nao)

        atencao = Image(source='nx.png')

        box.add_widget(atencao)
        box.add_widget(botoes)

        #pop = Popup(title='Deseja mesmo sair ',content=box)
        animText = Animation(color=(0,0,0,1)) + Animation(color=(1,1,1,1))
        animText.repeat = True
        animText.start(sim)
        animText.start(nao)
        anim = Animation(size=(300,180), duration = 0.2, t = 'out_back')
        anim.start(pop)
        pop.open()
        return True

class CameraClick(Screen):    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
      
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids.camera
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("{}/IMG_{}.png".format(PATH,timestr))
        print("{}/IMG_{}.png".format(PATH,timestr))

    def select_camera(self, facing):
        self.parent.ids.preview.select_camera(facing)

class Botao(ButtonBehavior,Label):
    cor = ListProperty([0.1,0.5,0.7,1])
    cor2 = ListProperty([0.1,0.1,0.1,1])

    def __init__(self,**kwargs):
        super(Botao,self).__init__(**kwargs)
        self.atualizar()

    def on_pos(self,*args):
        self.atualizar()

    def on_size(self,*args):
        self.atualizar()

    def on_press(self,*args):
        self.cor, self.cor2 = self.cor2, self.cor

    def on_release(self,*args):  #Propriedades e atribuição simultânea
        self.cor, self.cor2 = self.cor2, self.cor

    def on_cor(self,*args):
        self.atualizar()

    def atualizar(self,*args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.cor)
            Ellipse(size=(self.height,self.height),
                    pos=self.pos)
            Ellipse(size=(self.height,self.height),
                    pos=(self.x+self.width-self.height,self.y))
            Rectangle(size=(self.width-self.height,self.height),
                        pos=(self.x+self.height/2.0,self.y))   

class Main(MDApp):
    def build(self):
        self.theme_cls.Theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Gerenciador()
Main().run()