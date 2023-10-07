from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        button = Button(text='Узнать размер окна')
        button.bind(on_release=self.on_button_click)
        return button

    def on_button_click(self, instance):
        window_width = self.root_window.width
        window_height = self.root_window.height
        print(f'Ширина окна: {window_width}, Высота окна: {window_height}')

if __name__ == '__main__':
    MyApp().run()
