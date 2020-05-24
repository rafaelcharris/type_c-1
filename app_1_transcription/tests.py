from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random, itertools

class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            yield(pages.Instrucciones)
            yield (pages.Tarea, {'text_input': "Text 1"})
        elif 1 < self.round_number <= Constants.num_rounds:
            yield(pages.Tarea, {'text_input': "Text 2"})
            yield (pages.Resultados)

