from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random, itertools

class PlayerBot(Bot):
    def play_round(self):

        answers =[
            "Bad",
            "San kanyang, kalungkutan ay una sa lahat, natagpuaan sa isang uri, ng pakikiramay sa kanyang nakaraa.",
            "Bad",
            "Lam mapagpakumbabang, pag aalaga at masakit na atensiyon na sumasakop, sa mga nasa kanyang kalagayan.",
            "Aks niiwas nila, ang kanilang mga mata sa kanya, o kung ang matinding kalungkutan ng kanyang pagkaba.",
            "Ipi pinipilit silang tumingin sa kanya, ito ay lamang na tumiwalag kaya hindi sumasangayon, sa isang.",
            "Pan kanyang mga aksyon, ay mga bagay ng pangangalaga sa publiko magkalas ng isang salita, mahirap ma.",
            "Pup sa isang malaking, pagpupulong siya ang taong pinagtutuunan ng lahat ng kanilang mga matta, nasa.",
            "Ang kanilang mga, hilig ay tila naghihintay na maghintay, upang matanggap ang kilusan at direkmksyon.",
            "Agk mayroon siya, sa bawat sandali, isang pagkakataon ng mga kagiliw-giliw na sangkatauhan, at sa pa.",
            "Bad",
            "Ang alituntunin na kung saan tayo ay natural na sumasang, ayon sumasang, ayono sa ating sariling pag.",
            "Ay tila magkakapareho, ng pareho a pamamagitan ng kung ipinatupad natin, a mga katulad na paghuhukom.",
            "Tungkol sa pag uugali ng ibang tao, Pinahihintulutan man, natin o hindi ayon ang pag uugali ng ibang.",
            "Tao sa naramdaman natin na, kung natin sa ating sarili ang kanyang kaso, maaari natina o hindi lubos.",
            "Na sa mga damdamino at motibo na itinuro nito at, sa parehong paraano, sinasang ayunan natin o hindi.",
            "Sumasang ayon sa aming sariling, ayon sa nadarama namin, kapag inilalagay natino ang ating sarili sa.",
            "Bad",
            "O hindi lubos na makapasok at, makisimpatiya mga damdamin at motibo, na nakakaimpluwensya dito amino.",
            "Ang aming sariling mga damdamin at motibo, hindi tayo maaaring gumawa, ng anumang paghuhusga tungkol.",
            "Bad"
            ]

        answer = answers[self.player.round_number - 1]



        if self.round_number == 1:
            yield(pages.Instrucciones)
            yield (pages.Tarea, {'text_input': answer})
        elif 1 < self.round_number < Constants.num_rounds:
            yield (pages.Tarea, {'text_input': answer})
        elif self.round_number == Constants.num_rounds:
            yield (pages.Tarea, {'text_input': answer})
            yield (pages.Resultados)

