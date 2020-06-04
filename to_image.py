from PIL import Image, ImageDraw, ImageFont

#fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
text_list = [ "Lah isang anak na lalaki, sa pagkamatay ng isang mapagpasunod at kagalang-galang ama, ay maaaring ma.",
    "San kanyang, kalungkutan ay una sa lahat,  natagpuaan sa isang uri, ng pakikiramay sa kanyang nakaraa.",
    "Yon taong mayaman, ay nagmula sa kanyang kayamanan, rsapagkat naramdaman niya na natural na nakukuha.",
    "Lam mapagpakumbabang, pag aalaga at masakit na atensiyon na sumasakop, sa mga nasa kanyang kalagayan.",
    "Aks niiwas nila, ang kanilang mga mata sa kanya, o kung ang matinding kalungkutan ng kanyang pagkaba.",
    "Ipi pinipilit silang tumingin sa kanya, ito ay lamang na tumiwalag kaya hindi sumasangayon, sa isang.",
    "Pan kanyang mga aksyon, ay mga bagay ng pangangalaga sa publiko magkalas ng isang salita, mahirap ma.",
    "Pup sa isang malaking, pagpupulong siya ang taong pinagtutuunan ng lahat ng kanilang mga matta, nasa.",
    "Ang kanilang mga, hilig ay tila naghihintay na maghintay, upang matanggap ang kilusan at direkmksyon.",
    "Agk mayroon siya, sa bawat sandali, isang pagkakataon ng mga kagiliw-giliw na sangkatauhan, at sa pa.",
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
    "Aalisin ating sarili, tulad nito, mula sa aming sariling likas na istasyon at pagsisikap na tingnano."]

for text in range(len(text_list)):
    #https://code-maven.com/create-images-with-python-pil-pillow
    img = Image.new('RGB', (1025, 55), color=(246,233,192))
    helvetica = ImageFont.truetype(font="Helvetica.ttf", size=20)
    d = ImageDraw.Draw(img)

    d.text((10, 10), text_list[text], font = helvetica, fill=(62,61,57))

    img.save("_static\\app_1_transcription\\paragraphs\\" + str(text) +".png")
