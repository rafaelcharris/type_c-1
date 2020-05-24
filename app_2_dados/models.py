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
    die_numbers = [1, 2, 3, 4, 5, 6]
    numbers_payoffs = [2, 4, 6, 8, 10, 0]
    # Session wide constants (to be copied and pasted in each models.py)
    cop_per_ume = 2000
    currency = "UME"



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    reporte_numero = models.IntegerField(
        #choices shows to the user the right-hand side and stores in the model the left-hand side.
        choices=[
            (Constants.die_numbers[0], str(Constants.die_numbers[0])),
            (Constants.die_numbers[1], str(Constants.die_numbers[1])),
            (Constants.die_numbers[2], str(Constants.die_numbers[2])),
            (Constants.die_numbers[3], str(Constants.die_numbers[3])),
            (Constants.die_numbers[4], str(Constants.die_numbers[4])),
            (Constants.die_numbers[5], str(Constants.die_numbers[5])),
        ],
        verbose_name='Por favor seleccione el número de su primer lanzamiento del dado en el siguiente cuadro:',
    )

    reporte_pago = models.IntegerField(
        choices=[
            (Constants.numbers_payoffs[0], str(Constants.numbers_payoffs[0]) + " " + Constants.currency),
            (Constants.numbers_payoffs[1], str(Constants.numbers_payoffs[1]) + " " + Constants.currency),
            (Constants.numbers_payoffs[2], str(Constants.numbers_payoffs[2]) + " " + Constants.currency),
            (Constants.numbers_payoffs[3], str(Constants.numbers_payoffs[3]) + " " + Constants.currency),
            (Constants.numbers_payoffs[4], str(Constants.numbers_payoffs[4]) + " " + Constants.currency),
            (Constants.numbers_payoffs[5], str(Constants.numbers_payoffs[5]) + " " + Constants.currency),
        ],
        verbose_name='Ahora por favor seleccione su pago de acuerdo a la tabla anterior en el siguiente cuadro:',
    )

    total_payoff = models.IntegerField()
    #TODO: There´s got to be an easier way to write this. Perhaps with aditional parameters or a dictionary?
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

    def report_dados(self):
        self.participant.vars['dados_total_payoff'] = self.total_payoff
        print("[[ APP_2_DADOS ]] - PLAYER - report_dados.............ROUND NUMBER", self.round_number)
        print("[[ APP_2_DADOS ]] - PLAYER - report_dados.............PVARS ARE", self.participant.vars)

