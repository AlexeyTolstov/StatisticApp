from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout


class GenderLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"

        self.man_checkbox = CheckBox(group="gender")
        self.man_checkbox.label = Label(text="Мужской",
                                        bold=True,
                                        font_size=30)
        self.add_widget(self.man_checkbox)
        self.add_widget(self.man_checkbox.label)
        self.man_checkbox.bind(active=self.on_radiobutton)

        self.woman_checkbox = CheckBox(group="gender")
        self.woman_checkbox.label = Label(text="Женский",
                                          bold=True,
                                          font_size=30)
        self.add_widget(self.woman_checkbox)
        self.add_widget(self.woman_checkbox.label)
        self.woman_checkbox.bind(active=self.on_radiobutton)

    @staticmethod
    def on_radiobutton(instance, value):
        pass

    def check_data(self):
        return self.man_checkbox.active or self.woman_checkbox.active


class DropDownClasses(DropDown):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_height = 300
        self.container.spacing = 2
        for i in range(1, 12):
            btn = Button(text=str(i),
                         size_hint_y=None,
                         height=100,
                         background_color=(.9, .3, .3, 1),
                         background_normal="",
                         font_size=60)

            btn.bind(on_release=lambda btn_: self.select(btn_.text))
            self.add_widget(btn)


class NumberKeyboard(BoxLayout):
    def __init__(self, label, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        row1 = BoxLayout(orientation="horizontal")
        self.btn_1 = Button(text="1")
        row1.add_widget(self.btn_1)
        self.btn_2 = Button(text="2")
        row1.add_widget(self.btn_2)
        self.btn_3 = Button(text="3")
        row1.add_widget(self.btn_3)

        row2 = BoxLayout(orientation="horizontal")
        self.btn_4 = Button(text="4")
        row2.add_widget(self.btn_4)
        self.btn_5 = Button(text="5")
        row2.add_widget(self.btn_5)
        self.btn_6 = Button(text="6")
        row2.add_widget(self.btn_6)

        row3 = BoxLayout(orientation="horizontal")
        self.btn_7 = Button(text="7")
        row3.add_widget(self.btn_7)
        self.btn_8 = Button(text="8")
        row3.add_widget(self.btn_8)
        self.btn_9 = Button(text="9")
        row3.add_widget(self.btn_9)

        row4 = BoxLayout(orientation="horizontal")
        self.btn_enter = Button(text="_/")
        row4.add_widget(self.btn_enter)
        self.btn_0 = Button(text="0")
        row4.add_widget(self.btn_0)
        self.btn_delete = Button(text="DEL")
        row4.add_widget(self.btn_delete)

        self.add_widget(row1)
        self.add_widget(row2)
        self.add_widget(row3)
        self.add_widget(row4)


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
            layout.cb.label = Label(text=str(choice))

            layout.cb.label.bind(size=self.update_font_size)
            layout.cb.label.scale = 0.1

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