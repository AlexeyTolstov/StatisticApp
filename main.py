from kivy.app import App

from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout


class GenderLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.height = 70
        self.width = 250
        self.size_hint_y = None
        self.size_hint_x = None

        self.man_checkbox = CheckBox(group="gender")
        self.man_checkbox.label = Label(text="Мужской")
        self.add_widget(self.man_checkbox)
        self.add_widget(self.man_checkbox.label)
        self.man_checkbox.bind(active=self.on_radiobutton)

        self.woman_checkbox = CheckBox(group="gender")
        self.woman_checkbox.label = Label(text="Женский")
        self.add_widget(self.woman_checkbox)
        self.add_widget(self.woman_checkbox.label)
        self.woman_checkbox.bind(active=self.on_radiobutton)

    @staticmethod
    def on_radiobutton(instance, value):
        # if value:
        #     print(instance.label.text)
        pass


class NumberInput(TextInput):
    def __init__(self, type_input, **kwargs):
        super().__init__(**kwargs)
        self.multiline = False
        self.type_input = type_input

    def press_keyboard(self, instance, value):
        if self.type_input == "age":
            if value:
                if not value.isdigit():
                    self.text = value[:-1]
                elif int(value) > 99:
                    self.text = value[:2]
        elif self.type_input == "phone":
            pass
        print(value)


class WelcomePage(FloatLayout):
    def __init__(self):
        super().__init__()
        self.number_page = 0

        self.welcome_label = Label(text="Добрый день",
                                      pos_hint={'center_x': 0.5, 'center_y': 0.9},
                                      size_hint=(0.1, 0.05),
                                      font_size=30)
        self.add_widget(self.welcome_label)

        self.next_button = Button(text="Начать опрос",
                                      pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                      size_hint=(0.25, 0.1),
                                      font_size=30)
        self.add_widget(self.next_button)


class RegistrationPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title_label = Label(text="Остановись, мама!",
                                 pos_hint={'center_x': 0.5, 'center_y': 0.9},
                                 size_hint=(0.1, 0.05),
                                 font_size=30)

        self.gender_label = Label(text="Выберите пол:",
                                  pos_hint={'center_x': 0.4,
                                            'center_y': 0.75})
        self.gender_layout = GenderLayout(
            pos_hint={'center_x': 0.5, 'center_y': 0.7})

        self.age_label = Label(text="Выберите возраст:",
                               pos_hint={'center_x': 0.4,
                                         'center_y': 0.57})
        self.age_input = NumberInput(type_input="age",
                                     font_size=30,
                                     size_hint=(.05, .07),
                                     pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.age_input.bind(text=self.age_input.press_keyboard)

        self.telephone_label = Label(text="Укажите телефон:",
                                     pos_hint={'center_x': 0.4,
                                               'center_y': 0.4})
        self.telephone_input = NumberInput(type_input="phone",
                                           text='+7 XXX XXX XX-XX',
                                           font_size=30,
                                           size_hint=(.3, .07),
                                           pos_hint={'center_x': 0.5, 'center_y': 0.32})
        self.telephone_input.bind(text=self.telephone_input.press_keyboard)

        self.next_button = Button(text="Далее",
                                  pos_hint={'center_x': 0.5, 'center_y': 0.2},
                                  size_hint=(0.1, 0.05))

        self.add_widget(self.gender_layout)
        self.add_widget(self.gender_label)

        self.add_widget(self.age_input)
        self.add_widget(self.age_label)

        self.add_widget(self.telephone_input)
        self.add_widget(self.telephone_label)

        self.add_widget(self.next_button)
        self.add_widget(self.title_label)

    def get_data(self):
        if self.gender_layout.man_checkbox.active:
            print("Мужской пол")
        else:
            print("Женский пол")

        print(self.age_input.text)
        print(self.telephone_input.text)

        print("Следущая страница")
        MyApp.layout = RegistrationPage()


# class


opened_page = 0
opened_layout = WelcomePage()


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layouts_lst = [WelcomePage(), RegistrationPage()]
        self.opened_page_ind = 0
        self.opened_page = self.layouts_lst[self.opened_page_ind]
        # self.btn_next = Button(text="Следущая страница",
        #                        pos_hint={'center_x': 0.5, 'center_y': 0.1})
        # self.btn_next.bind(on_press=self.next_page)

        self.main_layout = FloatLayout()

    def build(self):
        self.main_layout.add_widget(self.opened_page)
        self.opened_page.next_button.bind(on_press=self.next_page)
        # self.main_layout.add_widget(self.opened_page.next_button)
        return self.main_layout

    def next_page(self, instance):
        self.main_layout.remove_widget(self.opened_page)
        self.opened_page_ind += 1
        self.opened_page = self.layouts_lst[self.opened_page_ind]
        self.main_layout.add_widget(self.opened_page)


if __name__ == "__main__":
    MyApp().run()