import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1  # set number of columns for the grid

        self.inside = GridLayout()
        self.inside.cols = 2

        elems = ['First Name:', 'Last Name:', 'Email:']
        # The elements are added to the grid in order as we add them.
        self.text_inputs = []
        self.labels = []

        for el in elems:
            l = Label(text=el)
            _ = el.replace(' ', '_').replace(':', '').lower()
            self.__setattr__(_, TextInput(multiline=False))
            self.__setattr__(_ + '_label',l)
            self.inside.add_widget(l)
            self.inside.add_widget(self.__getattribute__(_))
            self.text_inputs.append(self.__getattribute__(_))
            self.labels.append(l)

        # Add the interior layout to the main layout
        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.first_name_label.text
        last = self.last_name_label.text
        email = self.email_label.text

        print("Name:", name, 'Last Name:', last, 'Email:', email)

        for _ in self.labels:
            _.text = ''


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
