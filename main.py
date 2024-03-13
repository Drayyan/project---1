from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp

class interface(FloatLayout):
    def display_information (self):
        data= self.ids.textInput.text
        self.ids.label.text = data

class FirstApp(App):
   pass

FirstApp().run()