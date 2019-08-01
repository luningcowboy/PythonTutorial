from random import random

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line


class PaintScreen(Widget):
    def on_touch_down(self, touch):
        color = (random(), random(), random())
        with self.canvas:
            Color(*color)
            d = 30
            Ellipse(pos=(touch.x - d / 2, touch.y - d/2),size=(d,d))
            touch.ud['line'] = Line(points=(touch.x,touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class MyApp(App):
    def build(self):
        return PaintScreen()

if __name__ == '__main__':
    MyApp().run()
