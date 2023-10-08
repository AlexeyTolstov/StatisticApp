from customwidgets import *
from kivy.uix.floatlayout import FloatLayout

from config import *


class WelcomePage(FloatLayout):
    def __init__(self):
        super().__init__()
        self.title_label = Label(text="Добрый день",
                                      pos_hint={'center_x': 0.5,
                                                'center_y': 0.9},
                                      size_hint=(0.1, 0.05),
                                      bold=True,
                                      halign="center")

        self.text_label = Label(text="Пройдите наш опрос по \nвнеурочной деятельности\n[Текст такого содержания]",
                                      pos_hint={'center_x': 0.5,
                                                'center_y': 0.6},
                                      size_hint=(0.5, 0.4))

        self.btn_next = Button(text="Начать",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.1},
                               size_hint=(0.9, 0.1),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.title_label.scale = 1
        self.text_label.scale = 0.15
        self.btn_next.scale = 0.1

        self.btn_next.bind(size=self.update_font_size)
        self.text_label.bind(size=self.update_font_size)
        self.title_label.bind(size=self.update_font_size)

        self.add_widget(self.title_label)
        self.add_widget(self.text_label)
        self.add_widget(self.btn_next)

    @staticmethod
    def is_can_next():
        return True

    @staticmethod
    def update_font_size(instance, value):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size


class RegistrationPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.gender_label = Label(text="Выберите пол:",
                                  pos_hint={'center_x': 0.5,
                                            'center_y': 0.9},
                                  halign="center",
                                  bold=True,
                                  font_size=25)

        self.gender_layout = GenderLayout(pos_hint={'center_x': 0.45, 'center_y': 0.82},
                                          size_hint=(.8, .1))

        self.gender_not_label = Label(pos_hint={'center_x': 0.5,
                                                'center_y': 0.7},
                                        halign="center",
                                        color=[1, 0, 0, 1],
                                        bold=True,
                                        font_size=20)

        self.dropdown_class = DropDownClasses()
        self.btn_class = Button(text="Выбрать\nкласс",
                                pos_hint={'center_x': 0.5,
                                          'center_y': 0.55},
                                size_hint=(.3, .15),
                                halign="center",
                                background_color=(1, .4, .4, 1),
                                background_normal="",
                                bold=True)

        self.btn_class.bind(on_release=self.dropdown_class.open)
        self.dropdown_class.bind(on_select=lambda instance, x: setattr(self.btn_class, "text", x))

        self.class_not_label = Label(pos_hint={'center_x': 0.5,
                                            'center_y': 0.44},
                                halign="center",
                                color=[1, 0, 0, 1],
                                bold=True,
                                font_size=20)

        self.btn_next = Button(text="Следущая страница",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.1},
                               size_hint=(0.9, 0.1),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.btn_class.scale = 0.2
        self.btn_next.scale = 0.07
        self.gender_label.scale = 0.07
        self.class_not_label.scale = 0.05
        self.gender_not_label.scale = 0.05

        self.btn_class.bind(size=self.update_font_size)
        self.btn_next.bind(size=self.update_font_size)
        self.gender_label.bind(size=self.update_font_size)
        self.class_not_label.bind(size=self.update_font_size)
        self.gender_not_label.bind(size=self.update_font_size)

        self.add_widget(self.gender_layout)
        self.add_widget(self.gender_label)
        self.add_widget(self.gender_not_label)

        self.add_widget(self.class_not_label)
        self.add_widget(self.btn_class)
        self.add_widget(self.btn_next)

    def is_can_next(self):
        gender = self.gender_layout.check_data()
        age = self.btn_class.text

        if not age.isdigit():
            self.class_not_label.text = "Выберите класс"

        if not gender:
            self.gender_not_label.text = "Вы не указали пол"
        else:
            self.gender_not_label.text = ""
        
        return gender and age.isdigit()

    def get_data(self):
        global data_dict

        if self.gender_layout.man_checkbox.active:
            data_dict["Gender"] = "Мужской пол"
        else:
            data_dict["Gender"] = "Женский пол"

        data_dict["Class"] = self.btn_class.text

    @staticmethod
    def update_font_size(instance, value):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size


