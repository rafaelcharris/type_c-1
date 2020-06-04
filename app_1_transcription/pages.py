from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time

class Instrucciones(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True
        elif self.round_number > 1:
            return False

    def vars_for_template(self):
        return dict(
            time_limit=int(Constants.time_limit / 60)
        )

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + self.session.config['time_limit']

class Tarea(Page):

    form_model = "player"
    form_fields = ["text_input"]

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def vars_for_template(self):
        self.player.accumulated_variables()
        correct_last_round = self.colour_correct()

        return dict(
            image_path='/app_1_transcription/paragraphs/{}.png'.format(self.round_number-1),
            reference_text=Constants.text_list[self.round_number - 1], #ESTO ES PARA CORREGIR EL TEXTO
            task_text=self.player.task_text,
            is_correct=self.player.is_correct,
            accumulated_is_correct=self.player.accumulated_is_correct,
            accumulated_payoff=self.player.accumulated_payoff,
            correct_last_round=correct_last_round,
            round_count=self.player.round_number
        )

    def is_displayed(self):
        return self.participant.vars['expiry'] - time.time() > 0

    def before_next_page(self):
        self.player.check_if_correct()
        if self.round_number == Constants.num_rounds:
            self.player.accumulated_variables()
            self.player.final_payoff_calculator()

    def colour_correct(self):
        """
        This function creates a string depending on is_correct from previous rounds. Depending in the string,
        in the .html the text is painted red or green.
        """
        if self.player.round_number == 1:  # on very first task
            correct_last_round = ""
        else:  # all subsequent tasks
            if self.player.in_previous_rounds()[-1].is_correct:
                return str("correcta")
            else:
                return str("incorrecta")


class Resultados(Page):
    form_model = "player"

    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False

    def vars_for_template(self):
        table_rows = []
        for p in self.player.in_all_rounds():
            if (p.text_input is not None):
                row = dict(
                    num_ronda=p.round_number,
                    is_correct=p.is_correct,
                    task_text=p.task_text,
                    text_input=p.text_input
                )
                table_rows.append(row)
        return dict(
            table_rows=table_rows,
            accumulated_payoff=self.player.accumulated_payoff,
            final_payoff=self.player.final_payoff
        )

    def before_next_page(self):
        self.player.report_transcription()


page_sequence = [
    Instrucciones,
    Tarea,
    Resultados,
]
