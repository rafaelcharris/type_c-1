from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
#For atuhentication with the spreadsheet
import gspread
import pandas as pd
from django.core.validators import EmailValidator
from django.db import models as djmodels

author = 'Your name here'

doc = """
Your app description
"""
class UnalEmailValidator(EmailValidator):
    def validate_domain_part(self, domain_part):
        if domain_part != 'unal.edu.co':
            return False
        return True
    message = "Por favor ingrese un correo con dominio @unal.edu.co"


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
    id_number = models.StringField()
    phone = models.StringField()
    was_before = models.BooleanField()
    e_mail = djmodels.EmailField(validators=[UnalEmailValidator()])

    is_mobile = models.BooleanField()

    # Esta función me permite verificar si un form cumple con los requisitos especificados en ella. Para hacerlo,
    # solo necesito agregar {{ form.phone.errors }} en la template para que haga su magia.
    def phone_error_message(self, value):
        if len(str(value)) != 10:
            return "Error: el número de celular debe tener 10 dígitos."

        try:
            int(value)
        except ValueError:
            return "Error: el teléfono tiene carácteres no númericos"

    def id_number_error_message(self, value):
        try:
            int(value)
        except ValueError:
            return "Error: el documento de identidad tiene carácteres no númericos"

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
        sheet_values = sheet.get_all_values()

        df_sheet = pd.DataFrame.from_records(sheet_values)
        print(df_sheet.values)
        print(self.id_number)
        # toca convertir los valores en strings para que se pueda hacer bien la comparación con valores
        if str(self.id_number) in df_sheet.values or str(self.phone) in df_sheet.values:
            print("este valor ya está. no lo puede agregar")
            print(df_sheet.values)
            self.was_before = True
        else:
            #Add into to these two columns
            print("updated value en la fila {}".format(len(df_sheet)))
            #Esto consigue el length del data set y le agrega un valor nuebo.
            for_format = len(df_sheet) + 1
            sheet.update("A{}:C{}".format(for_format,for_format, for_format), [[self.id_number, self.phone, str(self.e_mail)]])
            self.was_before = False
