from playfairdeneme import create_playfair_alphabet

def metni_parcala(metin, boyut=2):
    parcalar = []
    i = 0
    while i < len(metin):
        parca = metin[i:i+boyut]
        if len(parca) == 1:
            parca += 'A'  # Tek harf kalırsa A ekleyin
        elif parca[0] == parca[1]:
            parca = parca[0] + 'A'  # Aynı harf varsa araya A ekleyin
            i -= 1
        parcalar.append(parca)
        i += boyut
    return parcalar

def playfair_sifrele(metin, anahtar):
    metin = metin.upper() # replace sildik.
    alfabe = create_playfair_alphabet(anahtar)
    kare = [alfabe[i:i+6] for i in range(0, len(alfabe), 6)]

    def konum_bul(harf):
        for satir in range(6):
            for sutun in range(6):
                if kare[satir][sutun] == harf:
                    return satir, sutun
        return None
    parcalar = metni_parcala(metin)
    sifreli_metin = ""

    for parca in parcalar:
        satir1, sutun1 = konum_bul(parca[0])
        satir2, sutun2 = konum_bul(parca[1])

        if satir1 is None or satir2 is None:
            raise ValueError(f"Karakter tablosunda bulunamadı: {parca[0]} veya {parca[1]}")

        if satir1 == satir2:
            sifreli_metin += kare[satir1][(sutun1 + 1) % 6] + kare[satir2][(sutun2 + 1) % 6]
        elif sutun1 == sutun2:
            sifreli_metin += kare[(satir1 + 1) % 6][sutun1] + kare[(satir2 + 1) % 6][sutun2]
        else:
            sifreli_metin += kare[satir1][sutun2] + kare[satir2][sutun1]

    return sifreli_metin
#Deşifreleme kısmı
def playfair_desifrele(sifreli_metin, anahtar):
    sifreli_metin = sifreli_metin.upper().replace("J", "I")
    alfabe = create_playfair_alphabet(anahtar)
    kare = [alfabe[i:i+6] for i in range(0, len(alfabe), 6)]

    def konum_bul(harf):
        for satir in range(6):
            for sutun in range(6):
                if kare[satir][sutun] == harf:
                    return satir, sutun
        return None

    parcalar = [sifreli_metin[i:i+2] for i in range(0, len(sifreli_metin), 2)]
    desifreli_metin = ""

    for parca in parcalar:
        satir1, sutun1 = konum_bul(parca[0])
        satir2, sutun2 = konum_bul(parca[1])

        if satir1 is None or satir2 is None:
            raise ValueError(f"Karakter tablosunda bulunamadı: {parca[0]} veya {parca[1]}")

        if satir1 == satir2:
            desifreli_metin += kare[satir1][(sutun1 - 1) % 6] + kare[satir2][(sutun2 - 1) % 6]
        elif sutun1 == sutun2:
            desifreli_metin += kare[(satir1 - 1) % 6][sutun1] + kare[(satir2 - 1) % 6][sutun2]
        else:
            desifreli_metin += kare[satir1][sutun2] + kare[satir2][sutun1]

    return desifreli_metin
