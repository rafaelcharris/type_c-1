from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random, itertools


class PlayerBot(Bot):
    names = itertools.cycle(['Alberto', 'Bolivar', 'Carlos', 'Danilo', 'Elmer', 'Facundo', 'Guillermo', 'Hernán',
                             'Idilio', 'Janice', 'Kimberly', 'Lola'])
    phones = random.sample(range(10),10)
    phones = "".join(str(num) for num in phones)
    def play_round(self):
        yield (pages.Verification, {'id_number': random.randint(18, 90), 'e_mail': "bot" + str(random.randint(1,100)) + "@unal.edu.co" , 'phone':
            self.phones})
        yield (pages.Bienvenido)
        yield (pages.Consent, {'name': next(self.names)})

