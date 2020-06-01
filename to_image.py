from PIL import Image, ImageDraw, ImageFont

#fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
text_list = [ "lah isang anak na lalaki, sa pagkamatay ng isang mapagpasunod at kagalang-galang ama, ay maaaring ma.",
    "san kanyang, kalungkutan ay una sa lahat, natagpuaan sa isang uri, ng pakikiramay sa kanyang nakaraa.",
    "yon taong mayaman, ay nagmula sa kanyang kayamanan, rsapagkat naramdaman niya na natural na nakukuha.",
    "lam mapagpakumbabang, pag-aalaga at masakit na atensiyon na sumasakop, sa mga nasa kanyang kalagayan.",
    "aks niiwas nila, ang kanilang mga mata sa kanya, o kung ang matinding kalungkutan ng kanyang pagkaba.",
    "ipi pinipilit silang tumingin sa kanya, ito ay lamang na tumiwalag kaya hindi sumasangayon, sa isang.",
    "pan kanyang mga aksyon, ay mga bagay ng pangangalaga sa publiko magkalas ng isang salita, mahirap ma.",
    "pup sa isang malaking, pagpupulong siya ang taong pinagtutuunan ng lahat ng kanilang mga matta, nasa.",
    "ang kanilang mga, hilig ay tila naghihintay na maghintay, upang matanggap ang kilusan at direkmksyon.",
    "agk mayroon siya, sa bawat sandali, isang pagkakataon ng mga kagiliw-giliw na sangkatauhan, at sa pa.",
    "kan yang sarili, ang object ng pagmamasid at kapwalpakiramdam ng bawat katawan, tungkol sa kanya wal."]

for text in range(len(text_list)):
    img = Image.new('RGB', (775, 30), color=(73, 109, 137))

    d = ImageDraw.Draw(img)

    d.text((10, 10), text_list[text], fill=(255, 255, 0))

    img.save("app_1_transcription\\paragraphs\\image" + str(text) +".png")