class InterestsPage(FloatLayout):
    def __init__(self):
        super().__init__()

        self.interesting_label = Label(text="Список предпочитаемых предметов",
                                       size_hint=(1, .1),
                                       pos_hint={'center_x': 0.5, 'center_y': 0.95},
                                       halign="center",
                                       bold=True)

        self.interesting = MultiplyChoiceCheckBox(choices=classes[7].keys(),
                        size_hint=(.75, .7),
                        pos_hint={'center_x': 0.4, 'center_y': 0.57})

        self.interesting_label_not = Label(size_hint=(.1, .2),
                                           pos_hint={'center_x': 0.5, 'center_y': 0.18},
                                           color=[1, 0, 0, 1],
                                           halign="center")

        self.interesting_label.bind(size=self.update_font_size)
        self.interesting_label.scale = 0.05

        self.interesting_label_not.bind(size=self.update_font_size)
        self.interesting_label_not.scale = 0.05

        self.btn_next = Button(text="Следущая\nстраница",
                               pos_hint={'center_x': 0.75,
                                         'center_y': 0.1},
                               size_hint=(0.4, 0.15),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.btn_next.bind(size=self.update_font_size)
        self.btn_next.scale = 0.1

        self.btn_back = Button(text="Предыдущая\nстраница",
                               pos_hint={'center_x': 0.25,
                                         'center_y': 0.1},
                               size_hint=(0.4, 0.15),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.btn_back.bind(size=self.update_font_size)
        self.btn_back.scale = 0.1

        self.add_widget(self.btn_next)
        self.add_widget(self.btn_back)

        self.add_widget(self.interesting)
        self.add_widget(self.interesting_label)
        self.add_widget(self.interesting_label_not)

    def is_can_next(self):
        global data_dict

        interesting = self.interesting.check_data()
        interest_lst = self.interesting.get_data()

        data_dict["FavoriteSubjects"] = interest_lst

        if not interesting:
            self.interesting_label_not.text = "Выберите больше 0 и меньше 3"
        else:
            self.interesting_label_not.text = ""

        return interesting

    @staticmethod
    def update_font_size(instance, value):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size


class RestPage(FloatLayout):
    def __init__(self):
        super().__init__()
        self.rest_label = Label(text="Список предпочитаемого отдыха",
                                size_hint=(.1, .5),
                                pos_hint={'center_x': 0.55, 'center_y': 0.8},
                                halign="center")

        self.rest_label.bind(size=self.update_font_size)
        self.rest_label.scale = 0.1

        self.rest_cb = MultiplyChoiceCheckBox(rest,
                        size_hint=(.7, .4),
                        pos_hint={'center_x': 0.4, 'center_y': 0.5})

        self.rest_label_not = Label(size_hint=(.1, .2),
                                    pos_hint={'center_x': 0.5, 'center_y': 0.25},
                                    color=[1, 0, 0, 1],
                                    halign="center")

        self.rest_label_not.bind(size=self.update_font_size)
        self.rest_label_not.scale = 0.05

        self.btn_next = Button(text="Следущая\nстраница",
                               pos_hint={'center_x': 0.75,
                                         'center_y': 0.1},
                               size_hint=(0.4, 0.15),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center",
                               font_size=25)

        self.btn_next.bind(size=self.update_font_size)
        self.btn_next.scale = 0.1

        self.btn_back = Button(text="Предыдущая\nстраница",
                               pos_hint={'center_x': 0.25,
                                         'center_y': 0.1},
                               size_hint=(0.4, 0.15),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.btn_back.bind(size=self.update_font_size)
        self.btn_back.scale = 0.1

        self.add_widget(self.btn_next)
        self.add_widget(self.btn_back)

        self.add_widget(self.rest_cb)
        self.add_widget(self.rest_label)
        self.add_widget(self.rest_label_not)

    def is_can_next(self):
        global data_dict
        data_dict["Rest"] = self.rest_cb.get_data()

        rest = self.rest.check_data()

        if not rest:
            self.rest_label_not.text = "Выберите больше 0 и меньше 3"
        else:
            self.rest_label_not.text = ""

        return rest

    @staticmethod
    def update_font_size(instance, value):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size


class ResultPage(FloatLayout):
    def __init__(self):
        global data_dict

        super().__init__()

        self.welcome_label = Label(text="Опрос пройден.\n Вот результат:",
                                   pos_hint={'center_x': 0.5, 'center_y': 0.9},
                                   size_hint=(0.1, 0.05),
                                   font_size=30)
        rests = '\n'.join(data_dict['Rest'])
        interests = '\n'.join(data_dict['FavoriteSubjects'])
        sections = '\n'.join(data_dict['Sections'])

        self.info_text = Label(text=f"Пол: {data_dict['Gender']}\n\nВозраст: {data_dict['Class']}\n" +
                               f"Интересы: {interests}\n\nОтдых: {rests}\n\n Секции: {sections}")

        self.btn_next = Button(text="Завершить",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.1},
                               size_hint=(0.9, 0.1),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center",
                               font_size=25)

        self.add_widget(self.welcome_label)
        self.add_widget(self.info_text)
        self.add_widget(self.btn_next)

    @staticmethod
    def update_font_size(instance, value):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size


class SectionPage(FloatLayout):
    def __init__(self):
        global data_dict
        super().__init__()

        self.label = Label(text="В городе Бийск есть кружки.\n Выберите те, которые посещаете",
                                      pos_hint={'center_x': 0.5,
                                                'center_y': 0.9},
                                      size_hint=(0.1, 0.05),
                                      font_size=20)
        self.add_widget(self.label)

        self.choice_lst = []
        for subj_name in data_dict["FavoriteSubjects"]:
            self.choice_lst += classes[int(data_dict["Class"])][subj_name]
        self.choice_lst += ["Другое", "Ничего"]
        self.cb = MultiplyChoiceCheckBox(self.choice_lst,
                                         pos_hint={'center_x': 0.4,
                                                   'center_y': 0.5},
                                         size_hint=(0.6, 0.5))

        self.btn_next = Button(text="Следущая\nстраница",
                               pos_hint={'center_x': 0.75,
                                         'center_y': 0.1},
                               size_hint=(0.4, 0.15),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center",
                               font_size=25)

        self.btn_back = Button(text="Предыдущая\nстраница",
                               pos_hint={'center_x': 0.25,
                                         'center_y': 0.1},
                               size_hint=(0.4, 0.15),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center",
                               font_size=25)

        self.add_widget(self.btn_next)
        self.add_widget(self.btn_back)

        self.add_widget(self.cb)

    # @staticmethod
    def is_can_next(self):
        global data_dict
        data_dict["Sections"] = self.cb.get_data()
        return True