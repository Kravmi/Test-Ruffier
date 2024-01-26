# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
import instructions
import ruffier as ruf


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name = 'main_scr'))
        sm.add_widget(FirstScr(name = 'scr1'))
        sm.add_widget(SecondScr(name = 'scr2'))
        sm.add_widget(ThirdScr(name = 'scr3'))
        sm.add_widget(ResultScr(name = 'result'))
        return sm


class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        v = BoxLayout(orientation = 'vertical')
        h = BoxLayout()
        instruction = Label(text = instructions.txt_instruction)
        self.text_name = TextInput(text = 'Введите имя')
        self.age = TextInput(text = 'Введите возраст')
        start = Button(text = 'начать')
        start.on_press = self.next
        h.add_widget(self.text_name)
        h.add_widget(self.age)
        v.add_widget(instruction)
        v.add_widget(h)
        v.add_widget(start)
        self.add_widget(v)

    def next(self):
        global text_name, age
        text_name = self.text_name.text
        age = self.age.text
        print(text_name)
        print(age)
        self.manager.current = 'scr1'


class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        v = BoxLayout(orientation = 'vertical')
        txt = Label(text = instructions.txt_test1)
        self.text_input = TextInput(text = 'Введите свой пульс')
        btn = Button(text = 'Продолжить')
        btn.on_press = self.next
        v.add_widget(txt)
        v.add_widget(self.text_input)
        v.add_widget(btn)
        self.add_widget(v)

    def next(self):
        global puls1
        puls1 = int(self.text_input.text)
        print(puls1)
        self.manager.current = 'scr2'


class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        v = BoxLayout(orientation = 'vertical')
        txt = Label(text = instructions.txt_test2)
        btn = Button(text = 'Продолжить')
        btn.on_press = self.next
        v.add_widget(txt)
        v.add_widget(btn)
        self.add_widget(v)

    def next(self):
        self.manager.current = 'scr3'


class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        v = BoxLayout(orientation = 'vertical')
        h = BoxLayout()
        txt = Label(text = instructions.txt_test3)
        self.text_input1 = TextInput(text = 'Введите свой пульс после упражнений')
        self.text_input2 = TextInput(text = 'Введите свой пульс после отдыха')
        btn = Button(text = 'Продолжить')
        btn.on_press = self.next
        h.add_widget(self.text_input1)
        h.add_widget(self.text_input2)
        v.add_widget(txt)
        v.add_widget(h)
        v.add_widget(btn)
        self.add_widget(v)

    def next(self):
        global puls2, puls3
        puls2 = int(self.text_input1.text)
        puls3 = int(self.text_input2.text)
        print(puls2, puls3)
        self.manager.current = 'result'


class ResultScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.result = Label(text = "")

        self.on_enter = self.before
        self.add_widget(self.result)

    def before(self):
        self.result.text = text_name + ',' + '\n' + ruf.txt_index + str(ruf.ruffier_index(puls1, puls2, puls3))



app = MyApp()
app.run()
