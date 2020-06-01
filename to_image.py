from PIL import Image, ImageDraw, ImageFont

#fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
text_list = [ "lah isang anak na lalaki, sa pagkamatay ng isang \n\nmapagpasunod at kagalang-galang ama, ay maaaring ma.",
    "san kanyang, kalungkutan ay una sa lahat, \n\n natagpuaan sa isang uri, ng pakikiramay sa kanyang nakaraa.",
    "yon taong mayaman, ay nagmula sa kanyang \n\nkayamanan, rsapagkat naramdaman niya na natural na nakukuha.",
    "lam mapagpakumbabang, pag-aalaga at masakit na\n\n atensiyon na sumasakop, sa mga nasa kanyang kalagayan.",
    "aks niiwas nila, ang kanilang mga mata sa kanya,\n\n o kung ang matinding kalungkutan ng kanyang pagkaba.",
    "ipi pinipilit silang tumingin sa kanya, ito ay\n\n lamang na tumiwalag kaya hindi sumasangayon, sa isang.",
    "pan kanyang mga aksyon, ay mga bagay ng pangangalaga\n\n sa publiko magkalas ng isang salita, mahirap ma.",
    "pup sa isang malaking, pagpupulong siya ang taong\n\n pinagtutuunan ng lahat ng kanilang mga matta, nasa.",
    "ang kanilang mga, hilig ay tila naghihintay na maghintay,\n\n upang matanggap ang kilusan at direkmksyon.",
    "agk mayroon siya, sa bawat sandali, isang pagkakataon\n\n ng mga kagiliw-giliw na sangkatauhan, at sa pa.",
    "kan yang sarili, ang object ng pagmamasid at kapwalpakiramdam\n\n ng bawat katawan, tungkol sa kanya wal."]

for text in range(len(text_list)):
    #https://code-maven.com/create-images-with-python-pil-pillow
    img = Image.new('RGB', (810, 125), color=(211,211,211))
    helvetica = ImageFont.truetype(font="Helvetica.ttf", size=30)
    d = ImageDraw.Draw(img)

    d.text((10, 10), text_list[text], font = helvetica, fill=(0,0,0))

    img.save("_static\\app_1_transcription\\paragraphs\\" + str(text) +".png")
