from OyunTahtasi import *


def TasSezgisi(tahta, birinci_durummu):
    
    
    '''
    Tahtadaki tas sayisinia bakan sezgisel
    '''

    ''' 1. oyuncu tas sayisi'''
    birinciOyuncuTasSayisi = kacTane(tahta, "1")

    ''' 2. oyuncu tas sayisi'''
    ikinciOyuncuTasSayisi = kacTane(tahta, "2")


    if not birinci_durummu:
        movablePiecesBlack = len(DurumIkiveyaUcHamleleri(tahta))
        if ikinciOyuncuTasSayisi <= 2 or movablePiecesBlack == 0:
            sezgiolc = float('inf')
        elif birinciOyuncuTasSayisi <= 2:
            sezgiolc = float('-inf')
        else:
            sezgiolc = 200 * (birinciOyuncuTasSayisi - ikinciOyuncuTasSayisi)
    else:
        sezgiolc = 100 * (birinciOyuncuTasSayisi - ikinciOyuncuTasSayisi)

    return sezgiolc


def olasiUcluSezgisi(tahta, birinci_durummu):

    sezgiolc = 0

    birinciOyuncuTasSayisi = kacTane(tahta, "1")
    ikinciOyuncuTasSayisi = kacTane(tahta, "2")



    if not birinci_durummu:
        movablePiecesBlack = len(DurumIkiveyaUcHamleleri(tahta))
        if ikinciOyuncuTasSayisi <= 2 or movablePiecesBlack == 0:
            sezgiolc = float('inf')
        elif birinciOyuncuTasSayisi <= 2:
            sezgiolc = float('-inf')
        else:
            if (birinciOyuncuTasSayisi < 4):
                sezgiolc += 100 * olasiUclemeSayisi(tahta, "1")
                sezgiolc += 200 * UcluOlabilecekTaslar(tahta, "2")
            else:
                sezgiolc += 200 * olasiUclemeSayisi(tahta, "1")
                sezgiolc += 100 * UcluOlabilecekTaslar(tahta, "2")
    else:
        if birinciOyuncuTasSayisi < 4:
            sezgiolc += 100 * olasiUclemeSayisi(tahta, "1")
            sezgiolc += 200 * UcluOlabilecekTaslar(tahta, "2")
        else:
            sezgiolc += 200 * olasiUclemeSayisi(tahta, "1")
            sezgiolc += 100 * UcluOlabilecekTaslar(tahta, "2")

    return sezgiolc


def hamleYapabilecekTaslarSezgisi(tahta, birinci_durummu):

    birinciOyuncuTasSayisi = kacTane(tahta, "1")
    ikinciOyuncuTasSayisi = kacTane(tahta, "2")


    if not birinci_durummu:
        ikinciOyuncuOynatilabilenTaslar = len(DurumIkiveyaUcHamleleri(tahta))
        if ikinciOyuncuTasSayisi <= 2 or ikinciOyuncuOynatilabilenTaslar == 0:
            sezgiolc = float('inf')
        elif birinciOyuncuTasSayisi <= 2:
            sezgiolc = float('-inf')
        else:
            sezgiolc = 100 * (birinciOyuncuTasSayisi - ikinciOyuncuTasSayisi)
            sezgiolc -= 50 * ikinciOyuncuOynatilabilenTaslar
    else:
        sezgiolc = 100 * (birinciOyuncuTasSayisi - ikinciOyuncuTasSayisi)


    return sezgiolc


def GelismisSezgi(tahta, birinci_durummu):
    '''
     Tas sayisi ve olasi uclu tas sayisi sezgiseli
    '''

    sezgiolc = 0

    birinciOyuncuTasSayisi = kacTane(tahta, "1")
    ikinciOyuncuTasSayisi = kacTane(tahta, "2")

    ikinciOyuncuHamleYapilabilirTaslar = 0

    if not birinci_durummu:
        ikinciOyuncuHamleYapilabilirTaslar = len(DurumIkiveyaUcHamleleri(tahta))
        if ikinciOyuncuTasSayisi <= 2 or ikinciOyuncuHamleYapilabilirTaslar == 0:
            sezgiolc = float('inf')
        elif birinciOyuncuTasSayisi <= 2:
            sezgiolc = float('-inf')
        else:
            if (birinciOyuncuTasSayisi < 4):
                sezgiolc += 100 * olasiUclemeSayisi(tahta, "1")
                sezgiolc += 200 * UcluOlabilecekTaslar(tahta, "2")
            else:
                sezgiolc += 200 * olasiUclemeSayisi(tahta, "1")
                sezgiolc += 100 * UcluOlabilecekTaslar(tahta, "2")
            sezgiolc -= 25 * ikinciOyuncuHamleYapilabilirTaslar
            sezgiolc += 50 * (birinciOyuncuTasSayisi - ikinciOyuncuTasSayisi)
    else:
        if birinciOyuncuTasSayisi < 4:
            sezgiolc += 100 * olasiUclemeSayisi(tahta, "1")
            sezgiolc += 200 * UcluOlabilecekTaslar(tahta, "2")
        else:
            sezgiolc += 200 * olasiUclemeSayisi(tahta, "1")
            sezgiolc += 100 * UcluOlabilecekTaslar(tahta, "2")
        sezgiolc -= 25 * ikinciOyuncuHamleYapilabilirTaslar
        sezgiolc += 50 * (birinciOyuncuTasSayisi - ikinciOyuncuTasSayisi)

    return sezgiolc