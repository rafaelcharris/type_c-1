from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instrucciones(Page):
    pass


class Tarea(Page):

    form_model = "player"
    form_fields = ["text_input"]

    def vars_for_template(self):
        return dict(
            task_text=self.player.task_text
        )


class Resultados(Page):
    pass

page_sequence = [
    Instrucciones,
    Tarea,
    Resultados,
]
