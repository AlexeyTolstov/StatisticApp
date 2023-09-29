from customwidgets import *
from kivy.uix.floatlayout import FloatLayout


data_dict = {}


class WelcomePage(FloatLayout):
    def __init__(self):
        super().__init__()

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
                                 font_size=30,
                                 halign="center")

        self.gender_label = Label(text="Выберите пол:",
                                  pos_hint={'center_x': 0.5,
                                            'center_y': 0.75},
                                  halign="center")

        self.gender_layout = GenderLayout(
            pos_hint={'center_x': 0.5, 'center_y': 0.7})

        self.gender_not_label = Label(pos_hint={'center_x': 0.5,
                                            'center_y': 0.65},
                                  halign="center",
                                color=[1, 0, 0, 1])

        self.age_label = Label(text="Выберите возраст:",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.57},
                               halign="center")

        self.age_not_label = Label(pos_hint={'center_x': 0.5,
                                            'center_y': 0.45},
                                  halign="center",
                                color=[1, 0, 0, 1])

        self.age_input = NumberInput(type_input="age",
                                     font_size=30,
                                     size_hint=(.1, .06),
                                     pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.age_input.bind(text=self.age_input.press_keyboard)

        self.telephone_label = Label(text="Укажите телефон:",
                                     pos_hint={'center_x': 0.5,
                                               'center_y': 0.4},
                                     halign="center")
        self.telephone_input = NumberInput(type_input="phone",
                                           font_size=30,
                                           size_hint=(.6, .07),
                                           pos_hint={'center_x': 0.5, 'center_y': 0.32})

        self.telephone_input.bind(text=self.telephone_input.press_keyboard)

        self.add_widget(self.gender_layout)
        self.add_widget(self.gender_label)
        self.add_widget(self.gender_not_label)

        self.add_widget(self.age_input)
        self.add_widget(self.age_label)
        self.add_widget(self.age_not_label)

        self.add_widget(self.telephone_input)
        self.add_widget(self.telephone_label)
        self.add_widget(self.title_label)

    def is_can_next(self):
        gender = self.gender_layout.check_data()
        age = self.age_input.check_data()
        if not gender:
            self.gender_not_label.text = "Вы не указали пол"
        else:
            self.gender_not_label.text = ""

        if not age:
            self.age_not_label.text = "Вы не указали возраст"
        else:
            self.age_not_label.text = ""

        if gender and age:
            self.get_data()
        
        return gender and age

    def get_data(self):
        global data_dict

        if self.gender_layout.man_checkbox.active:
            data_dict["gender"] = "Мужской пол"
        else:
            data_dict["gender"] = "Женский пол"

        data_dict["age"] = self.age_input.text
        data_dict["phone"] = self.telephone_input.text


class InterestsPage(FloatLayout):
    def __init__(self):
        super().__init__()

        self.choices_lst = ["русский язык", "литература", "родная литература",
                            "математика", "история", "иностранный язык",
                            "физика", "химия", "биология",
                            "обществознание", "география", "физкультура",
                            "информатика", "ОБЖ", "Астрономия", "Вероятность и статистика",
                            "ОДНКНР", "Черчение", "Технология",
                            "Музыка", "Основы экономики", "Основы финансовой грамотности",
                            "МХК", "краеведение"]

        self.interesting_label = Label(text="Список предпочитаемых предметов",
                                       size_hint=(.1, .1),
                                       pos_hint={'center_x': 0.5, 'center_y': 0.95},
                                       halign="center")

        self.interesting = MultiplyChoiceCheckBox(choices=self.choices_lst,
                        size_hint=(.75, .7),
                        pos_hint={'center_x': 0.4, 'center_y': 0.57})

        self.interesting_label_not = Label(size_hint=(.1, .2),
                                           pos_hint={'center_x': 0.5, 'center_y': 0.18},
                                           color=[1, 0, 0, 1],
                                           halign="center")

        self.add_widget(self.interesting)
        self.add_widget(self.interesting_label)
        self.add_widget(self.interesting_label_not)

    def is_can_next(self):
        global data_dict
        interesting = self.interesting.check_data()
        interest_lst = self.interesting.get_data()

        data_dict["interests"] = interest_lst

        if not interesting:
            self.interesting_label_not.text = "Выберите больше 0 и меньше 3"
        else:
            self.interesting_label_not.text = ""

        return interesting


class FavoriteSectionPage(FloatLayout):
    def __init__(self):
        super().__init__()

        self.favorite_section_label = Label(text="Список предпочитаемого творчества",
                                       size_hint=(.1, .5),
                                       pos_hint={'center_x': 0.5, 'center_y': 0.6},
                                       halign="center")

        self.favorite_section = MultiplyChoiceCheckBox(["Музыкалка", "Художка"],
                        size_hint=(.4, .1),
                        pos_hint={'center_x': 0.5, 'center_y': 0.53})

        self.favorite_section_label_not = Label(size_hint=(.1, .2),
                                           pos_hint={'center_x': 0.5, 'center_y': 0.45},
                                           color=[1, 0, 0, 1],
                                           halign="center")

        self.add_widget(self.favorite_section)
        self.add_widget(self.favorite_section_label)
        self.add_widget(self.favorite_section_label_not)

    def is_can_next(self):
        global data_dict
        favorite = self.favorite_section.check_data()
        favorite_section = self.favorite_section.get_data()

        data_dict["favorite_sections"] = favorite_section

        if not favorite:
            self.favorite_section_label_not.text = "Выберите больше 0 и меньше 3"
        else:
            self.favorite_section_label_not.text = ""

        return favorite


class RestPage(FloatLayout):
    def __init__(self):
        super().__init__()
        self.rest_label = Label(text="Список предпочитаемого отдыха",
                                size_hint=(.1, .5),
                                pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                halign="center")

        self.rest = MultiplyChoiceCheckBox(["Активный", "Пассивный"],
                        size_hint=(.4, .1),
                        pos_hint={'center_x': 0.5, 'center_y': 0.33})

        self.rest_label_not = Label(size_hint=(.1, .2),
                                    pos_hint={'center_x': 0.5, 'center_y': 0.25},
                                    color=[1, 0, 0, 1],
                                    halign="center")

        self.add_widget(self.rest)
        self.add_widget(self.rest_label)
        self.add_widget(self.rest_label_not)

    def is_can_next(self):
        global data_dict
        data_dict["rests"] = self.rest.get_data()

        rest = self.rest.check_data()

        if not rest:
            self.rest_label_not.text = "Выберите больше 0 и меньше 3"
        else:
            self.rest_label_not.text = ""

        return rest


class ResultPage(FloatLayout):
    def __init__(self):
        global data_dict
        super().__init__()

        self.welcome_label = Label(text="Опрос пройден.\n Вот результат:",
                                   pos_hint={'center_x': 0.5, 'center_y': 0.9},
                                   size_hint=(0.1, 0.05),
                                   font_size=30)

        self.info_text = Label(text=f"Пол: {data_dict['gender']}\nВозраст: {data_dict['age']}\nТелефон: {data_dict['phone']}\n" +
                               f"Интересы: {data_dict['interests']}\n Любимые секции: {data_dict['favorite_sections']}\nОтдых: {data_dict['rests']}")
        self.add_widget(self.welcome_label)
        self.add_widget(self.info_text)