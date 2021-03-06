import kivy
from kivy.app import App
from kivy.graphics import Rectangle, Color,Line
from kivy.uix.widget import Widget


class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Line(points=(20,30,400,500,60,500)) 
            Color(1,0,0,0.5,mode='rgba')
            self.rect = Rectangle(pos=(0, 0), size=(50, 50))
    
    def on_touch_down(self, touch):
        self.rect.pos = touch.pos

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos

class TchApp(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    TchApp().run()
