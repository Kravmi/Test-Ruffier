# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
import instructions
from seconds import Seconds
import ruffier as ruf
from runner import Runner
from sits import Sits


def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

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
        age = check_int(self.age.text)
        if age == False or age < 7:
            age = 0
            self.age.text = str(age)
        else:
            self.manager.current = 'scr1'


class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.level = False
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done = self.sec_finished)
        v = BoxLayout(orientation = 'vertical')
        txt = Label(text = instructions.txt_test1)
        self.text_input = TextInput(text = 'Введите свой пульс')
        self.text_input.set_disabled(True)
        self.btn = Button(text = 'Начать')
        self.btn.on_press = self.next
        v.add_widget(txt)
        v.add_widget(self.lbl_sec)
        v.add_widget(self.text_input)
        v.add_widget(self.btn)
        self.add_widget(v)
        
    def sec_finished(self, *args):
        self.level = True
        self.text_input.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'
        

    def next(self):
        global puls1
        if self.level == False:
            self.text_input.set_disabled(True)
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            puls1 = check_int(self.text_input.text)
            if puls1 == False or puls1 <= 0:
                puls1 = 0
                self.text_input.text = str(puls1)
            else:
                self.manager.current = 'scr2'


class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bool = False
        self.run = Runner(total = 30, step_time = 1)
        self.run.bind(finished = self.run_finished)
        self.sit = Sits(30)
        v = BoxLayout(orientation = 'vertical')
        v2 = BoxLayout(orientation = 'vertical')
        h = BoxLayout()
        txt = Label(text = instructions.txt_test2)
        self.btn = Button(text = 'Начать')
        self.btn.on_press = self.next
        v2.add_widget(self.sit)
        v2.add_widget(self.run)
        h.add_widget(v2)
        v.add_widget(txt)
        v.add_widget(h)
        v.add_widget(self.btn)
        self.add_widget(v)

    def run_finished(self, *args):
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'
        self.bool = True

    def next(self):
        if self.bool == False:
            self.btn.set_disabled(True)
            self.run.start()
            self.run.bind(value = self.sit.next)
        else:
            self.manager.current = 'scr3'


class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bool = False
        self.level = 0 
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done = self.sec_finished)
        v = BoxLayout(orientation = 'vertical')
        h = BoxLayout()
        self.txt = Label(text = instructions.txt_test3)
        self.text_input1 = TextInput(text = 'Введите свой пульс после упражнений')
        self.text_input1.set_disabled(True)
        self.text_input2 = TextInput(text = 'Введите свой пульс после отдыха')
        self.text_input2.set_disabled(True)
        self.btn = Button(text = 'Продолжить')
        self.btn.on_press = self.next
        h.add_widget(self.text_input1)
        h.add_widget(self.text_input2)
        v.add_widget(self.txt)
        v.add_widget(self.lbl_sec)
        v.add_widget(h)
        v.add_widget(self.btn)
        self.add_widget(v)

    def sec_finished(self, *args):
        if self.lbl_sec.done:
            if self.level == 0:
                self.level = 1
                self.txt.text = 'Отдыхайте'
                self.lbl_sec.restart(30)
                self.text_input1.set_disabled(False)
            elif self.level == 1:
                self.level = 2
                self.txt.text = 'Считайте пульс'
                self.lbl_sec.restart(15)
            elif self.level == 2:
                self.btn.text = 'Завершить'
                self.btn.set_disabled(False)
                self.text_input2.set_disabled(False)
                self.bool = True

    def next(self):
        global puls2, puls3
        if self.bool == False:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            puls2 = check_int(self.text_input1.text)
            puls3 = check_int(self.text_input2.text)
            if puls2 == False or puls2 <= 0 or puls3 == False or puls3 <=0:
                puls2 = 0
                puls3 = 0
                self.text_input1.text = str(puls2)
                self.text_input2.text = str(puls3)
            else:
                self.manager.current = 'result'


class ResultScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.result = Label(text = "")

        self.on_enter = self.before
        self.add_widget(self.result)

    def before(self):
        self.result.text = text_name + '\n' + ruf.test(puls1, puls2, puls3, age)




app = MyApp()
app.run()
