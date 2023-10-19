from customwidgets import *
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

from config import *


def switch_new_line(text, max_line_length):
    lines = []
    current_line = ""

    for line in text.split("\n"):
        for word in line.split():
            if len(current_line + word) < max_line_length:
                current_line += ' ' + word
            else:
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)
            current_line = ""

    return '\n'.join(lines)


class WelcomePage(FloatLayout):
    def __init__(self):
        super().__init__()
        self.title_label = Label(text="Привет, Друг!",
                                 pos_hint={'center_x': 0.5,
                                           'center_y': 0.9},
                                 size_hint=(0.1, 0.05),
                                 bold=True,
                                 halign="center")

        text = "Мы твои сверстники. У нас есть увлечения кроме школы."

        self.text_label = Label(text=switch_new_line(text, 20),
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
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size


class GenderPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.gender_label = Label(text="Выберите пол:",
                                  pos_hint={'center_x': 0.5,
                                            'center_y': 0.9},
                                  halign="center",
                                  bold=True,
                                  font_size=25)

        self.gender_layout = GenderLayout(pos_hint={'center_x': 0.45, 'center_y': 0.82},
                                          size_hint=(1, .1))
        self.gender_layout.man_checkbox.bind(active=self.on_radiobutton)
        self.gender_layout.woman_checkbox.bind(active=self.on_radiobutton)

        self.gender_not_label = Label(pos_hint={'center_x': 0.5,
                                                'center_y': 0.7},
                                      halign="center",
                                      color=[1, 0, 0, 1],
                                      bold=True,
                                      font_size=20)

        self.image = Image(pos_hint={'center_x': 0.5,
                                     'center_y': 0.5},
                           size_hint=(0.5, 0.5),
                           color=background_canvas_color)

        self.btn_next = Button(text="Следующая страница",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.1},
                               size_hint=(0.9, 0.1),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.btn_next.scale = 0.07
        self.gender_label.scale = 0.07
        self.gender_not_label.scale = 0.05

        self.btn_next.bind(size=self.update_font_size)
        self.gender_label.bind(size=self.update_font_size)
        self.gender_not_label.bind(size=self.update_font_size)

        self.add_widget(self.gender_layout)
        self.add_widget(self.image)
        self.add_widget(self.gender_label)
        self.add_widget(self.gender_not_label)

        self.add_widget(self.btn_next)

    def is_can_next(self):
        gender = self.gender_layout.check_data()

        if not gender:
            self.gender_not_label.text = "Вы не указали пол"
        else:
            self.gender_not_label.text = ""

        return gender

    def get_data(self):
        global data_dict

        if self.gender_layout.man_checkbox.active:
            data_dict["Gender"] = "Мужской пол"
        else:
            data_dict["Gender"] = "Женский пол"

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size

    def on_radiobutton(self, instance, value):
        if value:
            if instance.label.text == "Мужской":
                self.image.source = "man_logo.jpg"
            else:
                self.image.source = "woman_logo.png"
            self.image.color = (1, 1, 1, 1)


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
                                          size_hint=(1, .1))

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

        self.btn_next = Button(text="Следующая страница",
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
    def update_font_size(instance, _):
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

        self.interesting_label_not = Label(size_hint=(.5, .2),
                                           pos_hint={'center_x': 0.5, 'center_y': 0.19},
                                           color=[1, 0, 0, 1],
                                           halign="center")

        self.btn_next = Button(text="Следующая\nстраница",
                               pos_hint={'center_x': 0.75,
                                         'center_y': 0.1},
                               size_hint=(0.4, 0.15),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.btn_back = Button(text="Предыдущая\nстраница",
                               pos_hint={'center_x': 0.25,
                                         'center_y': 0.1},
                               size_hint=(0.4, 0.15),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.btn_back.scale = 0.15
        self.btn_next.scale = 0.15
        self.interesting_label.scale = 0.05
        self.interesting_label_not.scale = 0.1

        self.btn_back.bind(size=self.update_font_size)
        self.btn_next.bind(size=self.update_font_size)
        self.interesting_label.bind(size=self.update_font_size)
        self.interesting_label_not.bind(size=self.update_font_size)

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
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size


class RestPage(FloatLayout):
    def __init__(self):
        super().__init__()
        self.rest_label = Label(text="Список предпочитаемого отдыха",
                                size_hint=(1, .5),
                                pos_hint={'center_x': 0.55, 'center_y': 0.8},
                                halign="center",
                                bold=True)

        self.rest_cb = MultiplyChoiceCheckBox(rest,
                                              size_hint=(.7, .4),
                                              pos_hint={'center_x': 0.4, 'center_y': 0.5})

        self.rest_label_not = Label(size_hint=(.5, .2),
                                    pos_hint={'center_x': 0.5, 'center_y': 0.25},
                                    color=[1, 0, 0, 1],
                                    halign="center",
                                    bold=True)

        self.btn_next = Button(text="Следующая\nстраница",
                               pos_hint={'center_x': 0.75,
                                         'center_y': 0.1},
                               size_hint=(0.4, 0.15),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.btn_back = Button(text="Предыдущая\nстраница",
                               pos_hint={'center_x': 0.25,
                                         'center_y': 0.1},
                               size_hint=(0.4, 0.15),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.rest_label_not.scale = 0.1
        self.rest_label.scale = 0.05
        self.btn_next.scale = 0.15
        self.btn_back.scale = 0.15

        self.rest_label.bind(size=self.update_font_size)
        self.rest_label_not.bind(size=self.update_font_size)
        self.btn_next.bind(size=self.update_font_size)
        self.btn_back.bind(size=self.update_font_size)

        self.add_widget(self.btn_next)
        self.add_widget(self.btn_back)

        self.add_widget(self.rest_cb)
        self.add_widget(self.rest_label)
        self.add_widget(self.rest_label_not)

    def is_can_next(self):
        global data_dict
        data_dict["Rests"] = self.rest_cb.get_data()

        if not data_dict["Rests"]:
            self.rest_label_not.text = "Выберите больше 0 и меньше 3"
        else:
            self.rest_label_not.text = ""

        return bool(data_dict["Rests"])

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size


class SectionPage(FloatLayout):
    def __init__(self):
        global data_dict
        super().__init__()

        self.label = Label(text="В городе Бийск есть кружки.\n Выберите те, которые посещаете",
                           pos_hint={'center_x': 0.5,
                                     'center_y': 0.9},
                           size_hint=(0.8, 0.05),
                           bold=True)
        self.add_widget(self.label)

        self.choice_lst = []
        for subj_name in data_dict["FavoriteSubjects"]:
            self.choice_lst += classes[int(data_dict["Class"])][subj_name]
        self.choice_lst += ["Другое", "Ничего"]
        self.cb = MultiplyChoiceCheckBox(self.choice_lst,
                                         pos_hint={'center_x': 0.4,
                                                   'center_y': 0.5},
                                         size_hint=(0.6, 0.5))

        self.btn_next = Button(text="Следующая\nстраница",
                               pos_hint={'center_x': 0.75,
                                         'center_y': 0.1},
                               size_hint=(0.4, 0.15),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.btn_back = Button(text="Предыдущая\nстраница",
                               pos_hint={'center_x': 0.25,
                                         'center_y': 0.1},
                               size_hint=(0.4, 0.15),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.label_section_not = Label(text="")

        self.btn_back.scale = 0.15
        self.btn_next.scale = 0.15
        self.label.scale = 0.07
        self.label_section_not.scale = 0.1

        self.btn_next.bind(size=self.update_font_size)
        self.btn_back.bind(size=self.update_font_size)
        self.label.bind(size=self.update_font_size)
        self.label_section_not.bind(size=self.update_font_size)

        self.add_widget(self.btn_next)
        self.add_widget(self.btn_back)

        self.add_widget(self.cb)

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size

    def is_can_next(self):
        global data_dict
        data_dict["Sections"] = self.cb.get_data()

        if len(data_dict["Sections"]) != 1 and "Ничего" in data_dict["Sections"]:
            pass

        if not data_dict["Sections"]:
            data_dict["Sections"] = ["Ничего"]
        return bool(data_dict["Sections"])

    def update(self):
        self.remove_widget(self.cb)
        self.choice_lst = []
        for subj_name in data_dict["FavoriteSubjects"]:
            self.choice_lst += classes[int(data_dict["Class"])][subj_name]
        self.choice_lst += ["Другое", "Ничего"]
        self.cb = MultiplyChoiceCheckBox(self.choice_lst,
                                         pos_hint={'center_x': 0.4,
                                                   'center_y': 0.5},
                                         size_hint=(0.6, 0.5))
        self.add_widget(self.cb)


class TelephonePage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_opened_kb = False
        self.label = Label(text="Укажите телефон",
                           pos_hint={'center_x': 0.5,
                                     'center_y': 0.9},
                           size_hint=(1, 0.3),
                           bold=True)

        self.telephone_label = Button(text="",  # +7 (XXX) XXX-XX-XX
                                      pos_hint={'center_x': 0.5,
                                                'center_y': 0.5},
                                      size_hint=(.7, 0.1),
                                      bold=True,
                                      background_normal="",
                                      background_down="",
                                      background_color=(1, .4, .4, 1))

        self.telephone_label.bind(on_press=self.open_keyboard)
        self.number_keyboard = NumberKeyboard(self.label,
                                              pos_hint={'center_x': 0.5,
                                                        'center_y': 0.2},
                                              size_hint=(1, 0.4))

        self.btn_next = Button(text="Следующая\nстраница",
                               pos_hint={'center_x': 0.75,
                                         'center_y': 0.1},
                               size_hint=(0.4, 0.15),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.btn_back = Button(text="Предыдущая\nстраница",
                               pos_hint={'center_x': 0.25,
                                         'center_y': 0.1},
                               size_hint=(0.4, 0.15),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.btn_back.scale = 0.15
        self.btn_next.scale = 0.15
        self.telephone_label.scale = 0.1
        self.label.scale = 0.1

        self.number_keyboard.btn_0.scale = \
            self.number_keyboard.btn_1.scale = \
            self.number_keyboard.btn_2.scale = \
            self.number_keyboard.btn_3.scale = \
            self.number_keyboard.btn_4.scale = \
            self.number_keyboard.btn_5.scale = \
            self.number_keyboard.btn_6.scale = \
            self.number_keyboard.btn_7.scale = \
            self.number_keyboard.btn_8.scale = \
            self.number_keyboard.btn_9.scale = \
            self.number_keyboard.btn_delete.scale = \
            self.number_keyboard.btn_enter.scale = 0.3

        self.btn_next.bind(size=self.update_font_size)
        self.btn_back.bind(size=self.update_font_size)
        self.telephone_label.bind(size=self.update_font_size)
        self.label.bind(size=self.update_font_size)

        self.add_widget(self.btn_next)
        self.add_widget(self.btn_back)

        self.number_keyboard.btn_1.bind(on_press=self.press_number, size=self.update_font_size)
        self.number_keyboard.btn_2.bind(on_press=self.press_number, size=self.update_font_size)
        self.number_keyboard.btn_3.bind(on_press=self.press_number, size=self.update_font_size)
        self.number_keyboard.btn_4.bind(on_press=self.press_number, size=self.update_font_size)
        self.number_keyboard.btn_5.bind(on_press=self.press_number, size=self.update_font_size)
        self.number_keyboard.btn_6.bind(on_press=self.press_number, size=self.update_font_size)
        self.number_keyboard.btn_7.bind(on_press=self.press_number, size=self.update_font_size)
        self.number_keyboard.btn_8.bind(on_press=self.press_number, size=self.update_font_size)
        self.number_keyboard.btn_9.bind(on_press=self.press_number, size=self.update_font_size)
        self.number_keyboard.btn_0.bind(on_press=self.press_number, size=self.update_font_size)
        self.number_keyboard.btn_delete.bind(on_press=self.delete)

        self.number_keyboard.btn_enter.bind(on_press=self.enter)
        self.add_widget(self.label)
        self.add_widget(self.telephone_label)

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size

    def open_keyboard(self, _):
        if not self.is_opened_kb:
            self.add_widget(self.number_keyboard)
            self.remove_widget(self.btn_next)
            self.remove_widget(self.btn_back)
        else:
            self.remove_widget(self.number_keyboard)
            self.add_widget(self.btn_next)
            self.add_widget(self.btn_back)

        self.is_opened_kb = not self.is_opened_kb

    def press_number(self, instance):
        if self.is_opened_kb:
            self.telephone_label.text += instance.text

    def delete(self, _):
        if len(self.telephone_label.text) > 0:
            self.telephone_label.text = self.telephone_label.text[:-1]

    def enter(self, _):
        if self.is_opened_kb:
            self.is_opened_kb = False

            self.remove_widget(self.number_keyboard)
            self.add_widget(self.btn_next)
            self.add_widget(self.btn_back)

    def is_can_next(self):
        print(self.telephone_label.text)
        return True


class ResultPage(FloatLayout):
    def __init__(self):
        super().__init__()

        self.welcome_label = Label(text="Опрос пройден.\n Вот результат:",
                                   pos_hint={'center_x': 0.5, 'center_y': 0.9},
                                   size_hint=(0.1, 0.05),
                                   font_size=30)

        self.info_text = Label(text=f"Пол: {data_dict['Gender']}\n\nВозраст: {data_dict['Class']}\n" +
                                    f"Интересы: {data_dict['FavoriteSubjects']}\n\nОтдых: {data_dict['Rests']}\n\n "
                                    f"Секции: {data_dict['Sections']}")

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
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size

    def update(self):
        self.info_text.text = f"Пол: {data_dict['Gender']}\n\nВозраст: {data_dict['Class']}\n" + \
                              f"Интересы: {data_dict['FavoriteSubjects']}\n\nОтдых: {data_dict['Rests']}\n\n" + \
                              f"Секции: {data_dict['Sections']}"


class AboutPage(FloatLayout):
    def __init__(self):
        super().__init__()
        self.text_label = Label(text="",
                                pos_hint={'center_x': 0.5,
                                          'center_y': 0.6},
                                size_hint=(0.5, 0.4))

        self.btn_next = Button(text="Дальше",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.1},
                               size_hint=(0.9, 0.1),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.text_label.scale = 0.15
        self.btn_next.scale = 0.1

        self.btn_next.bind(size=self.update_font_size)
        self.text_label.bind(size=self.update_font_size)

        self.add_widget(self.text_label)
        self.add_widget(self.btn_next)

    @staticmethod
    def is_can_next():
        return True

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size

    def update(self):
        global data_dict

        if len(data_dict["Sections"]) == 0 or data_dict["Sections"][0] == "Другое":
            text = "В вашем городе есть кружки вам по интересам, вы можете записаться на них"
        elif 0 < len(data_dict["Sections"]) < 3:
            text = "У вас все хорошо"
        else:
            text = "А тебе нормально столько кружков"

        self.text_label.text = switch_new_line(text, 20) + "\n" + switch_new_line(
            "На следующей странице вы можете указать телефон родителя, чтобы мы рассказали о ваших результатах", 25)


class CompletionPage(FloatLayout):
    def __init__(self):
        super().__init__()
        text = "Спасибо за прохождение опроса"
        self.text_label = Label(text=switch_new_line(text, 20),
                                pos_hint={'center_x': 0.5,
                                          'center_y': 0.6},
                                size_hint=(0.5, 0.4))

        self.btn_next = Button(text="Завершить",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.1},
                               size_hint=(0.9, 0.1),
                               background_color=(1, .4, .4, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.text_label.scale = 0.15
        self.btn_next.scale = 0.1

        self.btn_next.bind(size=self.update_font_size)
        self.text_label.bind(size=self.update_font_size)

        self.add_widget(self.text_label)
        self.add_widget(self.btn_next)

    @staticmethod
    def is_can_next():
        return True

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size
