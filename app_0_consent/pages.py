from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Verification(Page):

    form_model = 'player'
    form_fields = ['id_number', 'phone', 'e_mail']

    def before_next_page(self):
        self.player.update_database()

class Bienvenido(Page):

    def before_next_page(self):
        user_agent = self.request.META['HTTP_USER_AGENT']
        is_mobile = False
        for substring in ["Mobi", "Android"]:
            if substring in user_agent:
                is_mobile = True
                self.player.is_mobile = True
            else:
                self.player.is_mobile = False
        print("fue mobile?: " + str(is_mobile))

    def is_displayed(self):
        return self.player.was_before == False

class Consent(Page):

    form_model = 'player'
    form_fields = ['name']

    def before_next_page(self):
        self.player.report_consent()


    def is_displayed(self):
        return self.player.was_before == False

class NormalWaitPage(WaitPage):
    pass

class end(Page):

    def is_displayed(self):
        return self.player.was_before == True

page_sequence = [
    Verification,
    Bienvenido,
    Consent,
    end
]
