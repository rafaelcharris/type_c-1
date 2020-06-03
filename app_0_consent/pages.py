from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Bienvenido(Page):
    pass


class Consent(Page):

    form_model = 'player'
    form_fields = ['name', 'id_number', 'phone']

    def before_next_page(self):
        self.player.report_consent()
        self.player.update_database()
        self.player.identify_device()

class NormalWaitPage(WaitPage):
    pass

class end(Page):

    def is_displayed(self):
        return self.player.was_before == True

page_sequence = [
    Bienvenido,
    Consent,
    end
]
