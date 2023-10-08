from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class ResizableFontLabelApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Привет, мир!', font_size='20sp')
        layout.add_widget(label)
        label.bind(size=self.update_font_size)
        return layout

    def update_font_size(self, instance, value):
        new_font_size = 0.15 * instance.width
        instance.font_size = new_font_size

if __name__ == '__main__':
    ResizableFontLabelApp().run()
