from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton


class RadioButtonApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Создаем группу радиокнопок
        radio_group = []

        for i in range(3):
            radio_button = ToggleButton(text=f'Option {i + 1}', group='options')
            radio_button.bind(on_press=self.on_radio_button_press)
            radio_group.append(radio_button)
            layout.add_widget(radio_button)

        self.result_label = Label(text="Выбрана опция: None")
        layout.add_widget(self.result_label)

        return layout

    def on_radio_button_press(self, instance):
        self.result_label.text = f"Выбрана опция: {instance.text}"


if __name__ == '__main__':
    RadioButtonApp().run()
