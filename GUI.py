from kivy.config import Config
Config.set('kivy', 'window_icon', 'icon.ico')
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '450')
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from connection import SocketServer


class FirstScreen(Screen):
    def on_click(self, app):
        app.root.ids.second.username = self.ids.namein.text
        app.root.current = "second"
        app.root.ids.second.conn = SocketServer(app.root.ids.second, self.ids.namein.text, ("YourServerIPHere", 5050), 8192)
        app.root.ids.second.conn.start()


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username = ""
        self.conn = None

    def on_click(self):
        self.conn.send(self.ids.entry.text)
        self.ids.entry.text = ""


class Manager(ScreenManager):
    pass


class PreventOverload(TextInput):
    max_char = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.focus = True

    def insert_text(self, substring, from_undo=False):
        new = self.text + substring
        if len(new) <= self.max_char and new != "":
            self.text = new


class PreventOverloadAndEnter(PreventOverload):
    func = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_shift_pressed = False
        self.focus = True

    def on_enter(self):
        self.func()

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if self.focus and keycode[0] == 13 and not self.is_shift_pressed:
            self.on_enter()
            self.is_shift_pressed = False
        elif self.focus and keycode[0] == 304:
            self.is_shift_pressed = True
        elif self.focus and keycode[0] == 13 and self.is_shift_pressed:
            super().keyboard_on_key_down(window, keycode, text, modifiers)
            self.is_shift_pressed = False
        else:
            super().keyboard_on_key_down(window, keycode, text, modifiers)
            self.is_shift_pressed = False


class OnOverload(Popup):
    def on_click(self):
        self.close()


class GUI(App):
    def build(self):
        self.title = r"Msg App"
        return Manager()


if __name__ == '__main__':
    GUI().run()
