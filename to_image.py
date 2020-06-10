#pip install pillow
from PIL import Image, ImageDraw, ImageFont

#fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
text_list = [
    "Lah isang anak na lalakiarili ang o",
    "Sa pagkamatay ng isang mabject ng p",
    "Pagpasunod at kagalanggalng alitunt",
    "Ang ama ay maaaring maank agmamasid",
    "Anyang kalungkutan ay unaat kapwalp",
    "Sa lahat natagpuaan sa is akiramdam",
    "Ang uri ng pakikiramay sang bawat k",
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
    "Iwalag kaya hindi sumasanayono sa a",
    "Gayon sa isang pan kanyan paamagita",
    "Mga aksyonay mga bagay ngnaramdaman",
    "Pangangalaga sa publikoma aming sar",
    "Gkalas ng isang salitamah damdamino",
    "Iirap ma pup sa isangmala makapasok",
    "King pagpupulong siya angnatin sa a",
    "Taong pinagtutuunan ng la anng kung",
    "Hat ng kanilang mga matta ting sari",
    "Nasaang kanilang mga hiliumasang ay",
    "Gytila naghihintay na maginatupad n",
    "Hintay upang matanggap anpatin a mg",
    "Agg kilusan at direkmksyoia katulad",
    "Agk mayroon siya sa bawatna paghuhu",
    "Sandali isang pagkakatao ningpagkom",
    "Ng mga kagiliwgiliw nasa nungkol sa",
    ]

for text in range(len(text_list)):
    #https://code-maven.com/create-images-with-python-pil-pillow
    img = Image.new('RGB', (1025, 55), color=(246,233,192))
    helvetica = ImageFont.truetype(font="Helvetica.ttf", size=20)
    d = ImageDraw.Draw(img)

    d.text((10, 10), text_list[text], font = helvetica, fill=(62,61,57))

    img.save("_static\\app_1_transcription\\paragraphs\\" + "img_" + str(text) +".png")
