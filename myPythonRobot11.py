print("Hei, haluisin laskea paljonko sinulla on tunteja jaljella 70 ikavuoteen")


def KeraaTiedot():
    enimi = str(input("anna etunimi: "))
    snimi = str(input("anna sukunimi: "))
    ika = int(input("anna ika: "))
    return enimi,snimi,ika;

def wit(enimi,snimi,ika):
    """
    enimi=wot[0]
    snimi=wot[1]
    ika=wot[2]
    """
    tunnit = 613200 #70 vuotta laskettu tunneiksi
    laskIka = ika * 365 * 24 #ika tunneiksi
    print("Laskennan tulos: "+ enimi +" " + snimi + " sinulla on noin ", tunnit-laskIka, " tuntia 70 ikavuoteen jaljella")

e,s,i=KeraaTiedot()

wit(e,s,i)