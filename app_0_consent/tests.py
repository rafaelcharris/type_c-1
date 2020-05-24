from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random, itertools


class PlayerBot(Bot):
    names = itertools.cycle(['Alberto', 'Bolivar', 'Carlos', 'Danilo', 'Elmer', 'Facundo', 'Guillermo', 'Hernán',
                             'Idilio', 'Janice', 'Kimberly', 'Lola'])
    phones = itertools.cycle(['1234567891'])

    def play_round(self):
        yield (pages.Bienvenido)
        yield (pages.Consent, {'name': next(self.names), 'id_number': random.randint(18, 90), 'phone': next(
            self.phones)})

