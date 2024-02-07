# напиши модуль для подсчета количества приседаний
from kivy.uix.label import Label
from kivy.clock import Clock


class Sits(Label):
    
    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        text_ = f'Осталось приседаний {self.total}'
        super().__init__(text = text_, **kwargs)

    def next(self, *args):
        self.current += 1
        result = max(0, self.total - self.current)
        self.text = 'Осталось приседаний' + str(result)