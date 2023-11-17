from customwidgets import *
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.core.window import Window
from config import *
from requests import get
from funcs import encrypt


def post_data():
    global data_dict

    url = f"http://192.168.4.1/post?telephone={encrypt(data_dict['PhoneNumber'])}&class={data_dict['Class']}&city={encrypt(data_dict['City'])}&gender={encrypt(data_dict['Gender'])}"

    for i, v in enumerate(data_dict['FavoriteSubjects']):
        url += f"&favorite_subjects{i}={encrypt(v)}"

    for i, v in enumerate(data_dict['Rests']):
        url += f"&rests{i}={encrypt(v)}"

    for i, v in enumerate(data_dict['Sections']):
        url += f"&sections{i}={encrypt(v)}"
    get(url)


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
        with self.canvas.before:
            Color(.38, .33, .86)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.title_label = Label(text="Привет, Друг!",
                                 pos_hint={'center_x': 0.5,
                                           'center_y': 0.8},
                                 size_hint=(0.1, 0.05),
                                 bold=True,
                                 halign="center")

        text = "Мы твои сверстники, и как и ты мы учимся в школе, но кроме школы у нас есть и другие увлечения."

        self.image = Image(source="creator_2.png",
                           pos_hint={'center_x': 0.5,
                                     'center_y': 0.4},
                           size_hint=(0.9, 1))

        self.text_label = Label(bold=True,
                                text=switch_new_line(text, 30),
                                pos_hint={'center_x': 0.5,
                                          'center_y': 0.65},
                                size_hint=(0.5, 0.4))

        self.btn_next = RoundedButton(color_=(.95, .94, .99),
                                    text="Познакомиться получше",
                                    pos_hint={'center_x': 0.5,
                                              'center_y': 0.1},
                                    size_hint=(0.6, 0.07),
                                    color=(.55, .51, 1),
                                    background_normal="",
                                    bold=True,
                                    halign="center")

        self.text_label_2 = Label(bold=True,
                                text="Давай познакомимся получше",
                                pos_hint={'center_x': 0.5,
                                          'center_y': 0.2},
                                size_hint=(0.5, 0.4),
                                color=(1, 1, 1))

        self.title_label.scale = .85
        self.text_label_2.scale = .1
        self.text_label.scale = 0.11
        self.btn_next.scale = 0.07

        self.btn_next.bind(size=self.update_font_size)
        self.text_label.bind(size=self.update_font_size)
        self.text_label_2.bind(size=self.update_font_size)
        self.title_label.bind(size=self.update_font_size)

        self.add_widget(self.title_label)
        self.add_widget(self.text_label)
        self.add_widget(self.text_label_2)
        self.add_widget(self.image)
        self.add_widget(self.btn_next)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    @staticmethod
    def is_can_next():
        return True

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size


class AboutAlexPage(FloatLayout):
    def __init__(self):
        super().__init__()
        with self.canvas.before:
            Color(1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

            Color(82/255, 70/255, 205/255)
            self.design_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[50,])

        text = "Меня зовут Алексей, я увлечен программированием и в свободное от школы время занимаюсь им"

        self.image = Image(source="Logo/Alex.png",
                           pos_hint={'center_x': 0.5,
                                     'center_y': 0.71},
                           size_hint=(0.5, 1))

        self.text_label = Label(bold=True,
                                text=switch_new_line(text, 30),
                                pos_hint={'center_x': 0.5,
                                          'center_y': 0.4},
                                size_hint=(0.5, 0.4),
                                color=(0, 0, 0, 1))

        self.btn_next = RoundedButton(color_=(.39, .34, .89),
                                    text="Далее",
                                    pos_hint={'center_x': 0.5,
                                              'center_y': 0.1},
                                    size_hint=(0.6, 0.07),
                                    color=(1, 1, 1),
                                    background_color=(0, 0, 0, 1),
                                    background_normal="",
                                    bold=True,
                                    halign="center")

        self.text_label.scale = 0.11
        self.btn_next.scale = 0.07

        self.btn_next.bind(size=self.update_font_size)
        self.text_label.bind(size=self.update_font_size)

        self.add_widget(self.text_label)
        self.add_widget(self.image)
        self.add_widget(self.btn_next)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

        self.design_rect.size = (instance.size[0], instance.size[1]*0.6)
        self.design_rect.pos = (instance.pos[0], instance.pos[1]*0.5 + instance.size[1]*0.5)

    @staticmethod
    def is_can_next():
        return True

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size


