#Imports for Kivy and KivyMD
import kivy
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.button import Button
from kivymd.uix.list import OneLineListItem
from kivymd.uix.transition import MDSwapTransition

#Checks downloaded kivy version before trying to run rest of the code
kivy.require("2.2.0")




#Creates the different Screen classes
class home_screen(Screen):
     pass

class account_screen(Screen):
     pass

class settings_screen(Screen):
     pass

class WindowManager(ScreenManager):
     pass






#Manually looks for kivy file
kv = Builder.load_file("D:\VS\Kivy Code\Practice\Project\homescreen.kv")
#Changes window shape
Window.size = (300, 500)
#Sets background color to white
Window.clearcolor = (1, 1, 1, 1)





#Main part of the Program that is ran
#All features called from here
class MainPage(MDApp):
    #Creates the window
    def build(self):
        #Window name + icon
        self.title = "My Medicine Cabinet"
        self.icon = "D:\VS\Kivy Code\Practice\Project\!Project3.png"
        sm = ScreenManager()
        sm.add_widget(home_screen(name='home'))
        sm.add_widget(account_screen(name='account'))
        sm.add_widget(settings_screen(name='settings'))
        return sm

    #Def for the settings menu (coming from account screen)
    def home_menu(self):
         print("works")
         self.root.transition.direction = "right"
         self.root.current = "home"


    #Def for the settings menu (coming from settings screen)
    def home_menu2(self):
         print("works")
         self.root.transition.direction = "down"
         self.root.current = "home"

            
    #Def for the account settings menu
    def accountSettings_menu(self):
        print("works")
        self.root.transition.direction = "left"
        self.root.current = "account"
    

    #Def for pop up stock list
    def popUp_menu(self):
         print("no works")
         self.root.transition.direction = "up"
         self.root.current = "settings"
         




#Runs the program
if __name__ == '__main__':
    MainPage().run()