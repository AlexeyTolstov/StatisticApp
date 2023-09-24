from kivy.app import App

from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label

from kivy.uix.anchorlayout import AnchorLayout
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
        print(instance.label.text)


class MyApp(App):
    def __int__(self):
        self.layout = AnchorLayout()
        self.gender_layout = GenderLayout()

    def build(self):
        self.layout.add_widget(self.gender_layout)
        return self.layout


if __name__ == "__main__":
    MyApp().run()