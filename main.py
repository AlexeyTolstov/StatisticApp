from kivy.app import App
from pages import *

Window.size = (360, 640)
# Window.size = (540, 960)


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layouts_lst = [
                            # WelcomePage(),
                            # AboutAlexPage(),
                            # AboutElPage(),
                            # AcquaintPage(),
                            CityPage(),
                            GenderPage(),
                            ClassPage(),
                            InterestsPage(),
                            RestPage(),
                            SectionPage(),
                            AboutPage(),
                            TelephonePage(),
                            CompletionPage()]

        self.opened_page_ind = 0
        self.opened_page = self.layouts_lst[self.opened_page_ind]

        try:
            self.opened_page.btn_next.bind(on_press=self.next_page)
        except AttributeError:
            pass

        try:
            self.opened_page.btn_back.bind(on_press=self.back_page)
        except AttributeError:
            pass

        self.main_layout = FloatLayout()
        self.main_layout.add_widget(self.opened_page)

    def build(self):
        return self.main_layout

    def back_page(self, _):
        self.main_layout.remove_widget(self.opened_page)
        self.opened_page_ind = (self.opened_page_ind - 1)
        self.opened_page = self.layouts_lst[self.opened_page_ind]
        self.main_layout.add_widget(self.opened_page)

        try:
            self.opened_page.btn_next.bind(on_press=self.next_page)
        except AttributeError:
            pass

        try:
            self.opened_page.btn_back.bind(on_press=self.back_page)
        except AttributeError:
            pass

    def next_page(self, _):
        try:
            res = self.opened_page.is_can_next()
        except AttributeError:
            res = True

        try:
            self.opened_page.get_data()
        except AttributeError:
            pass

        if res:
            self.main_layout.remove_widget(self.opened_page)
            self.opened_page_ind = (self.opened_page_ind + 1)
            self.opened_page = self.layouts_lst[self.opened_page_ind]

            try:
                self.opened_page.update()
            except AttributeError:
                pass

            self.main_layout.add_widget(self.opened_page)

            try:
                self.opened_page.btn_next.bind(on_press=self.next_page)
            except AttributeError:
                pass

            try:
                self.opened_page.btn_back.bind(on_press=self.back_page)
            except AttributeError:
                pass


if __name__ == "__main__":
    MyApp().run()