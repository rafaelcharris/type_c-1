from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'app_1_transcription'
    players_per_group = None
    num_rounds = 1
    text_list = ["Text 1", "Text 2", "Text 3", "Text 4", "Text 5"]


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.task_text = Constants.text_list[1]



class Group(BaseGroup):
    pass


class Player(BasePlayer):

    task_text = models.StringField()
    text_input = models.StringField()

    def report_app_1_transcript(self):
        self.participant.vars['consent_name'] = self.name
        print("[[ APP_0_CONSENT ]] - PLAYER - CONSENT_ADMIN.............ROUND NUMBER", self.round_number)
        print("[[ APP_0_CONSENT ]] - PLAYER - CONSENT_ADMIN.............PVARS ARE", self.participant.vars)
