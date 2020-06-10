from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'type_c',
        'display_name': 'type_c',
        'num_demo_participants': 2,
        #'app_sequence': ['app_1_transcription', 'app_11_report'],
        'app_sequence': ['app_0_consent', 'app_1_transcription', 'app_2_dados', 'app_10_questionnaire',
                         'app_11_report'],
        'use_browser_bots': False,
        'time_limit': 60*4,
    },
]

# TODO: Make more salient the error form in consent.html

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 0

ROOMS = [
    {
        'name': 'Estudio',
        'display_name': 'Estudio',
    }
]
ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'e#4fre$rjqcttn)jfbwljsaq@j)mmgp(05ro*$%8#dfv(k*=)_'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
