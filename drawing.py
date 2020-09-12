import kivy
from kivy.app import App
from kivy.graphics import Rectangle, Color
from kivy.uix.widget import Widget


class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(1,0,0,0.5,mode='rgba')
            self.rect = Rectangle(pos=(0, 0), size=(50, 50))
            Color(1,1,0,0.5,mode='rgba')
            self.rect2 = Rectangle(pos=(200, 300), size=(100, 50))


class TchApp(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    TchApp().run()
