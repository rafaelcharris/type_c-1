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
    num_rounds = 2
    text_list = ["Text 1", "Text 2", "Text 3", "Text 4", "Text 5"]
    piece_rate = 2000


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.task_text = Constants.text_list[self.round_number - 1]
            print("[[ APP_1_TRANSCRIPTION ]] - SUBSESSION - creating_session().............ROUND NUMBER: ",
                  self.round_number)
            print("[[ APP_1_TRANSCRIPTION ]] - SUBSESSION - creating_session().............PARTICIPANT: ",
                  p) # This p is different for every round
            print("[[ APP_1_TRANSCRIPTION ]] - SUBSESSION - creating_session().............task_text: ", p.task_text)
            print("[[ APP_1_TRANSCRIPTION ]] - SUBSESSION - creating_session().............###########################")

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    task_text = models.StringField()
    text_input = models.StringField()
    is_correct = models.IntegerField()
    accumulated_is_correct = models.IntegerField()
    accumulated_payoff = models.IntegerField()

    # TODO: This function needs some refining. To control for spaces, caps and other stuff.
    def check_if_correct(self):
        if self.task_text == self.text_input:
            self.is_correct = 1
        else:
            self.is_correct = 0
        print("[[ APP_1_TRANSCRIPTION ]] - PLAYER - check_if_correct().............ROUND NUMBER: ",
              self.round_number)
        print("[[ APP_1_TRANSCRIPTION ]] - PLAYER - check_if_correct().............accumulated_is_correct: ",
              self.is_correct)

    def accumulated_variables(self):
        """
        This function counts the number of correct answers and the accumulated payoff. It depends on the round
        number. Check the self.in_all_rounds() and self.in_previous_rounds()
        """
        if self.round_number == 1:
            self.accumulated_is_correct = 0
            self.accumulated_payoff = 0
        elif 1 < self.round_number < Constants.num_rounds:
            self.accumulated_is_correct = sum(filter(None, [p.is_correct for p in self.in_previous_rounds()]))
            self.accumulated_payoff = self.accumulated_is_correct * Constants.piece_rate
        else:
            self.accumulated_is_correct = sum(filter(None, [p.is_correct for p in self.in_all_rounds()]))
            self.accumulated_payoff = self.accumulated_is_correct * Constants.piece_rate
        print("[[ APP_1_TRANSCRIPTION ]] - PLAYER - accumulated_variables().............ROUND NUMBER: ",
              self.round_number)
        print("[[ APP_1_TRANSCRIPTION ]] - PLAYER - accumulated_variables().............accumulated_is_correct: ",
              self.accumulated_is_correct)
        print("[[ APP_1_TRANSCRIPTION ]] - PLAYER - accumulated_variables().............#########################")

    def report_app_1_transcript(self):
        self.participant.vars['consent_name'] = self.name
        print("[[ APP_1_TRANSCRIPTION ]] - PLAYER - report_app_1_transcript().............ROUND NUMBER: ",
              self.round_number)
        print("[[ APP_1_TRANSCRIPTION ]] - PLAYER - report_app_1_transcript().............PVARS ARE: ",
              self.participant.vars)
