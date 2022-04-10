



def kacTane(tahta, value):
    return tahta.count(value)

def TahtayiCevir(tahta):

    tahtayicevir = []
    for j in tahta:

        if j == "1":
            tahtayicevir.append("2")
        elif j == "2":
            tahtayicevir.append("1")
        else:
            tahtayicevir.append("X")


    return tahtayicevir

def cevrilmisTahtaListe(pos_list):
    '''
    '''


    result = []
    for j in pos_list:
        result.append(TahtayiCevir(j))
    return result




def komsuKonumlari(position):
    komsular = [
        [1, 3],
        [0, 2, 9],
        [1, 4],
        [0, 5, 11],
        [2, 7, 12],
        [3, 6],
        [5, 7, 14],
        [4, 6],
        [9, 11],
        [1, 8, 10, 17],
        [9, 12],
        [3, 8, 13, 19],
        [4, 10, 15, 20],
        [11, 14],
        [6, 13, 15, 22],
        [12, 14],
        [17, 19],
        [9, 16, 18],
        [17, 20],
        [11, 16, 21],
        [12, 18, 23],
        [19, 22],
        [21, 23, 14],
        [20, 22]
    ]
    return komsular[position]


def cizgiUstuUclemeKontrolu(position, tahta, player):
    ucleme_icindekiler = [
        (cizgiUstunuKapatmisMi(player, tahta, 1, 2) or cizgiUstunuKapatmisMi(player, tahta, 3, 5)),
        (cizgiUstunuKapatmisMi(player, tahta, 0, 2) or cizgiUstunuKapatmisMi(player, tahta, 9, 17)),
        (cizgiUstunuKapatmisMi(player, tahta, 0, 1) or cizgiUstunuKapatmisMi(player, tahta, 4, 7)),
        (cizgiUstunuKapatmisMi(player, tahta, 0, 5) or cizgiUstunuKapatmisMi(player, tahta, 11, 19)),
        (cizgiUstunuKapatmisMi(player, tahta, 2, 7) or cizgiUstunuKapatmisMi(player, tahta, 12, 20)),
        (cizgiUstunuKapatmisMi(player, tahta, 0, 3) or cizgiUstunuKapatmisMi(player, tahta, 6, 7)),
        (cizgiUstunuKapatmisMi(player, tahta, 5, 7) or cizgiUstunuKapatmisMi(player, tahta, 14, 22)),
        (cizgiUstunuKapatmisMi(player, tahta, 2, 4) or cizgiUstunuKapatmisMi(player, tahta, 5, 6)),
        (cizgiUstunuKapatmisMi(player, tahta, 9, 10) or cizgiUstunuKapatmisMi(player, tahta, 11, 13)),
        (cizgiUstunuKapatmisMi(player, tahta, 8, 10) or cizgiUstunuKapatmisMi(player, tahta, 1, 17)),
        (cizgiUstunuKapatmisMi(player, tahta, 8, 9) or cizgiUstunuKapatmisMi(player, tahta, 12, 15)),
        (cizgiUstunuKapatmisMi(player, tahta, 3, 19) or cizgiUstunuKapatmisMi(player, tahta, 8, 13)),
        (cizgiUstunuKapatmisMi(player, tahta, 20, 4) or cizgiUstunuKapatmisMi(player, tahta, 10, 15)),
        (cizgiUstunuKapatmisMi(player, tahta, 8, 11) or cizgiUstunuKapatmisMi(player, tahta, 14, 15)),
        (cizgiUstunuKapatmisMi(player, tahta, 13, 15) or cizgiUstunuKapatmisMi(player, tahta, 6, 22)),
        (cizgiUstunuKapatmisMi(player, tahta, 13, 14) or cizgiUstunuKapatmisMi(player, tahta, 10, 12)),
        (cizgiUstunuKapatmisMi(player, tahta, 17, 18) or cizgiUstunuKapatmisMi(player, tahta, 19, 21)),
        (cizgiUstunuKapatmisMi(player, tahta, 1, 9) or cizgiUstunuKapatmisMi(player, tahta, 16, 18)),
        (cizgiUstunuKapatmisMi(player, tahta, 16, 17) or cizgiUstunuKapatmisMi(player, tahta, 20, 23)),
        (cizgiUstunuKapatmisMi(player, tahta, 16, 21) or cizgiUstunuKapatmisMi(player, tahta, 3, 11)),
        (cizgiUstunuKapatmisMi(player, tahta, 12, 4) or cizgiUstunuKapatmisMi(player, tahta, 18, 23)),
        (cizgiUstunuKapatmisMi(player, tahta, 16, 19) or cizgiUstunuKapatmisMi(player, tahta, 22, 23)),
        (cizgiUstunuKapatmisMi(player, tahta, 6, 14) or cizgiUstunuKapatmisMi(player, tahta, 21, 23)),
        (cizgiUstunuKapatmisMi(player, tahta, 18, 20) or cizgiUstunuKapatmisMi(player, tahta, 21, 22)),
    ]

    return ucleme_icindekiler[position]