class AboutElPage(FloatLayout):
    def __init__(self):
        super().__init__()
        with self.canvas.before:
            Color(1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

            Color(82/255, 70/255, 205/255)
            self.design_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[50,])

        text = "Меня зовут Элеонора. Я изучаю китайский язык"
        text_2 = "Мы рассказали про себя, давай теперь познакомимся с тобой"
        self.image = Image(source="Logo/El.png",
                           pos_hint={'center_x': 0.5,
                                     'center_y': 0.73},
                           size_hint=(0.5, 1))

        self.text_label = Label(bold=True,
                                text=switch_new_line(text, 30),
                                pos_hint={'center_x': 0.5,
                                          'center_y': 0.4},
                                size_hint=(0.5, 0.4),
                                color=(1, 1, 1))

        self.text_2_label = Label(bold=True,
                                text=switch_new_line(text_2, 30),
                                pos_hint={'center_x': 0.5,
                                          'center_y': 0.25},
                                size_hint=(0.5, 0.4),
                                color=(1, 1, 1))

        self.btn_next = RoundedButton(color_=(.95, .94, .99),
                                text="Рассказать про себя",
                                pos_hint={'center_x': 0.5,
                                             'center_y': 0.1},
                                size_hint=(0.6, 0.07),
                                color=(.55, .51, 1),
                                background_normal="",
                                bold=True,
                                halign="center")

        self.text_label.scale = 0.11
        self.text_2_label.scale = 0.11
        self.btn_next.scale = 0.07

        self.btn_next.bind(size=self.update_font_size)
        self.text_label.bind(size=self.update_font_size)
        self.text_2_label.bind(size=self.update_font_size)

        self.add_widget(self.text_label)
        self.add_widget(self.text_2_label)
        self.add_widget(self.image)
        self.add_widget(self.btn_next)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

        self.design_rect.size = (instance.size[0], instance.size[1]*0.7)
        self.design_rect.pos = (instance.pos[0], -instance.size[1]*0.155)

    @staticmethod
    def is_can_next():
        return True

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size


