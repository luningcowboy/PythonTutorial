from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        s = Scatter()
        l = Label(text='Scatter', font_size=100)
        s.add_widget(l)
        return s

if __name__ == '__main__':
    MyApp().run()
