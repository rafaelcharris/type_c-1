from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
#        yield pages.cuestionario_intro
        yield pages.Cuestionario, dict(sexo=random.randint(0, 2),
                                       edad=random.randint(18, 70),
                                       e_civil=random.randint(1, 4),
                                       facultad=random.choice(["Ciencias Económicas", "Ciencias Agrarias", "Artes", "Ciencias", "Enfermería",
                                          "Ciencias Humanas", "Derecho, Ciencias Políticas y Sociales", "Ingeniería", "Medicina",
                                          "Odontología", "Medicina Veterinaria y Zootécnia", "Otra"]),
                                       carrera=random.choice(["Administración de empresas", "Antropología", "Arquitectura",
                                          "Artes plasticas",
                                          "Biología", "Ciencia Política", "Ciencias de la Computación", "Cine y Televisión",
                                          "Contaduría Pública", "Derecho", "Diseño Gráfico", "Diseño Industrial", "Economía", "Enfermería",
                                          "Español y Filologia clásica", "Estadística", "Estudios Literarios",
                                          "Farmacia", "Filología e Idiomas",
                                          "Filosofía", "Fisioterapia", "Fonoaudiología", "Geografía", "Geología", "Historia", "Ingeniería Agrícola",
                                          "Ingeniería Agronómica", "Ingeniería Civil", "Ingeniería de Sistemas y Computación", "Ingeniería Eléctrica",
                                          "Ingeniería Electrónica", "Ingeniería Industrial", "Ingeniería Mecánica", " Ingeniería Mecatrónica",
                                          "Ingeniería Química", "Lingüística", "Matemáticas", "Medicina",
                                          "Medicina Veterinaria", "Música", "Nutrición y Dietética", "Odontología", "Psicología", " Química",
                                          "Sociología", "Terapía Ocupacional", "Trabajo Social", "Zootecnia", "Otra"]),
                                       veces_matriculado=random.randint(1,15),
                                       ed_padre=random.randint(1, 7),
                                       ed_madre=random.randint(1, 7),
                                       estrato=random.randint(1, 6),
                                       localidad=random.randint(0, 19),
                                       peso=random.randint(40,100),
                                       altura=random.randint(100, 220))
        yield pages.Medidas, dict(riesgo_1=random.randint(1, 5),
                                  riesgo_2=random.randint(1, 5),
                                  gasto_no_plan=random.randint(1, 4),
                                  asalto_fisico=random.randint(1, 3),
                                  asalto_fisico_numero=random.randint(1, 10),
                                  asalto_fisico_familiar=random.randint(1, 3),
                                  asalto_fisico_numero_familiar=random.randint(1, 10),
                                  confrontacion=random.randint(1, 3),
                                  confrontacion_numero=random.randint(1, 10),
                                  violencia=random.randint(1, 3),
                                  prob_atraco=random.randint(1, 5),
                                  barrio_violento=random.randint(1, 5),
                                  barrio_ayuda=random.choice(["True", "False"]),
                                  barrio_seguro=random.choice(["True", "False"]),
                                  estrato_esperado=random.randint(1, 6),
                                  elecciones=random.randint(1, 4),
                                  botella=random.randint(1, 6),
                                  self_perception_justicia=random.randint(1, 10))
