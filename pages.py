from customwidgets import *


class WelcomePage(FloatLayout):
    def __init__(self):
        super().__init__()
        self.number_page = 0

        self.welcome_label = Label(text="Добрый день",
                                      pos_hint={'center_x': 0.5, 'center_y': 0.9},
                                      size_hint=(0.1, 0.05),
                                      font_size=30)
        self.add_widget(self.welcome_label)


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

        self.add_widget(self.gender_layout)
        self.add_widget(self.gender_label)

        self.add_widget(self.age_input)
        self.add_widget(self.age_label)

        self.add_widget(self.telephone_input)
        self.add_widget(self.telephone_label)
        self.add_widget(self.title_label)

    def get_data(self):
        if self.gender_layout.man_checkbox.active:
            print("Мужской пол")
        else:
            print("Женский пол")

        print(self.age_input.text)
        print(self.telephone_input.text)

        print("Следущая страница")


class InterestsPage(FloatLayout):
    def __init__(self):
        super().__init__()

        self.interesting = MultiplyChoiceCheckBox(["1", "2", "3"])