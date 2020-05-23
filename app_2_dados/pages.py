from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro_dados(Page):
    #TODO: Ask or decide when to show results and how many results.
    #TODO: Add a function called money_payoff that converts UMEs to pesos for each app and then sums them up at the end.
    pass


class Lanzamiento(Page):

    form_model = 'player'
    form_fields = ['reporte_numero', 'reporte_pago']
    def before_next_page(self):
        self.player.set_payoff()


class Results_dados(Page):
    pass


page_sequence = [
    Intro_dados,
    Lanzamiento,
    Results_dados
]
