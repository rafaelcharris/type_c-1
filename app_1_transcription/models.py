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
    text_list = [
    "Lah isang anak na lalakiarili angpo",
    "Sa pagkamatay ng isang mabject ngpp",
    "Pagpasunod at kagalanggalng alitunt",
    "Ang ama ay maaaring maank agmamasid",
    "Anyang kalungkutan ay unaat kapwalp",
    "Sa lahat natagpuaan sa is akiramdam",
    "Ang uri ng pakikiramay sang bawatlk",
    "Kanyang nakaraa yon taongatawa tung",
    "Aayaman ay nagmula sa kankol sa kan",
    "Yang kayamanan rsapagkatnunin na ku",
    "Aramdaman niya na naturalng saan ta",
    "Nakukuha lam mapagpakumbayo ay natu",
    "Bang pag aalaga at masakiral na sum",
    "Tna atensiyon na sumasakoasang ayon",
    "Sa mga nasa kanyang kalagy tila mag",
    "Aayanks niiwas nila angka kakapareh",
    "Hilang mga mata sa kanyao ng pareho",
    "Kung ang matinding kalung sumasangr",
    "Kutan ng kanyang pagkabapa pamamagi",
    "Pnipilit silang tuminginsayono sapa",
    "Kanya ito ay lamang natumya walieud",
    "Iwalag kaya hindi sumasanayono sata",
    "Gayon sa isang pan kanyan paamagita",
    "Mga aksyonay mga bagay ngnaramdaman",
    "Pangangalaga sa publikoma aming sar",
    "Gkalas ng isang salitamah damdamino",
    "Iirap ma pup sa isangmala makapasok",
    "King pagpupulong siya angnatin saka",
    "Taong pinagtutuunan ng la anng kung",
    "Hat ng kanilang mga matta ting sari",
    "Nasaang kanilang mga hiliumasang ay",
    "Gytila naghihintay na maginatupadin",
    "Hintay upang matanggap anpatin a mg",
    "Agg kilusan at direkmksyoia katulad",
    "Agk mayroon siya sa bawatna paghuhu",
    "Sandali isang pagkakatao ningpagkom",
    "Ng mga kagiliwgiliw nasa nungkol sa",
#    "pag uugali ng ibang tao Pinahihintulutan man natin o hindi ayon ang pag uugali ng ibang",
#    "ao sa  natin na kung natin sa ating sarili ang kanyang kaso maaari natina o hindi lubos",
#    "a sa mga damdamino at motibo na itinuro nito at sa parehong paraano sinasang ayunan natin o hindi",
#    "on sa aming sariling ayon sa nadarama namin kapag inilalagay natino ang ating sarili sa",
#    "itwasyon tao at tiningnan ito tulad ng mga mata mula sa kanyang istasyon maaari nating ang maging",
#    "ndi lubos na makapasok at makisimpatiya mga damdamin at motibo na nakakaimpluwensya dito amino",
#    "ng aming sariling mga damdamin at motibo hindi tayo maaaring gumawa ng anumang paghuhusga tungkol",
#    "alisin ating sarili tulad nito mula sa aming sariling likas na istasyon at pagsisikap na tingnano"
    ]

    num_rounds = len(text_list)
    treatments = [0, 1]
    shock = 0.2
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
