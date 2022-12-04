from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.icon = "favicon.ico"
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}

        self.window.add_widget(Image(source="220608_Logo_Hochformat_DRK-Ortsvereinigung_HochheimamMain_4c.png"))
        self.greeting = Label(text="Dein Name bitte!")
        self.window.add_widget(self.greeting)
        self.user = TextInput(multiline = False)
        self.window.add_widget(self.user)
        self.button = Button(text = "Grüße")
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)

        self.button1 = Button(text = "kommen")
        self.button1.bind(on_press = self.callback)
        self.button1.background_color = "green"
        self.button2 = Button(text = "gehen")
        self.button2.bind(on_press = self.callback)
        self.button2.background_color = "red"

        boxlayout = BoxLayout()
        boxlayout.add_widget(self.button1)
        boxlayout.add_widget(self.button2)
        self.window.add_widget(boxlayout)

        return self.window

    def callback(self, instance):
        self.greeting.text = "Hallo " + self.user.text + "!"


if __name__ == "__main__":
    SayHello().run()