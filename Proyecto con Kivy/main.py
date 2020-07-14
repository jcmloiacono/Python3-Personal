import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.utils import get_color_from_hex as getColor
from kivy.utils import get_hex_from_color
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen):
    color1 = getColor("ffff00")
    color2 = getColor("b5b500")
    color3 = getColor("898901")
    color4 = getColor("515100")
    pass
#    def btnDarEntrada(self):
#        print("btnDarEntrada")
#    def btnVerInventario(self):
#        print("btnVerInventario")
#    def btnDarBaja(self):
#        print("btnDarBaja")
#    def btnCalcular(self):
#        print("btnCalcular")
class WindowDarEntrada(Screen):
    pass
class WindowVerInventario(Screen):
    pass
class WindowDarSalida(Screen):
    pass
class WindowCalcular(Screen):
    pass
class WindowManager(ScreenManager):
    pass

#kv = Builder.load_file("my.kv")

class MyApp(App): # <- Main Class
    def build(self):
        return Builder.load_file("my.kv")
    '''
        root = WindowManager()
        root.add_widget(MainWindow())
        root.add_widget(WindowDarEntrada())
        root.add_widget(WindowVerInventario())
        root.add_widget(WindowDarSalida())
        root.add_widget(WindowCalcular())
        return root
'''

if __name__ == "__main__":
    MyApp().run()
