from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="UserName"))
        self.userName = TextInput(multiline=False)
        self.add_widget(self.userName)
        self.add_widget(Label(text="Password"))
        self.passworld = TextInput(multiline=False)
        self.add_widget(self.passworld)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
