from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

from pages import *

Window.size = (360, 640)


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layouts_lst = [WelcomePage(),
                            RegistrationPage(),
                            InterestsPage(),
                            FavoriteSectionPage(),
                            RestPage()]

        self.opened_page_ind = 0
        self.opened_page = self.layouts_lst[self.opened_page_ind]

        self.btn_next = Button(text="Следущая страница",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.1},
                               size_hint=(0.5, 0.1))
        self.btn_next.bind(on_press=self.next_page)

        self.main_layout = FloatLayout()
        self.main_layout.add_widget(self.btn_next)

    def build(self):
        return self.main_layout

    def next_page(self, _):
        try:
            res = self.opened_page.is_can_next()
        except AttributeError:
            res = True

        if self.opened_page_ind == 0:
            self.layouts_lst = [WelcomePage(),
                                RegistrationPage(),
                                InterestsPage(),
                                FavoriteSectionPage(),
                                RestPage()]
        elif self.opened_page_ind == 3:
            self.btn_next.text = "Завершить"
        elif self.opened_page_ind == 4:
            self.btn_next.text = "Перейти на главную страницу"
        else:
            self.btn_next.text = "Следущая страница"

        if res:
            if self.opened_page_ind == 4:
                self.layouts_lst.append(ResultPage())

            self.main_layout.remove_widget(self.opened_page)
            self.opened_page_ind = (self.opened_page_ind + 1) % len(self.layouts_lst)
            self.opened_page = self.layouts_lst[self.opened_page_ind]
            self.main_layout.add_widget(self.opened_page)


if __name__ == "__main__":
    MyApp().run()
