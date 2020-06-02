from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
#For atuhentication with the spreadsheet
import gspread
from oauth2client.service_account import ServiceAccountCredentials

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'app_0_consent'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    name = models.StringField()
    id_number = models.IntegerField()
    phone = models.IntegerField()

    # Esta función me permite verificar si un form cumple con los requisitos especificados en ella. Para hacerlo,
    # solo necesito agregar {{ form.phone.errors }} en la template para que haga su magia.
    def phone_error_message(self, value):
        if len(str(value)) != 10:
            return "Error: el número de celular debe tener 10 dígitos."

    def report_consent(self):
        self.participant.vars['consent_name'] = self.name
        self.participant.vars['consent_id_number'] = self.id_number
        self.participant.vars['consent_phone'] = self.phone
        print("[[ APP_0_CONSENT ]] - PLAYER - report_consent.............ROUND NUMBER", self.round_number)
        print("[[ APP_0_CONSENT ]] - PLAYER - report_consent.............PVARS ARE", self.participant.vars)

    ######################################################
    #This is for the interaction with the google API
    # use creds to create a client to interact with the Google Drive API
    def update_database(self):
        """
        Update la spreadsheet con la id y el número de telefono del participante
        :return: Boolean
        """
        gc = gspread.service_account(filename="client_secret.json")

        sh = gc.open("type c participation")

        sheet = sh.get_worksheet(0)
        list_of_hashes = sheet.get_all_records()
        print(list_of_hashes)
        sheet.update("A3", self.id_number)