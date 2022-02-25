import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
# Replace this with your
# current version
kivy.require('1.11.1')
import sys
#sys.path.insert(0, "")
from services.CloudService import CloudService
import  kivy.uix.button
# Defining a class
class MyFirstKivyApp(App):

    # Function that returns
    # the root widget
    global cloudservice
    cloudservice =CloudService()
    def addFace(self,event):
        cloudservice.addFace()
    def build(self):

        # Label with text Hello World is
        # returned as root widget

         btn1 = Button(text='Register Student',font_size ="20sp",
                   background_color =(10, 1, 100, 1),
                   color =(1, 1, 100, 1),
                   size =(22, 32),
                   size_hint =(.2, .2),
                   pos =(300, 250))
         btn1.bind(on_press=self.addFace)
         return btn1


# Here our class is initialized
# and its run() method is called.
# This initializes and starts
# our Kivy application.
MyFirstKivyApp().run()
