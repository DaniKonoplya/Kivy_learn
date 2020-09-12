import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    first_name = ObjectProperty(None)
    last_name = ObjectProperty(None)

    def btn(self):
        print("Name:", self.first_name.text, 'Last Name:', self.last_name.text)
        self.first_name.text = ""
        self.last_name.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()
