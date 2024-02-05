# напиши модуль для работы с анимацией
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout

class Runner(BoxLayout):
    finished = BooleanProperty(False)
    value = NumericProperty(0)
    def __init__(self, total=10, step_time=1):
        self.total = total
        self.step_time = step_time
        self.btn = Button(text = 'Присядь!!!', size_hint = (1, 0.1), pos_hint = ('top': 1.0))
        self.animation = (Animation(pos_hint={'top': 0.1}, duration=steptime/2)
                       + Animation(pos_hint={'top': 1.0}, duration=steptime/2))
        self.add_widget(self.btn)
        super().__init__(**kwargs)

    def start(self):
        self.value = 0
        self.finished = False
        self.animation.repeat = True
        self.animation.start()

    def next(self, widget, step):
        if step == 1.0:
            self.value += 1
            if self.value > self.total:
                self.animation.repeat = False
                self.finished = True