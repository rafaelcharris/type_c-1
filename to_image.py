#pip install pillow
from PIL import Image, ImageDraw, ImageFont

#fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
text_list = [
    "Lah isang anak na lalakia",
    "Sa pagkamatay ng isang ma",
    "Pagpasunod at kagalanggal",
    "Ang ama ay maaaring maank",
    "Anyang kalungkutan ay una",
    "Sa lahat natagpuaan sa is",
    "Ang uri ng pakikiramay sa",
    "Kanyang nakaraa yon taong",
    "Aayaman ay nagmula sa kan",
    "Yang kayamanan rsapagkatn",
    "Aramdaman niya na natural",
    "Nakukuha lam mapagpakumba",
    "Bang pag aalaga at masaki",
    "Tna atensiyon na sumasako",
    "Sa mga nasa kanyang kalag",
    "Aayanks niiwas nila angka",
    "Hilang mga mata sa kanyao",
    "Kung ang matinding kalung",
    "Kutan ng kanyang pagkabap",
    "Pnipilit silang tumingins",
    "Kanya ito ay lamang natum",
    "Iwalag kaya hindi sumasan",
    "Gayon sa isang pan kanyan",
    "Mga aksyonay mga bagay ng",
    "Pangangalaga sa publikoma",
    "Gkalas ng isang salitamah",
    "Iirap ma pup sa isangmala",
    "King pagpupulong siya ang",
    "Taong pinagtutuunan ng la",
    "Hat ng kanilang mga matta",
    "Nasaang kanilang mga hili",
    "Gytila naghihintay na mag",
    "Hintay upang matanggap an",
    "Agg kilusan at direkmksyo",
    "Agk mayroon siya sa bawat",
    "Sandali isang pagkakataon",
    "Ng mga kagiliwgiliw nasan",
    "Kan yang sarili, ang object ng pagmamasid at kapwalpakiramdam ng bawat katawan, tungkol sa kanya wal.",
    "Ang alituntunin na kung saan tayo ay natural na sumasang, ayon sumasang, ayono sa ating sariling pag.",
    "Ay tila magkakapareho, ng pareho a pamamagitan ng kung ipinatupad natin, a mga katulad na paghuhukom.",
    "Tungkol sa pag uugali ng ibang tao, Pinahihintulutan man, natin o hindi ayon ang pag uugali ng ibang.",
    "Tao sa naramdaman natin na, kung natin sa ating sarili ang kanyang kaso, maaari natina o hindi lubos.",
    "Na sa mga damdamino at motibo na itinuro nito at, sa parehong paraano, sinasang ayunan natin o hindi.",
    "Sumasang ayon sa aming sariling, ayon sa nadarama namin, kapag inilalagay natino ang ating sarili sa.",
    "Sitwasyon tao, at tiningnan ito, tulad ng mga mata mula sa kanyang istasyon maaari nating ang maging.",
    "O hindi lubos na makapasok at, makisimpatiya mga damdamin at motibo, na nakakaimpluwensya dito amino.",
    "Ang aming sariling mga damdamin at motibo, hindi tayo maaaring gumawa, ng anumang paghuhusga tungkol.",
    "Aalisin ating sarili, tulad nito, mula sa aming sariling likas na istasyon at pagsisikap na tingnano."
]

for text in range(len(text_list)):
    #https://code-maven.com/create-images-with-python-pil-pillow
    img = Image.new('RGB', (1025, 55), color=(246,233,192))
    helvetica = ImageFont.truetype(font="Helvetica.ttf", size=20)
    d = ImageDraw.Draw(img)

    d.text((10, 10), text_list[text], font = helvetica, fill=(62,61,57))

    img.save("_static\\app_1_transcription\\paragraphs\\" + "img_" + str(text) +".png")
