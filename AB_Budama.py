from OyunTahtasi import *

ulasilan_asama = 0


budanan = 0

class olcum():

    def __init__(self):
        self.olcum = 0
        self.tahta = []


def alpha_beta_budama(tahta, derinlik, birinci_oyuncumu, alpha, beta, birinci_durummu, heuristic):
    sonOlcumDegeri = olcum()

    global ulasilan_asama
    ulasilan_asama += 1

    if derinlik != 0:
        if birinci_oyuncumu:

            if birinci_durummu:
                olasi_konum_durumlari = durumBirdeHamle(tahta)
            else:
                olasi_konum_durumlari = DurumIkiveyaUcHamleleri(tahta)

        else:

            if birinci_durummu:
                olasi_konum_durumlari = cevrilmisTahtaListe(durumBirdeHamle(TahtayiCevir(tahta)))

            else:
                olasi_konum_durumlari = cevrilmisTahtaListe(DurumIkiveyaUcHamleleri(TahtayiCevir(tahta)))

        for move in olasi_konum_durumlari:

            if birinci_oyuncumu:

                anlikOlcumDegeri = alpha_beta_budama(move, derinlik - 1, False, alpha, beta, birinci_durummu, heuristic)

                if anlikOlcumDegeri.olcum > alpha:
                    alpha = anlikOlcumDegeri.olcum
                    sonOlcumDegeri.tahta = move
            else:

                anlikOlcumDegeri = alpha_beta_budama(move, derinlik - 1, True, alpha, beta, birinci_durummu, heuristic)

                if anlikOlcumDegeri.olcum < beta:
                    beta = anlikOlcumDegeri.olcum
                    sonOlcumDegeri.tahta = move

            if alpha >= beta:
                global budanan
                budanan += 1
                break

        if birinci_oyuncumu:
            sonOlcumDegeri.olcum = alpha
        else:
            sonOlcumDegeri.olcum = beta

    else:

        if birinci_oyuncumu:
            sonOlcumDegeri.olcum = heuristic(tahta, birinci_durummu)
        else:
            sonOlcumDegeri.olcum = heuristic(TahtayiCevir(tahta), birinci_durummu)

    return sonOlcumDegeri


def minimax(tahta, derinlik, birinci_oyuncumu, alpha, beta, birinci_durummu, heuristic):
    sonOlcumDegeri = olcum()

    global ulasilan_asama
    ulasilan_asama += 1

    if derinlik != 0:
        anlikOlcumDegeri = olcum()

        if birinci_oyuncumu:

            if birinci_durummu:
                olasi_konum_durumlari = durumBirdeHamle(tahta)
            else:
                olasi_konum_durumlari = DurumIkiveyaUcHamleleri(tahta)

        else:

            if birinci_durummu:
                olasi_konum_durumlari = cevrilmisTahtaListe(durumBirdeHamle(TahtayiCevir(tahta)))
            else:
                olasi_konum_durumlari = cevrilmisTahtaListe(DurumIkiveyaUcHamleleri(TahtayiCevir(tahta)))

        for move in olasi_konum_durumlari:

            if birinci_oyuncumu:

                anlikOlcumDegeri = minimax(move, derinlik - 1, False, alpha, beta, birinci_durummu, heuristic)

                if anlikOlcumDegeri.olcum > alpha:
                    alpha = anlikOlcumDegeri.olcum
                    sonOlcumDegeri.tahta = move
            else:

                anlikOlcumDegeri = minimax(move, derinlik - 1, True, alpha, beta, birinci_durummu, heuristic)

                if anlikOlcumDegeri.olcum < beta:
                    beta = anlikOlcumDegeri.olcum
                    sonOlcumDegeri.tahta = move

        if birinci_oyuncumu:
            sonOlcumDegeri.olcum = alpha
        else:
            sonOlcumDegeri.olcum = beta

    else:

        if birinci_oyuncumu:
            sonOlcumDegeri.olcum = heuristic(tahta, birinci_durummu)
        else:
            sonOlcumDegeri.olcum = heuristic(TahtayiCevir(tahta), birinci_durummu)

    return sonOlcumDegeri


def getbudanan():
    global budanan
    x = budanan
    budanan = 0
    return x


def getUlasilanAsama():
    global ulasilan_asama
    x = ulasilan_asama
    ulasilan_asama = 0
    return x
