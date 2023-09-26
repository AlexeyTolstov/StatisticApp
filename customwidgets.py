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


class MultiplyChoiceCheckBox(BoxLayout):
    def __init__(self, choices):
        super().__init__()
        self.orientation = "vertical"

        for choice in choices:
            cb = CheckBox()
            cb.label = Label(text=choice)
            self.add_widget(cb)
            self.add_widget(cb.label)