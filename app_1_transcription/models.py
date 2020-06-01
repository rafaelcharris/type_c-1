from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random, itertools


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'app_1_transcription'
    players_per_group = None
    num_rounds = 2
    text_list = [ "lah isang anak na lalaki, sa pagkamatay ng isang mapagpasunod at kagalang-galang ama, ay maaaring ma.",
    "san kanyang, kalungkutan ay una sa lahat, natagpuaan sa isang uri, ng pakikiramay sa kanyang nakaraa.",
    "yon taong mayaman, ay nagmula sa kanyang kayamanan, rsapagkat naramdaman niya na natural na nakukuha.",
    "lam mapagpakumbabang, pag-aalaga at masakit na atensiyon na sumasakop, sa mga nasa kanyang kalagayan.",
    "aks niiwas nila, ang kanilang mga mata sa kanya, o kung ang matinding kalungkutan ng kanyang pagkaba.",
    "ipi pinipilit silang tumingin sa kanya, ito ay lamang na tumiwalag kaya hindi sumasangayon, sa isang.",
    "pan kanyang mga aksyon, ay mga bagay ng pangangalaga sa publiko magkalas ng isang salita, mahirap ma.",
    "pup sa isang malaking, pagpupulong siya ang taong pinagtutuunan ng lahat ng kanilang mga matta, nasa.",
    "ang kanilang mga, hilig ay tila naghihintay na maghintay, upang matanggap ang kilusan at direkmksyon.",
    "agk mayroon siya, sa bawat sandali, isang pagkakataon ng mga kagiliw-giliw na sangkatauhan, at sa pa.",
    "kan yang sarili, ang object ng pagmamasid at kapwalpakiramdam ng bawat katawan, tungkol sa kanya wal."]
    treatments = [0, 1]
    shock = 0.2
    time_limit = 60*4
    piece_rate = 1
    shock_for_instructions = str(int((1-shock)*100)) + "%"
    # Session wide constants (to be copied and pasted in each models.py)
    cop_per_ume = 2000
    currency = "UME"

    #TODO: Pilot with the UEC the number of text they can write and adjust to match average from Sumas
class Subsession(BaseSubsession):
    def creating_session(self):
        """
        This function (otree native) runs at the beginning of the session and for all rounds of the session.
        """
        self.generate_text_lists()
        self.generate_treatments()

    def generate_text_lists(self):
        """
        This function generates the texts to be added to each participant for each round.
        """
        for p in self.get_players():
            p.task_text = Constants.text_list[self.round_number - 1]
            print("[[ APP_1_TRANSCRIPTION ]] - SUBSESSION - generate_text_lists().............round_number: ",
                  self.round_number)
            print("[[ APP_1_TRANSCRIPTION ]] - SUBSESSION - generate_text_lists().............participant: ",
                  p) # This p is different for every round
            print("[[ APP_1_TRANSCRIPTION ]] - SUBSESSION - generate_text_lists().............task_text: ", p.task_text)
            print("[[ APP_1_TRANSCRIPTION ]] - SUBSESSION - generate_text_lists().............########################")

    def generate_treatments(self):
        """
        This function assigns treatment values to the participants using itertools.cycle
        """
        treatment = itertools.cycle(Constants.treatments)
        for p in self.get_players():
            p.treatment = next(treatment)
            print("[[ APP_1_TRANSCRIPTION ]] - SUBSESSION - generate_treatments().............round_number: ",
                  self.round_number)
            print("[[ APP_1_TRANSCRIPTION ]] - SUBSESSION - generate_treatments().............participant: ",
                  p) # This p is different for every round
            print("[[ APP_1_TRANSCRIPTION ]] - SUBSESSION - generate_treatments().............treatment: ",
                  p.treatment)
            print("[[ APP_1_TRANSCRIPTION ]] - SUBSESSION - generate_treatments().............########################")

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    task_text = models.StringField()
    treatment = models.IntegerField()
    text_input = models.StringField()
    is_correct = models.IntegerField()
    accumulated_is_correct = models.IntegerField()
    accumulated_payoff = models.IntegerField()
    final_payoff = models.IntegerField()

    def check_if_correct(self):
        """
        This function calculates if the text in Constants is the same as the user inputted text.
        """
        if self.task_text == self.text_input:
            self.is_correct = 1
        else:
            self.is_correct = 0
        print("[[ APP_1_TRANSCRIPTION ]] - PLAYER - check_if_correct().............round_number: ",
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
            self.accumulated_payoff = int(self.accumulated_is_correct * Constants.piece_rate)
        else:
            self.accumulated_is_correct = sum(filter(None, [p.is_correct for p in self.in_all_rounds()]))
            self.accumulated_payoff = int(self.accumulated_is_correct * Constants.piece_rate)
        print("[[ APP_1_TRANSCRIPTION ]] - PLAYER - accumulated_variables().............round_number: ",
              self.round_number)
        print("[[ APP_1_TRANSCRIPTION ]] - PLAYER - accumulated_variables().............accumulated_is_correct: ",
              self.accumulated_is_correct)
        print("[[ APP_1_TRANSCRIPTION ]] - PLAYER - accumulated_variables().............#########################")

    def final_payoff_calculator(self):
        """
        This function affects accumulated_payoff from the very last round depending on treatment and on
        Constants.shock. Besides, it converts UME into pesos.
        """
        if self.treatment == 1:
            self.final_payoff = int(self.accumulated_payoff * Constants.shock * Constants.cop_per_ume)
        elif self.treatment == 0:
            self.final_payoff = self.accumulated_payoff * Constants.cop_per_ume
        print("[[ APP_1_TRANSCRIPTION ]] - PLAYER - final_payoff().............round_number: ",self.round_number)
        print("[[ APP_1_TRANSCRIPTION ]] - PLAYER - final_payoff().............final_payoff: ",self.final_payoff)
        print("[[ APP_1_TRANSCRIPTION ]] - PLAYER - final_payoff().............treatment: ",self.treatment)

    def report_transcription(self):
        """
        This function passes key information from each app to participant.vars so report can access it.
        """
        self.participant.vars['transcription_final_payoff'] = self.final_payoff
        print("[[ APP_1_TRANSCRIPTION ]] - PLAYER - report_transcription.............ROUND NUMBER", self.round_number)
        print("[[ APP_1_TRANSCRIPTION ]] - PLAYER - report_transcription.............PVARS ARE", self.participant.vars)
