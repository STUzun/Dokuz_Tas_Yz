# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from AB_Budama import *
from OyunTahtasi import *
from Sezgi import *
import time

alpha = float('-inf')
beta = float('inf')
derinlik = 3
ai_derinlik = 4


def tahtaCiktisi(tahta):
    print(tahta[0] + "(00)----------------------" + tahta[1] + "(01)----------------------" + tahta[2] + "(02)")
    print("|                           |                           |")
    print("|       " + tahta[8] + "(08)--------------" + tahta[9] + "(09)--------------" + tahta[10] + "(10)     |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |        " + tahta[16] + "(16)-----" + tahta[17] + "(17)-----" + tahta[18] + "(18)       |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print(tahta[3] + "(03)---" + tahta[11] + "(11)----" + tahta[19] + "(19)               " + tahta[20] + "(20)----" +
          tahta[12] + "(12)---" + tahta[4] + "(04)")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |        " + tahta[21] + "(21)-----" + tahta[22] + "(22)-----" + tahta[23] + "(23)       |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       " + tahta[13] + "(13)--------------" + tahta[14] + "(14)--------------" + tahta[15] + "(15)     |")
    print("|                           |                           |")
    print("|                           |                           |")
    print(tahta[5] + "(05)----------------------" + tahta[6] + "(06)----------------------" + tahta[7] + "(07)")


def HUMAN_VS_AI(heuristic_stage1, heuristic_stage23):
    tahta = []
    for i in range(24):
        tahta.append("X")

    evaluation = olcum()

    for i in range(9):

        tahtaCiktisi(tahta)
        finished = False
        while not finished:
            try:

                pos = int(input("\n'1' oyuncusu icin bolge: "))

                if tahta[pos] == "X":

                    tahta[pos] = '1'
                    if uclemeVarMi(pos, tahta):
                        itemPlaced = False
                        while not itemPlaced:
                            try:

                                pos = int(input("\nSilinecek '2' nin bolgesi: "))

                                if tahta[pos] == "2" and not uclemeVarMi(pos, tahta) or (
                                        uclemeVarMi(pos, tahta) and olasiUclemeSayisi(tahta, "1") == 3):
                                    tahta[pos] = "X"
                                    itemPlaced = True
                                else:
                                    print("Uygun olmayan pozisyon")

                            except Exception:
                                print("Giris sayi deği veya aralik disinda")

                    finished = True

                else:
                    print("Bu bolge dolu")

            except Exception:
                print("Input degeri alinamadi")

        tahtaCiktisi(tahta)
        evaltahta = alpha_beta_budama(tahta, derinlik, False, alpha, beta, True, heuristic_stage1)

        if evaltahta.olcum == float('-inf'):
            print("Kaybettin")
            exit(0)
        else:
            tahta = evaltahta.tahta

    endStagesFinished = False
    while not endStagesFinished:

        tahtaCiktisi(tahta)

        # Get the users next move
        userHasMoved = False
        while not userHasMoved:
            try:
                pos = int(input("\n'1' tasi haraket ettir: "))

                while tahta[pos] != '1':
                    pos = int(input("\n '1' tasi haraket ettir: "))

                userHasPlaced = False
                while not userHasPlaced:

                    newPos = int(input("'1' Yeni konum: "))

                    if tahta[newPos] == "X":
                        tahta[pos] = 'X'
                        tahta[newPos] = '1'

                        if uclemeVarMi(newPos, tahta):

                            userHasRemoved = False
                            while not userHasRemoved:
                                try:

                                    pos = int(input("\nSilinecek '2' nin bolgesi: "))

                                    if tahta[pos] == "2" and not uclemeVarMi(pos, tahta) or (
                                            uclemeVarMi(pos, tahta) and olasiUclemeSayisi(tahta, "1") == 3):
                                        tahta[pos] = "X"
                                        userHasRemoved = True
                                    else:
                                        print("Uygun olmayan pozisyon")
                                except Exception:
                                    print("Error while accepting input")

                        userHasPlaced = True
                        userHasMoved = True

                    else:
                        print("Buraya haraket edemezsin")

            except Exception:
                print("Buraya haraket edemezsin")

        if DurumIkiUcOlc(tahta) == float('inf'):
            print("Kazandin!")
            exit(0)

        tahtaCiktisi(tahta)

        evaluation = alpha_beta_budama(tahta, derinlik, False, alpha, beta, False, heuristic_stage23)

        if evaluation.olcum == float('-inf'):
            print("Kaybettin")
            exit(0)
        else:
            tahta = evaluation.tahta


if __name__ == "__main__":
    print("Dokuz tas oyununa hos geldiniz")
    print("==========================")
    print("Insan bilgisayara karsi")

    HUMAN_VS_AI(TasSezgisi, GelismisSezgi)
