from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.db import models as djmodels
from django.core.validators import EmailValidator


author = 'UEC'

doc = """
Report for experimenters to see
"""


class UnalEmailValidator(EmailValidator):
    def validate_domain_part(self, domain_part):
        if domain_part != 'unal.edu.co':
            return False
        return True
    message = "Por favor ingrese un correo con dominio @unal.edu.co"


class Constants(BaseConstants):
    name_in_url = 'app_11_report'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):

    def vars_for_admin_report(self):
        table_rows = []
        for p in self.get_players():
            row = p.participant.vars #quejesto?
            row['consent_name'] = p.participant.vars.get('consent_name')
            row['consent_id_number'] = p.participant.vars.get('consent_id_number')
            row['consent_phone'] = p.participant.vars.get('consent_phone')
            row['consent_e_mail'] = p.participant.vars.get('consent_e_mail')
            row['transcription_final_payoff'] = p.participant.vars.get('transcription_final_payoff')
            row['dados_final_payoff'] = p.participant.vars.get('dados_final_payoff')
            row['ultra_final_payoff'] = p.participant.vars.get('ultra_final_payoff')
            table_rows.append(row)
        return {'table_rows': table_rows}

    def pass_relevant_info_to_database(self):
        for p in self.get_players():
            p.name = p.participant.vars.get('consent_name')
            p.id_number = p.participant.vars.get('consent_id_number')
            p.phone = p.participant.vars.get('consent_phone')
            p.e_mail = p.participant.vars.get('consent_e_mail')
            p.payoff_transcription = p.participant.vars.get('transcription_final_payoff')
            p.payoff_dados = p.participant.vars.get('dados_final_payoff')
            p.payoff_ultra_final = p.participant.vars.get('ultra_final_payoff')
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    """
    The models here are to copy and pase the most relevant administrative variables into the oTree database for easy
    reference later on
    """
    name = models.StringField()
    id_number = models.StringField()
    phone = models.StringField() #For verification
    e_mail = models.StringField()
    payoff_transcription = models.IntegerField()
    payoff_dados = models.IntegerField()
    payoff_ultra_final = models.IntegerField()
