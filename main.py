from kivy.app import App
from kivy.core.window import Window

from customwidgets import *
from pages import *

Window.size = (360, 640)


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layouts_lst = [WelcomePage(),
                            RegistrationPage(),
                            InterestsPage()]

        self.opened_page_ind = 0
        self.opened_page = self.layouts_lst[self.opened_page_ind]

        self.btn_next = Button(text="Следущая страница",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.1},
                               size_hint=(0.45, 0.1))
        self.btn_next.bind(on_press=self.next_page)

        self.main_layout = FloatLayout()
        self.main_layout.add_widget(self.btn_next)

    def build(self):
        return self.main_layout

    def next_page(self, _):
        self.main_layout.remove_widget(self.opened_page)
        self.opened_page_ind += 1
        self.opened_page = self.layouts_lst[self.opened_page_ind]
        self.main_layout.add_widget(self.opened_page)


if __name__ == "__main__":
    MyApp().run()