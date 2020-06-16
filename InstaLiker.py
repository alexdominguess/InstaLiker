import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window 
Window.size = (450, 425)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import time
import sys
from easygui import multpasswordbox
from functions import open_chrome, login, like_posts


class LoginScreen(BoxLayout):
    def insta_login(self):
        email = self.email_field.text
        pwd = self.pwd_field.text
        #check if info were provided
        if email == '': 
            self.popup_message("Erro!", "Digite seu email")
        elif len(pwd) < 6:
            self.popup_message("Erro!", "Password não pode ser menor que 6 digitos")
        else:
            driver = open_chrome('https://www.instagram.com/')
            logar = login(driver, email, pwd)
            if logar[0] == 'fail':
                self.popup_message("Erro!",logar[1])
            else:

                action = like_posts(driver, 300)
                self.popup_message("Insta Liker", action)


    def popup_message(self, msg_type, message):
        popup = Popup(title= msg_type,
            content=Label(text= message),
            size_hint=(None, None), size=(350, 200))
        popup.open()

    def close(self):
        Instaliker().stop()



class Instaliker(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    Instaliker().run()