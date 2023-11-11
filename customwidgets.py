from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle

from config import *


class GenderLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"

        self.man_checkbox = CheckBox(group="gender",
                                     color=(1, 1, 1, 1))
        self.man_checkbox.label = Label(text="Мальчик",
                                        bold=True)
        self.add_widget(self.man_checkbox)
        self.add_widget(self.man_checkbox.label)

        self.woman_checkbox = CheckBox(group="gender")
        self.woman_checkbox.label = Label(text="Девочка",
                                          bold=True)

        self.woman_checkbox.label.scale = 0.25
        self.man_checkbox.label.scale = 0.25

        self.woman_checkbox.label.bind(size=self.update_font_size)
        self.man_checkbox.label.bind(size=self.update_font_size)

        self.add_widget(self.woman_checkbox)
        self.add_widget(self.woman_checkbox.label)

    @staticmethod
    def update_font_size(instance, value):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size

    @staticmethod
    def on_radiobutton(instance, value):
        pass

    def check_data(self):
        return self.man_checkbox.active or self.woman_checkbox.active


class RoundedButton(Button):
    def __init__(self, color_, radius_=20, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.bind(pos=self.update_canvas, size=self.update_canvas)
        self.color_ = color_
        self.radius_ = radius_

    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.color_)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[self.radius_,])


class DropDownClasses(DropDown):
    def __init__(self, height_win, **kwargs):
        super().__init__(**kwargs)
        self.height_win = height_win
        self.max_height = .4 * height_win
        self.container.spacing = 3

        for i in range(1, 12):
            btn = RoundedButton(
                        radius_=10,
                        text=str(i),
                        size_hint_y=None,
                        height=height_win * 0.07,
                        background_color=(1, 1, 1, 0.95),
                        background_normal="",
                        color_=(.55, .51, 1),
                        bold=True,
                        font_size=height_win * 0.15)

            btn.bind(on_release=lambda btn_: self.select(btn_.text))
            btn.scale = .15
            btn.bind(size=self.update_font_size)
            self.add_widget(btn)

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size


class DropDownCity(DropDown):
    def __init__(self, height_win, **kwargs):
        super().__init__(**kwargs)
        self.height_win = height_win
        self.max_height = .4 * height_win
        self.container.spacing = 3

        for i in city_dict.keys():
            btn = RoundedButton(
                        radius_=10,
                        text=str(i),
                        size_hint_y=None,
                        height=height_win * 0.07,
                        background_color=(1, 1, 1, 0.95),
                        background_normal="",
                        color_=(.55, .51, 1),
                        bold=True,
                        font_size=height_win * 0.15)

            btn.bind(on_release=lambda btn_: self.select(btn_.text))
            btn.scale = .07
            btn.bind(size=self.update_font_size)
            self.add_widget(btn)

    @staticmethod
    def update_font_size(instance, _):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size


class NumberKeyboard(BoxLayout):
    def __init__(self, label, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 3
        self.padding = 3
        self.color = (102/255, 90/255, 225/255)
        row1 = BoxLayout(orientation="horizontal", spacing=3)
        row2 = BoxLayout(orientation="horizontal", spacing=3)
        row3 = BoxLayout(orientation="horizontal", spacing=3)
        row4 = BoxLayout(orientation="horizontal", spacing=3)

        self.btn_1 = Button(text="1",
                            background_normal="",
                            background_color=self.color,
                            bold=True)

        self.btn_2 = Button(text="2",
                            background_normal="",
                            background_color=self.color,
                            bold=True)

        self.btn_3 = Button(text="3",
                            background_normal="",
                            background_color=self.color,
                            bold=True)

        self.btn_4 = Button(text="4",
                            background_normal="",
                            background_color=self.color,
                            bold=True)

        self.btn_5 = Button(text="5",
                            background_normal="",
                            background_color=self.color,
                            bold=True)

        self.btn_6 = Button(text="6",
                            background_normal="",
                            background_color=self.color,
                            bold=True)

        self.btn_7 = Button(text="7",
                            background_normal="",
                            background_color=self.color,
                            bold=True)

        self.btn_8 = Button(text="8",
                            background_normal="",
                            background_color=self.color,
                            bold=True)

        self.btn_9 = Button(text="9",
                            background_normal="",
                            background_color=self.color,
                            bold=True)

        self.btn_delete = Button(text="DEL",
                            background_normal="",
                            background_color=self.color,
                            bold=True)

        self.btn_0 = Button(text="0",
                            background_normal="",
                            background_color=self.color,
                            bold=True)

        self.btn_enter = Button(text="OK",
                            background_normal="",
                            background_color=self.color,
                            bold=True)

        self.btn_0.bind(size=self.update_font_size)
        self.btn_1.bind(size=self.update_font_size)
        self.btn_2.bind(size=self.update_font_size)
        self.btn_3.bind(size=self.update_font_size)
        self.btn_4.bind(size=self.update_font_size)
        self.btn_5.bind(size=self.update_font_size)
        self.btn_6.bind(size=self.update_font_size)
        self.btn_7.bind(size=self.update_font_size)
        self.btn_8.bind(size=self.update_font_size)
        self.btn_9.bind(size=self.update_font_size)
        self.btn_delete.bind(size=self.update_font_size)
        self.btn_enter.bind(size=self.update_font_size)

        row1.add_widget(self.btn_1)
        row1.add_widget(self.btn_2)
        row1.add_widget(self.btn_3)

        row2.add_widget(self.btn_4)
        row2.add_widget(self.btn_5)
        row2.add_widget(self.btn_6)

        row3.add_widget(self.btn_7)
        row3.add_widget(self.btn_8)
        row3.add_widget(self.btn_9)

        row4.add_widget(self.btn_delete)
        row4.add_widget(self.btn_0)
        row4.add_widget(self.btn_enter)

        self.add_widget(row1)
        self.add_widget(row2)
        self.add_widget(row3)
        self.add_widget(row4)

    @staticmethod
    def update_font_size(instance, value):
        new_font_size = instance.width * 0.2
        instance.font_size = new_font_size


class MultiplyChoiceCheckBox(BoxLayout):
    def __init__(self, choices, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.height = 10 * len(choices)
        self.width = 250

        self.lst = []

        for choice in choices:
            layout = BoxLayout(orientation="horizontal")
            layout.cb = CheckBox()
            layout.cb.label = Label(text=str(choice),
                                    bold=True)

            layout.cb.label.bind(size=self.update_font_size)
            layout.cb.label.scale = 0.13

            layout.add_widget(layout.cb)
            layout.add_widget(layout.cb.label)

            self.lst.append(layout.cb)
            self.add_widget(layout)

    def check_data(self):
        res = 0
        for i in self.lst:
            if i.active:
                res += 1

        return 1 <= res <= 2

    def get_data(self):
        lst = []
        for i in self.lst:
            if i.active:
                lst.append(i.label.text)

        return lst

    @staticmethod
    def update_font_size(instance, value):
        new_font_size = instance.width * instance.scale
        instance.font_size = new_font_size