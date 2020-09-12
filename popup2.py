import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup


class Widgets(Widget):
    text_input = ObjectProperty(None)
    def btn(self):
        if self.ids.text_input.text == 'text':
            PopupApp.show_popup()


class P(FloatLayout):
    def close_popup(cls):
        PopupApp.close_popup()


class PopupApp(App):
    popupWindow = None

    def build(self):
        return Widgets()

    @classmethod
    def show_popup(cls):
        show = P()

        if cls.popupWindow is None:
            cls.popupWindow = Popup(title="Popup Window", content=show,
                                    size_hint=(None, None), size=(400, 400))
        cls.popupWindow.open()

    @classmethod
    def close_popup(cls):
        cls.popupWindow.dismiss()


if __name__ == "__main__":
    PopupApp().run()

