from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.player.round_number == 1:
            yield (pages.Intro_dados)
            yield (pages.Lanzamiento, {'reporte_numero': 5, 'reporte_pago': 10})
            yield (pages.Results_dados)
        else:
            pass
