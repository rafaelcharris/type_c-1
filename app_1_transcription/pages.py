from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instrucciones(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True
        elif self.round_number > 1:
            return False


class Tarea(Page):

    form_model = "player"
    form_fields = ["text_input"]

    def is_displayed(self):
        if self.round_number <= Constants.num_rounds:
            return True
        else:
            return False


    def vars_for_template(self):
        self.player.accumulated_variables()
        return dict(
            task_text=self.player.task_text,
            is_correct = self.player.is_correct,
            accumulated_is_correct = self.player.accumulated_is_correct
        )

    def before_next_page(self):
        self.player.check_if_correct()


class Resultados(Page):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False

    form_model = "player"

#    def vars_for_template(self):
#        return dict(
#            is_correct=self.player.is_correct
#        )

page_sequence = [
    Instrucciones,
    Tarea,
    Resultados,
]
