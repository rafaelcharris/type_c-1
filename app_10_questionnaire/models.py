from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Rafael'

doc = """
Encuesta demográfica
"""

class Constants(BaseConstants):
    name_in_url = 'app_10_questionnaire'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

def preg_likert(label):
    return models.IntegerField(
        label = label,
        min  = 1, max = 5,
        widget=widgets.Slider,
    )
def preg_cuatro(label):
    return models.IntegerField(
        label = label,
        choices = [
            (1, 'No'),
            (2, 'Sí, una vez'),
            (3, 'Sí, más de una vez')
        ]
    )

class Player(BasePlayer):

    #is_phone = models.BooleanField()

    def phone_correct(self):
        if self.participant.vars['phone'] != self.phone2:
            print("numero incorrecto")
            self.is_phone = False
            print(self.is_phone)
        else:
            print("number ")
            self.is_phone = True
            print(self.is_phone)

    #phone2 = models.StringField(label = "Escríba su número de celular sin espacios. Ejemplo 3103312319") #tal vez toca cambiar este field

    def phone2_error_message(self, value):
        if len(str(value)) != 10:
            return "Error: el número de celular debe tener 10 dígitos"

    sexo =models.IntegerField(
        label= '¿Cuál es su sexo',
        choices =[
            (0, "Masculino"),
            (1, "Femenino"),
            (2, "Otro")
    ],
        widget = widgets.RadioSelectHorizontal
    )
    edad = models.PositiveIntegerField(
        label = '¿Cuál es su edad?',
        min = 13, max = 70
    )
    e_civil = models.IntegerField(
        choices=[
            (1, 'Soltera/o'),
            (2, 'Unión Marital de Hecho (Unión libre)'),
            (3, 'Casada/o'),
            (4, 'Viuda/o')
        ],
        verbose_name='¿Cuál es su estado civil?',
    )
    facultad = models.CharField(label = '¿ En que facultad está usted matriculado?',
                                choices =["Ciencias Económicas", "Ciencias Agrarias", "Artes","Ciencias","Enfermería",
                                          "Ciencias Humanas", "Derecho, Ciencias Políticas y Sociales", "Ingeniería", "Medicina",
                                          "Odontología", "Medicina Veterinaria y Zootécnia", "Otra"])
    carrera = models.CharField(label = '¿En que carrera está usted matriculado?',
                               choices = ["Administración de empresas", "Antropología", "Arquitectura", "Artes plásticas",
                                          "Biología", "Ciencia Política", "Ciencias de la Computación", "Cine y Televisión",
                                          "Contaduría Pública", "Derecho", "Diseño Gráfico", "Diseño Industrial", "Economía", "Enfermería",
                                          "Español y Filolofía clásica", "Estadística", "Estudios Literarios", "Farmacia", "Filología e Idiomas",
                                          "Filosofía", "Fisioterapia", "Fonoaudiología", "Geografía", "Geología", "Historia", "Ingeniería Agrícola",
                                          "Ingeniería Agronómica", "Ingeniería Civil", "Ingeniería de Sisstemas y Computación", "Ingeniería Eléctrica",
                                          "Ingeniería Electrónica", "Ingeniería Industrial", "Ingeniería Mecánica", " Ingeniería Mecatrónica",
                                          "Ingeniería Química", "Lingüística", "Matemáticas", "Medicina", "medicina Veterinaria", "Música",
                                          "Música Instrumental", "Nutrición y Dietética", "Odontología", "Psicología", " Química",
                                          "Sociología", "Terapía Ocupacional", "Trabajo Social", "Zootecnia", "Otra"])
    veces_matriculado = models.IntegerField(label = "¿Cuantas matrículas ha pagado contando la de este semestre?")
    ed_padre = models.IntegerField(
        choices=[
            (1, 'Ninguno'),
            (2, 'Primaria'),
            (3, 'Bachillerato'),
            (4, 'Algún semestre universitario, pero no graduado'),
            (5, 'Técnico'),
            (6, 'Universitario'),
            (7, 'Posgrado')
        ],
        verbose_name='¿Cuál es el nivel de educación de su padre?',
    )
    ed_madre = models.IntegerField(
        choices=[
            (1, 'Ninguno'),
            (2, 'Primaria'),
            (3, 'Bachillerato'),
            (4, 'Algún semestre universitario, pero no graduado'),
            (5, 'Técnico'),
            (6, 'Universitario'),
            (7, 'Posgrado')
        ],
        verbose_name='¿Cuál es el nivel de educación de su madre?',
    )
    estrato = models.IntegerField(
        label = "De acuerdo con las facturas de sus servicios públicos, ¿cuál es el estrato de la vivienda actual donde reside?",
        choices = [
            (1, 'Estrato 1'),
            (2, 'Estrato 2'),
            (3, 'Estrato 3'),
            (4, 'Estrato 4'),
            (5, 'Estrato 5'),
            (6, 'Estrato 6'),
        ],
        widget = widgets.RadioSelectHorizontal
    )
    ingresos = models.IntegerField(
        choices=[
            (0, 'Menos de 1 salario mínimo'),
            (1, '1 salarios mínimos'),
            (2, '2 salarios mínimos'),
            (3, '3 salarios mínimos'),
            (4, '4 salarios mínimos'),
            (5, '5 salarios mínimos'),
            (6, '6 salarios mínimos'),
            (7, 'Más de 6 salarios mínimos'),
        ],
        label = "¿Cuál es el valor aproximado de sus ingresos mensuales en Salarios Mínimos (SMMLV=COP 828,116)? "
                "(ej. 1 salario mínimo mensual, 2 SMMLV, etc.)"
    )
    localidad = models.IntegerField(
        choices=[
            (0, 'Fuera de Bogotá'),
            (1, 'Kennedy'),
            (2, 'Suba'),
            (3, 'Engativá'),
            (4, 'Ciudad Bolívar'),
            (5, 'Bosa'),
            (6, 'Usaquén'),
            (7, 'San Cristobal'),
            (8, 'Rafael Uribe'),
            (9, 'Fontibón'),
            (10, 'Usme'),
            (11, 'Puente Aranda'),
            (12, 'Barrios Unidos'),
            (13, 'Tunjuelito'),
            (14, 'Teusaquillo'),
            (15, 'Chapinero'),
            (16, 'Antonio Nariño'),
            (17, 'Santa Fe'),
            (18, 'Los Mártires'),
            (19, 'La Candelaria'),
        ],
        verbose_name='¿En que localidad usted reside?',
        #        widget=widgets.RadioSelect()
    )
    peso = models.IntegerField(label = "¿Cuál es su peso en kilogramos?")
    altura = models.IntegerField(label = "¿Cuál es su altura en centímetros?",
                                 min = 50, max = 240)
    riesgo_1 = preg_likert(label = '¿Cómo se considera usted? Normalmente ¿es usted una persona totalmente dispuesta a tomar riesgos o intenta evitar tomar riesgos? Por favor conteste usando la siguiente escala de uno a cinco, '
                                   'donde uno indica “totalmente dispuesto a tomar riesgos” y cinco '
                                   '“Totalmente contrario a tomar riesgos”. ')
    riesgo_2 = preg_likert(label = 'Normalmente ¿es usted una persona totalmente dispuesta a tomar riesgos de carácter financiero o intenta evitar tomar riesgos financieros? Por favor conteste usando la siguiente escala de uno a cinco,'
                                   ' donde uno indica “totalmente dispuesto a tomar riesgos” y cinco “Totalmente contrario a tomar riesgos”.')
    gasto_no_plan = models.IntegerField(
        label = 'Si tuviera que conseguir COP 600.000 en una semana para enfrentar un gasto no planeado, ¿qué tanta dificultad cree que tendría en conseguir el dinero?',
        choices = [
            (1, 'No tendría dificultad'),
            (2, 'Tendría alguna dificultad, pero lo conseguiría'),
            (3, 'No sé si lo conseguiría'),
            (4, 'Definitivamente no lo conseguiría')
        ]
    )
    asalto_fisico = preg_cuatro(
        label = '¿Ha sido objeto de asalto físico en los últimos doce meses?'
    )
    asalto_fisico_numero = models.IntegerField(
        label = 'Por favor, indique cuántas veces:',
        blank=True
    )
    asalto_fisico_familiar = preg_cuatro(
        label = "¿Algún familiar suyo ha sido objeto de asalto físico en los últimos doce meses?"
    )
    asalto_fisico_numero_familiar = models.IntegerField(
        label='Por favor indique cuántas veces:',
        blank = True
    )
    confrontacion = preg_cuatro(
        label = '¿Se ha encontrado en medio de una confrontación que involucre el uso de pistolas u otras armas de fuego en los últimos cinco años?'
    )
    confrontacion_numero = models.IntegerField(
        label = 'Por favor, indique cuántas veces:',
        blank = True
    )
    violencia = preg_cuatro(
        label = '¿Ha sido objeto de violencia directa (física o psicológica) en los últimos doce meses?'
    )
    prob_atraco = preg_likert(
        label = 'Cuál cree que es su probabilidad de ser víctima de un atraco en los próximos 12 meses?' 
                'Por favor conteste usando la siguiente escala de uno a cinco, donde uno indica “no muy probable” y 5 indica “muy probable”.'
    )
    barrio_violento = preg_likert(
        label = '¿Está de acuerdo con la afirmación “el barrio donde vivo es violento”?'
                'Por favor, conteste usando la siguiente escala de uno a cinco, donde uno indica “estoy totalmente en desacuerdo” y 5 indica “estoy totalmente de acuerdo”.'
    )
    barrio_ayuda = models.BooleanField(
        label = 'Si usted llegara a necesitar ayuda, ¿acudiría a alguien desconocido de su mismo barrio?'
    )
    barrio_seguro = models.BooleanField(
        label = '¿Se siente seguro mientras camina en la tarde en su barrio?'
    )
    estrato_esperado = models.IntegerField(
        label = '¿Cuál es el estrato de la vivienda donde usted espera vivir a lo largo de su vida?',
        choices = [
            (1, 'Estrato 1'),
            (2, 'Estrato 2'),
            (3, 'Estrato 3'),
            (4, 'Estrato 4'),
            (5, 'Estrato 5'),
            (6, 'Estrato 6'),
        ],
        widget = widgets.RadioSelectHorizontal
    )

    elecciones = models.IntegerField(
        label = '¿Con qué frecuencia vota en las elecciones políticas?',
        choices = [
            (1, "Nunca"),
            (2, "Raramente"),
            (3, "Casi siempre"),
            (4, "Todas las veces")
        ],
        widget= widgets.RadioSelectHorizontal
    )
    botella = models.IntegerField(
        label = 'Imagine la siguiente situación: usted está de compras en una ciudad que no es familiar para usted y se da cuenta de que perdió el camino. Usted decide preguntarle a un extraño por indicaciones. El extraño ofrece llevarlo en su carro al destino que usted tenía. El viaje dura cerca de 20 minutos y le cuesta al extraño 20.000 pesos. El extraño no desea dinero por haberlo llevado. Usted lleva seis botellas de vino con usted. La botella más barata cuesta 5.000 pesos, la botella más cara cuesta 30.000 pesos. '
                'Usted decide darle una de sus botellas al extraño como agradecimiento por el favor. ¿Cuál botella le daría?', #separar las preguntas para que sea más fácil de leer
        choices = [
            (1, 'Botella de 5.000 pesos'),
            (2, 'Botella de 10.000 pesos'),
            (3, 'Botella de 15.000 pesos'),
            (4, 'Botella de 20.000 pesos'),
            (5, 'Botella de 25.000 pesos'),
            (6, 'Botella de 30.000 pesos')],
        widget=widgets.RadioSelect
    )
    self_perception_justicia = models.IntegerField(
        label = '¿Cómo se ve a usted mismo? ¿Es una persona que generalmente está dispuesta a castigar comportamientos injustos, incluso, si esto es costoso para usted?'
                'Por favor use una escala de 0 a 10, donde 0 significa que usted “no está dispuesto a incurrir en costos para castigar comportamientos injustos” y 10 significa que usted “está muy dispuesto a incurrir en costos para castigar comportamientos injustos”. '
                'También puede usar los valores intermedios para indicar dónde se encuentra en la escala.',
        min = 1,
        max = 10,
        widget= widgets.Slider #todo agregar otra función para el step?
    )

    impuesto = preg_likert(
        label = "¿Qué tan de acuerdo está con que el Gobierno tenga que reducir las diferencias entre ricos y pobres, de pronto subiendo los impuestos para los ricos o proveyendo asistencia a los ingresos de los más pobres?"
                " Por favor, indique que tan de acuerdo está marcando un número de uno a cinco en la escala de abajo, donde uno indica “estoy totalmente en desacuerdo” y cinco indica “estoy totalmente de acuerdo”."
                                   )
    #