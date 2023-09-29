from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout


class GenderLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"

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
        pass

    def check_data(self):
        return self.man_checkbox.active or self.woman_checkbox.active


class NumberInput(TextInput):
    def __init__(self, type_input, **kwargs):
        super().__init__(**kwargs)
        self.multiline = False
        self.type_input = type_input
        self.halign = "center"
        if type_input == "phone":
            self.hint_text = "+7 XXX XXX XX-XX"

    def press_keyboard(self, _, value):
        if self.type_input == "age":
            if value:
                if not value.isdigit():
                    self.text = value[:-1]
                elif int(value) > 99:
                    self.text = value[:2]
        elif self.type_input == "phone":
            pass

    def check_data(self):
        if self.type_input == "age":
            if self.text:
                return True
        return False


class MultiplyChoiceCheckBox(BoxLayout):
    def __init__(self, choices, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.height = 70
        self.width = 250

        self.lst = []

        for choice in choices:
            layout = BoxLayout(orientation="horizontal")
            layout.cb = CheckBox()
            layout.cb.label = Label(text=choice)

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