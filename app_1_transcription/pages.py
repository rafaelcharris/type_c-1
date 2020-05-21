from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instrucciones(Page):
    pass


class Tarea(Page):
    pass


class Resultados(Page):
    pass

page_sequence = [
    Instrucciones,
    Tarea,
    Resultados,
]
