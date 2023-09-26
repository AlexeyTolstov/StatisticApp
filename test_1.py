from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Это виджет, который вы хотите удалить")
        self.button = Button(text="Удалить виджет")
        self.button.bind(on_press=self.remove_widget)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        return self.layout

    def remove_widget(self, instance):
        # Удаление виджета (self.label) из родительского виджета (self.layout)
        self.layout.remove_widget(self.label)

if __name__ == '__main__':
    MyApp().run()