from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Felipe Montealegre'

doc = """
app_2_dados
"""


class Constants(BaseConstants):
    name_in_url = 'app_2_dados'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    reporte_numero = models.IntegerField(
        choices=[
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
        ],
        verbose_name='Por favor seleccione el número de su primer lanzamiento del dado en el siguiente cuadro:',
    )

    reporte_pago = models.IntegerField(
        choices=[
            (2, '2 UME'),
            (4, '4 UME'),
            (6, '6 UME'),
            (8, '8 UME'),
            (10, '10 UME'),
            (0, '0 UME'),
        ],
        verbose_name='Ahora por favor seleccione su pago de acuerdo a la tabla anterior en el siguiente cuadro:',
    )

    total_payoff = models.IntegerField()

    def set_payoff(self):
        if self.reporte_numero == 1:
            self.total_payoff = 2
        elif self.reporte_numero == 2:
            self.total_payoff = 4
        elif self.reporte_numero == 3:
            self.total_payoff = 6
        elif self.reporte_numero == 4:
            self.total_payoff = 8
        elif self.reporte_numero == 5:
            self.total_payoff = 10
        elif self.reporte_numero == 6:
            self.total_payoff = 0

        self.payoff = self.total_payoff
        print("[[ DADOS ]] - PLAYER - SET_PAYOFF.............TOTAL_PAYOFF IS", self.total_payoff)
        print("[[ DADOS ]] - PLAYER - SET_PAYOFF.............PAYOFF IS", self.payoff)

    def memory_admin(self):
        self.participant.vars['dados_reporte_numero'] = self.reporte_numero
        self.participant.vars['dados_payoff'] = self.total_payoff
        print("[[ DADOS ]] - PLAYER - DADOS_ADMIN.............ROUND NUMBER", self.round_number)
        print("[[ DADOS ]] - PLAYER - DADOS_ADMIN.............PVARS ARE", self.participant.vars)
