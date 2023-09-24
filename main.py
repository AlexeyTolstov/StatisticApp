from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.radiobutton import BoxLayout


class MyApp(App):
    def build(self):
        self.layout = AnchorLayout()

        self.gender_layout = BoxLayout(orientation="horizontal")

        self.man_checkbox = CheckBox()
        self.man_label = Label(text="Мужской")
        self.gender_layout.add_widget(self.man_checkbox)
        self.gender_layout.add_widget(self.man_label)

        radio_button.bind(on_press=self.on_radio_button_press)

        self.woman_checkbox = CheckBox()
        self.woman_label = Label(text="Женский")
        self.gender_layout.add_widget(self.woman_checkbox)
        self.gender_layout.add_widget(self.woman_label)

        self.layout.add_widget(self.gender_layout)
        return self.layout


if __name__ == "__main__":
    MyApp().run()