from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


import drkconfig
import drklib
import time
import network
import drksql
import mariadb

# Konfiguration einlesen oder neu generieren
###############################################################################
config = drkconfig.set_std_config()
if drkconfig.check_config(drklib.get_gu_id()):
    config = drkconfig.get_config(drklib.get_gu_id())
    drkconfig.write_config(drklib.get_gu_id(), config)
else:
    drkconfig.write_config(drklib.get_gu_id(), config)
    #gui_close()


class Zeiterfassung(App):
    def build(self):
        self.icon = "favicon.ico"

        self.window = GridLayout()
        self.window.cols = 1

#        self.window.size_hint = (1, 1)
#        self.window.pos_hint = {"center_x":0.1, "center_y":0.1}

        self.window.add_widget(Image(source=config['allgemein']['logo_fil']))
        self.greeting = Label(text="Dein Name bitte!")
        self.window.add_widget(self.greeting)
        self.user = TextInput(multiline = False)
        self.window.add_widget(self.user)

        self.button_kommen = Button(text = config['texte']['ko'])
        self.button_kommen.bind(on_press = self.callback)
        self.button_kommen.background_color = config['farben']['ko']
        self.button_kommen.background_normal = ""
        self.button_gehen = Button(text = config['texte']['ge'])
        self.button_gehen.bind(on_press = self.callback)
        self.button_gehen.background_color = config['farben']['ge']
        self.button_gehen.background_normal = ""

        boxlayout = BoxLayout()
        boxlayout.add_widget(self.button_kommen)
        boxlayout.add_widget(self.button_gehen)
        self.window.add_widget(boxlayout)

        return self.window

    def callback(self, instance):
        self.greeting.text = "Hallo " + self.user.text + "!"


if __name__ == "__main__":
    Zeiterfassung().run()