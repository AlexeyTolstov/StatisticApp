from kivy.app import App
from kivy.core.window import Window

from pages import *


Window.size = (360, 640)
Window.clearcolor = (.7, .5, .9, 1)


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn = Button(text="hello",
                     font_size="50sp")
        self.main_layout = FloatLayout()
        self.main_layout.add_widget(btn)

    def build(self):
        return self.main_layout


if __name__ == "__main__":
    MyApp().run()