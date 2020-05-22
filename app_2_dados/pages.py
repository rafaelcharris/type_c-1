from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro_dados(Page):
    pass


class Lanzamiento(Page):

    form_model = 'player'
    form_fields = ['reporte_numero', 'reporte_pago']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results_dados(Page):
    def vars_for_template(self):
        self.player.set_payoff()
        self.player.memory_admin()


page_sequence = [
    Intro_dados,
    Lanzamiento,
    Results_dados
]
