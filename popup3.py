import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup


class Widgets(Widget):

    text_input = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.popup = PopupApp()

    def show_popup(self):
        if self.ids.text_input.text == 'text':
            self.popup.show_popup()


class P(FloatLayout):
    pass


class PopupApp(App):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        show = P()
        # The below object can be created only once
        self.popupWindow = Popup(
            title="Popup Window", content=show, size_hint=(None, None), size=(400, 400))
        self.widget = None

    def build(self):
        return Widgets()

    def show_popup(self):
        self.popupWindow.open()

    def close_popup(self):
        self.popupWindow.dismiss()


if __name__ == "__main__":
    PopupApp().run()