def cizgiUstunuKapatmisMi(oyuncu_numarasi, tahta, pos1, pos2):
    if tahta[pos1] == oyuncu_numarasi and tahta[pos2] == oyuncu_numarasi:
        return True
    return False


def uclemeVarMi(position, tahta):

    if tahta[position] != "X":
        return cizgiUstuUclemeKontrolu(position, tahta, tahta[position])

    return False


def durumBirdeHamle(tahta):
    tahta_list = []

    for j in range(len(tahta)):
        if (tahta[j] == "X"):
            tahta_clone = copy.deepcopy(tahta)
            tahta_clone[j] = "1"

            if (uclemeVarMi(j, tahta_clone)):
                tahta_list = TasSil(tahta_clone, tahta_list)
            else:
                tahta_list.append(tahta_clone)
    return tahta_list


def durumIkideHamle(tahta):
    tahta_list = []
    for j in range(len(tahta)):
        if (tahta[j] == "1"):
            adjacent_list = komsuKonumlari(j)

            for pos in adjacent_list:
                if (tahta[pos] == "X"):
                    tahta_clone = copy.deepcopy(tahta)
                    tahta_clone[j] = "X"
                    tahta_clone[pos] = "1"

                    if uclemeVarMi(pos, tahta_clone):
                        tahta_list = TasSil(tahta_clone, tahta_list)
                    else:
                        tahta_list.append(tahta_clone)
    return tahta_list


def durumUcdeHamle(tahta):
    tahta_list = []

    for i in range(len(tahta)):
        if (tahta[i] == "1"):

            for j in range(len(tahta)):
                if (tahta[j] == "X"):
                    tahta_clone = copy.deepcopy(tahta)

                    tahta_clone[i] = "X"
                    tahta_clone[j] = "1"

                    if (uclemeVarMi(j, tahta_clone)):
                        tahta_list = TasSil(tahta_clone, tahta_list)
                    else:
                        tahta_list.append(tahta_clone)
    return tahta_list


def DurumIkiveyaUcHamleleri(tahta):
    if (kacTane(tahta, "1") == 3):
        return durumUcdeHamle(tahta)
    else:
        return durumIkideHamle(tahta)


def TasSil(tahta_clone, tahta_list):

    for j in range(len(tahta_clone)):
        if (tahta_clone[j] == "2"):

            if not uclemeVarMi(j, tahta_clone):
                yeni_tahta = copy.deepcopy(tahta_clone)
                yeni_tahta[j] = "X"
                tahta_list.append(yeni_tahta)
    return tahta_list


def olasiUclemeSayisi(tahta, player):
    count = 0

    for j in range(len(tahta)):
        if (tahta[j] == "X"):
            if cizgiUstuUclemeKontrolu(j, tahta, player):
                count += 1
    return count


def DurumIkiUcOlc(tahta):
    birinciTasSayisi = kacTane(tahta, "1")
    ikinciTasSayisi = kacTane(tahta, "2")

    if ikinciTasSayisi <= 2:
        return float('inf')
    elif birinciTasSayisi <= 2:
        return float('-inf')
    else:
        return 0


def UcluOlabilirmi(position, tahta, oyuncu_nu):
    komsular = komsuKonumlari(position)

    for j in komsular:
        if (tahta[j] == oyuncu_nu) and (not cizgiUstuUclemeKontrolu(position, tahta, oyuncu_nu)):
            return True
    return False


def UcluOlabilecekTaslar(tahta, player):
    count = 0

    for i in range(len(tahta)):
        if (tahta[i] == player):
            komsular = komsuKonumlari(i)
            for pos in komsular:
                if (player == "1"):
                    if (tahta[pos] == "2"):
                        tahta[i] = "2"
                        if uclemeVarMi(i, tahta):
                            count += 1
                        tahta[i] = player

                elif (tahta[pos] == "1" and UcluOlabilirmi(pos, tahta, "1")):
                        count += 1
    return count


import copy
