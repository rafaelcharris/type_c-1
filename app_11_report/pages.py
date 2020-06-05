from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class AdminReport(Page):
    def is_displayed(self):
        return False


#class app_9_report_summary(Page):
#    def vars_for_template(self):
#        self.player.push_vars_to_report_summary()


class the_end(Page):

    def vars_for_template(self):
        self.subsession.pass_relevant_info_to_database()


page_sequence = [
    the_end
]