class CityPage(FloatLayout):
    def __init__(self):
        super().__init__()
        with self.canvas.before:
            Color(.38, .33, .86)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        text = "Выберите свой город, из перечисленных"
        self.title_label = Label(text=switch_new_line(text, 30),
                                 pos_hint={'center_x': 0.5,
                                           'center_y': 0.8},
                                 size_hint=(0.1, 0.05),
                                 bold=True)

        self.btn_search_city = RoundedButton(color_=(1, 1, 1),
                                             radius_=10,
                                text="Выбрать город",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.65},
                               size_hint=(0.6, 0.07),
                               color=(.55, .51, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.dropdown_city = DropDownCity(height_win=Window.height)

        self.btn_search_city.bind(on_release=self.dropdown_city.open)
        self.dropdown_city.bind(on_select=self.show_next)

        self.btn_next = RoundedButton(color_=(1, 1, 1),
                                text="Далее",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.1},
                               size_hint=(0.6, 0.07),
                               color=(.55, .51, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.title_label.scale = .8
        self.btn_next.scale = 0.07
        self.btn_search_city.scale = 0.07

        self.btn_next.bind(size=self.update_font_size)
        self.btn_search_city.bind(size=self.update_font_size)
        self.title_label.bind(size=self.update_font_size)

        self.add_widget(self.title_label)

        self.add_widget(self.btn_search_city)
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def show_next(self, instance, x):
        self.remove_widget(self.btn_next)
        self.btn_search_city.text = x
        self.add_widget(self.btn_next)

    @staticmethod
    def is_can_next():
        return True

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size

    def get_data(self):
        global data_dict

        data_dict["City"] = self.btn_search_city.text


class GenderPage(FloatLayout):
    def __init__(self):
        super().__init__()
        with self.canvas.before:
            Color(1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

            Color(82/255, 70/255, 205/255)
            self.design_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[50,])

        self.title_label = Label(bold=True,
                                text="Кто ты?",
                                pos_hint={'center_x': 0.5,
                                          'center_y': 0.9},
                                size_hint=(0.5, 0.4),
                                color=(1, 1, 1),
                                 halign="center")

        self.gender_layout = GenderLayout(pos_hint={'center_x': 0.45, 'center_y': 0.82},
                                          size_hint=(1, .1))
        self.gender_layout.man_checkbox.bind(active=self.on_radiobutton)
        self.gender_layout.woman_checkbox.bind(active=self.on_radiobutton)

        self.image = Image(pos_hint={'center_x': 0.5,
                                     'center_y': 0.4},
                           size_hint=(0.5, 0.5))

        self.btn_next = RoundedButton(color_=(.39, .34, .89),
                                text="Далее",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.1},
                               size_hint=(0.6, 0.07),
                               color=(1, 1, 1),
                               background_color=(0, 0, 0, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.title_label.scale = 0.2
        self.btn_next.scale = 0.07

        self.btn_next.bind(size=self.update_font_size)
        self.title_label.bind(size=self.update_font_size)

        self.add_widget(self.title_label)
        self.add_widget(self.gender_layout)
        self.add_widget(self.image)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

        self.design_rect.size = (instance.size[0], instance.size[1]*0.4)
        self.design_rect.pos = (instance.pos[0], instance.pos[1] + instance.size[1]*0.7)

    @staticmethod
    def is_can_next():
        return True

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size

    def on_radiobutton(self, instance, value):
        if value:
            if "м" in instance.label.text.lower():
                self.image.source = "man.png"
            else:
                self.image.source = "woman.png"
            self.add_widget(self.btn_next)
        else:
            self.image.source = ""
            self.remove_widget(self.btn_next)

    def get_data(self):
        global data_dict
        if self.gender_layout.man_checkbox.active:
            data_dict["Gender"] = "Мальчик"
        else:
            data_dict["Gender"] = "Девочка"


class ClassPage(FloatLayout):
    def __init__(self):
        super().__init__()
        with self.canvas.before:
            Color(1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

            Color(82/255, 70/255, 205/255)
            self.design_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[50,])

        text = "В каком ты классе?"

        self.text_label = Label(bold=True,
                                text=switch_new_line(text, 30),
                                pos_hint={'center_x': 0.5,
                                          'center_y': 0.95},
                                size_hint=(0.5, 0.4),
                                color=(0, 0, 0))

        self.btn_class = RoundedButton(color_=(1, 1, 1),
                                             radius_=10,
                                             text="Выбрать класс",
                                             pos_hint={'center_x': 0.5,
                                                       'center_y': 0.7},
                                             size_hint=(0.6, 0.07),
                                             color=(.55, .51, 1),
                                             background_normal="",
                                             bold=True,
                                             halign="center")
        self.dropdown_class = DropDownClasses(height_win=Window.height)

        self.btn_class.bind(on_release=self.dropdown_class.open)
        self.dropdown_class.bind(on_select=self.show_next)

        self.btn_next = RoundedButton(color_=(.95, .94, .99),
                                text="Далее",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.1},
                               size_hint=(0.6, 0.07),
                               color=(.55, .51, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.text_label.scale = 0.17
        self.btn_next.scale = 0.07

        self.btn_next.bind(size=self.update_font_size)
        self.text_label.bind(size=self.update_font_size)

        self.add_widget(self.text_label)
        self.add_widget(self.btn_class)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

        self.design_rect.size = (instance.size[0], instance.size[1])
        self.design_rect.pos = (instance.pos[0], -instance.size[1]*0.155)

    def show_next(self, instance, x):
        self.remove_widget(self.btn_next)
        self.btn_class.text = x
        self.add_widget(self.btn_next)

    @staticmethod
    def is_can_next():
        return True

    def get_data(self):
        global data_dict
        data_dict["Class"] = int(self.btn_class.text)

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size


class InterestsPage(FloatLayout):
    def __init__(self):
        super().__init__()
        with self.canvas.before:
            Color(1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

            Color(82/255, 70/255, 205/255)
            self.design_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[50,])

        text = "Выбери предметы,\nкоторые тебе интересны"

        self.title_label = Label(bold=True,
                                text=text,
                                pos_hint={'center_x': 0.5,
                                          'center_y': 0.95},
                                size_hint=(0.5, 0.4),
                                color=(0, 0, 0),
                                halign="center")

        self.btn_next = RoundedButton(color_=(.95, .94, .99),
                                text="Далее",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.1},
                               size_hint=(0.6, 0.07),
                               color=(.55, .51, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.title_label.scale = 0.15
        self.btn_next.scale = 0.07

        self.btn_next.bind(size=self.update_font_size)
        self.title_label.bind(size=self.update_font_size)

        self.add_widget(self.title_label)
        self.add_widget(self.btn_next)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

        self.design_rect.size = (instance.size[0], instance.size[1])
        self.design_rect.pos = (instance.pos[0], -instance.size[1]*0.155)

    def update(self):
        self.interesting = MultiplyChoiceCheckBox(choices=city_dict[data_dict["City"]][data_dict["Class"]].keys(),
                                                  size_hint=(.75, .6),
                                                  pos_hint={'center_x': 0.4, 'center_y': 0.5})
        self.add_widget(self.interesting)

    @staticmethod
    def is_can_next():
        return True

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size

    def get_data(self):
        global data_dict
        data_dict["FavoriteSubjects"] = self.interesting.get_data()


class RestPage(FloatLayout):
    def __init__(self):
        super().__init__()
        with self.canvas.before:
            Color(1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

            Color(82/255, 70/255, 205/255)
            self.design_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[50,])

        self.title_label = Label(bold=True,
                                text="Как ты обычно отдыхаешь?",
                                pos_hint={'center_x': 0.5,
                                          'center_y': 0.9},
                                size_hint=(0.5, 0.4),
                                color=(1, 1, 1),
                                 halign="center")

        self.btn_next = RoundedButton(color_=(.39, .34, .89),
                                      text="Далее",
                                      pos_hint={'center_x': 0.5,
                                                'center_y': 0.1},
                                      size_hint=(0.6, 0.07),
                                      color=(1, 1, 1),
                                      background_color=(0, 0, 0, 1),
                                      background_normal="",
                                      bold=True,
                                      halign="center")

        self.rest_cb = MultiplyChoiceCheckBox(rest,
                                              size_hint=(.8, .5),
                                              pos_hint={'center_x': 0.35, 'center_y': 0.6})

        self.title_label.scale = 0.14
        self.btn_next.scale = 0.07

        self.btn_next.bind(size=self.update_font_size)
        self.title_label.bind(size=self.update_font_size)

        self.add_widget(self.title_label)
        self.add_widget(self.rest_cb)
        self.add_widget(self.btn_next)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

        self.design_rect.size = (instance.size[0], instance.size[1]*0.9)
        self.design_rect.pos = (instance.pos[0], instance.pos[1] + instance.size[1] * 0.2)

    @staticmethod
    def is_can_next():
        return True

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size

    def get_data(self):
        global data_dict
        data_dict["Rests"] = self.rest_cb.get_data()

    def on_radiobutton(self, instance, value):
        if value:
            if "м" in instance.label.text.lower():
                self.image.source = "man.png"
            else:
                self.image.source = "woman.png"
            self.add_widget(self.btn_next)
        else:
            self.image.source = ""
            self.remove_widget(self.btn_next)


class SectionPage(FloatLayout):
    def __init__(self):
        global data_dict
        super().__init__()
        with self.canvas.before:
            Color(1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

            Color(82/255, 70/255, 205/255)
            self.design_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[50,])

        text = f"В городе {data_dict['City']} есть кружки.\n Выберите те, которые посещаете"

        self.title_label = Label(bold=True,
                                text=text,
                                pos_hint={'center_x': 0.5,
                                          'center_y': 0.95},
                                size_hint=(0.5, 0.4),
                                color=(0, 0, 0),
                                halign="center")

        self.choice_lst = []
        for subj_name in data_dict["FavoriteSubjects"]:
            self.choice_lst += city_dict[data_dict["City"]][int(data_dict["Class"])][subj_name]
        self.choice_lst += ["Другое", "Ничего"]
        self.cb = MultiplyChoiceCheckBox(self.choice_lst,
                                         pos_hint={'center_x': 0.4,
                                                   'center_y': 0.5},
                                         size_hint=(0.6, 0.5))

        self.btn_next = RoundedButton(color_=(.95, .94, .99),
                                text="Далее",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.1},
                               size_hint=(0.6, 0.07),
                               color=(.55, .51, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.title_label.scale = 0.12
        self.btn_next.scale = 0.07

        self.btn_next.bind(size=self.update_font_size)
        self.title_label.bind(size=self.update_font_size)

        self.add_widget(self.title_label)
        self.add_widget(self.cb)
        self.add_widget(self.btn_next)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

        self.design_rect.size = (instance.size[0], instance.size[1])
        self.design_rect.pos = (instance.pos[0], -instance.size[1]*0.155)

    def update(self):
        self.remove_widget(self.title_label)
        text = f"В городе {data_dict['City']} есть кружки.\n Выберите те, которые посещаете"

        self.title_label = Label(bold=True,
                                text=text,
                                pos_hint={'center_x': 0.5,
                                          'center_y': 0.95},
                                size_hint=(0.5, 0.4),
                                color=(0, 0, 0),
                                halign="center")
        self.title_label.scale = 0.12
        self.title_label.bind(size=self.update_font_size)
        self.add_widget(self.title_label)

        self.remove_widget(self.cb)
        self.choice_lst = []
        for subj_name in data_dict["FavoriteSubjects"]:
            self.choice_lst += city_dict[data_dict["City"]][int(data_dict["Class"])][subj_name]
        self.choice_lst += ["Другое", "Ничего"]
        self.cb = MultiplyChoiceCheckBox(self.choice_lst,
                                         pos_hint={'center_x': 0.4,
                                                   'center_y': 0.5},
                                         size_hint=(0.6, 0.5))
        self.add_widget(self.cb)

    @staticmethod
    def is_can_next():
        return True

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size

    def get_data(self):
        global data_dict
        data_dict["Sections"] = self.cb.get_data()


class AboutPage(FloatLayout):
    def __init__(self):
        super().__init__()
        with self.canvas.before:
            Color(.38, .33, .86)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.text_label = Label(bold=True,
                                text=switch_new_line("", 30),
                                pos_hint={'center_x': 0.5,
                                          'center_y': 0.65},
                                size_hint=(0.5, 0.4))

        self.btn_next = RoundedButton(color_=(1, 1, 1),
                                text="Дальше",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.1},
                               size_hint=(0.6, 0.07),
                               color=(.55, .51, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

        self.text_label.scale = 0.11
        self.btn_next.scale = 0.07

        self.btn_next.bind(size=self.update_font_size)
        self.text_label.bind(size=self.update_font_size)

        self.add_widget(self.text_label)
        self.add_widget(self.btn_next)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    @staticmethod
    def is_can_next():
        return True

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size

    def update(self):
        global data_dict

        if len(data_dict["Sections"]) == 0 or data_dict["Sections"][0] == "Ничего":
            text = "В вашем городе есть кружки вам по интересам, вы можете записаться на них"
        elif 0 < len(data_dict["Sections"]) < 3:
            text = "У вас все хорошо"
        else:
            text = "А тебе нормально столько кружков"

        self.text_label.text = switch_new_line(text, 20) + "\n\n" + switch_new_line(
            "На следующей странице вы можете указать телефон родителя, чтобы мы рассказали о ваших результатах", 25)


class TelephonePage(FloatLayout):
    def __init__(self):
        super().__init__()
        with self.canvas.before:
            Color(1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

            Color(82/255, 70/255, 205/255)
            self.design_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[50,])

        self.is_opened_kb = False
        text = "Ты можешь указать телефон родителя"

        self.text_label = Label(bold=True,
                                text=switch_new_line(text, 25),
                                pos_hint={'center_x': 0.5,
                                          'center_y': 0.95},
                                size_hint=(0.5, 0.4),
                                color=(0, 0, 0),
                                halign="center")

        self.telephone_label = RoundedButton(color_=(1, 1, 1),
                                             radius_=10,
                                             text="",  # +7 (XXX) XXX-XX-XX
                                             pos_hint={'center_x': 0.5,
                                                       'center_y': 0.7},
                                             size_hint=(0.6, 0.07),
                                             color=(.55, .51, 1),
                                             background_normal="",
                                             bold=True,
                                             halign="center")

        self.telephone_label.bind(on_press=self.open_keyboard)
        self.number_keyboard = NumberKeyboard(self.telephone_label,
                                              pos_hint={'center_x': 0.5,
                                                        'center_y': 0.2},
                                              size_hint=(1, 0.4))

        self.btn_next = RoundedButton(color_=(.95, .94, .99),
                                text="Далее",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.1},
                               size_hint=(0.6, 0.07),
                               color=(.55, .51, 1),
                               background_normal="",
                               bold=True,
                               halign="center")

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
        self.telephone_label.scale = 0.1

        self.text_label.scale = 0.15
        self.btn_next.scale = 0.07

        self.btn_next.bind(size=self.update_font_size)
        self.text_label.bind(size=self.update_font_size)
        self.telephone_label.bind(size=self.update_font_size)

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

        self.add_widget(self.text_label)
        self.add_widget(self.telephone_label)
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

        self.design_rect.size = (instance.size[0], instance.size[1])
        self.design_rect.pos = (instance.pos[0], -instance.size[1]*0.155)

    def show_next(self, instance, x):
        setattr(self.btn_class, "text", x)
        self.add_widget(self.btn_next)

    def open_keyboard(self, _):
        if not self.is_opened_kb:
            self.add_widget(self.number_keyboard)
            self.remove_widget(self.btn_next)
        else:
            self.remove_widget(self.number_keyboard)
            self.add_widget(self.btn_next)

        self.is_opened_kb = not self.is_opened_kb

    def press_number(self, instance):
        if self.is_opened_kb:
            self.telephone_label.text += instance.text

    def delete(self, _):
        if len(self.telephone_label.text) > 0:
            self.telephone_label.text = self.telephone_label.text[:-1]

    def get_data(self):
        global data_dict
        data_dict["PhoneNumber"] = self.telephone_label.text

    def enter(self, _):
        if self.is_opened_kb:
            self.is_opened_kb = False

            self.remove_widget(self.number_keyboard)
            self.add_widget(self.btn_next)

    @staticmethod
    def is_can_next():
        return True


    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size


class ResultPage(FloatLayout):
    def __init__(self):
        super().__init__()

        self.welcome_label = Label(text="Опрос пройден.\n Вот результат:",
                                   pos_hint={'center_x': 0.5, 'center_y': 0.9},
                                   size_hint=(0.1, 0.05))

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
                               halign="center")

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


class CompletionPage(FloatLayout):
    def __init__(self):
        super().__init__()
        with self.canvas.before:
            Color(.38, .33, .86)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        text = "Спасибо за прохождение!"

        self.text_label = Label(bold=True,
                                text=switch_new_line(text, 30),
                                pos_hint={'center_x': 0.5,
                                          'center_y': 0.65},
                                size_hint=(0.5, 0.4))

        self.btn_next = RoundedButton(color_=(1, 1, 1),
                                text="Завершить",
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.1},
                               size_hint=(0.6, 0.07),
                               color=(.55, .51, 1),
                               background_normal="",
                               bold=True,
                               halign="center")
        self.text_label.scale = 0.15
        self.btn_next.scale = 0.07

        self.btn_next.bind(size=self.update_font_size)
        self.text_label.bind(size=self.update_font_size)

        self.add_widget(self.text_label)
        self.add_widget(self.btn_next)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update(self):
        post_data()

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    @staticmethod
    def is_can_next():
        return True

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size
