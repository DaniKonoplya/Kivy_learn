import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2  # set number of columns for the grid

        elems = ['First Name:', 'Last Name:', 'Email:']
        # The elements are added to the grid in order as we add them.
        for el in elems:
            self.add_widget(Label(text=el))
            _ = el.replace(' ', '_').replace(':', '').lower()
            self.__setattr__(_, TextInput(multiline=False))
            self.add_widget(self.__getattribute__(_))

        self.submit = Button(text="Submit", font_size=40)
        self.add_widget(self.submit)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
