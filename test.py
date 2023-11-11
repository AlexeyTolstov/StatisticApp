from kivy.core.window import Window
Window.size = (360, 640)
# Получить текущее разрешение экрана
screen_width = Window.width
screen_height = Window.height

print(f"Разрешение экрана: {screen_width}x{screen_height}")