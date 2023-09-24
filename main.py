from kivy.app import App

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
        if value:
            print(instance.label.text)


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout()

        self.title_label = Label(text="Остановись, мама!",
                                 pos_hint={'center_x': 0.5, 'center_y': 0.9},
                                 size_hint=(0.1, 0.05),
                                 font_size=30)

        self.gender_label = Label(text="Выберите пол:",
                                  pos_hint={'center_x': 0.4,
                                            'center_y': 0.75})
        self.gender_layout = GenderLayout(
            pos_hint={'center_x': 0.5, 'center_y': 0.7})

        self.age_label = Label(text="Выберите возраст:",
                                  pos_hint={'center_x': 0.4,
                                            'center_y': 0.57})
        self.age_input = TextInput(text='15',
                                   multiline=False,
                                   font_size=30,
                                   size_hint=(.05, .07),
                                   pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.telephone_label = Label(text="Укажите телефон:",
                                  pos_hint={'center_x': 0.4,
                                            'center_y': 0.4})
        self.telephone_input = TextInput(text='+7 XXX XXX XX-XX',
                                   multiline=False,
                                   font_size=30,
                                   size_hint=(.3, .07),
                                   pos_hint={'center_x': 0.5, 'center_y': 0.32})

        self.button_next = Button(text="Далее",
                                  pos_hint={'center_x': 0.5, 'center_y': 0.2},
                                  size_hint=(0.1, 0.05))
        self.button_next.bind(on_press=self.next)

    def build(self):
        self.layout.add_widget(self.gender_layout)
        self.layout.add_widget(self.gender_label)

        self.layout.add_widget(self.age_input)
        self.layout.add_widget(self.age_label)

        self.layout.add_widget(self.telephone_input)
        self.layout.add_widget(self.telephone_label)

        self.layout.add_widget(self.button_next)
        self.layout.add_widget(self.title_label)

        return self.layout

    @staticmethod
    def next(instance):
        print("Следущая страница")


if __name__ == "__main__":
    MyApp().run()