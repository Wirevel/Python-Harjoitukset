import random


# luo korteille maan ja numeron
class Kortti(object):
    def __init__(self,maa,vari,numero):
        self.maa = maa
        self.numero = numero
        self.vari = vari


kortit = {
    "Pata" : Kortti("Pata","Musta", [1,2,3,4,5,6,7,8,9,10,11,12,13]),
    "Hertta" : Kortti("Hertta","Punainen", [1,2,3,4,5,6,7,8,9,10,11,12,13]),
    "Ruutu" : Kortti("Ruutu","Punainen", [1,2,3,4,5,6,7,8,9,10,11,12,13]),
    "Risti" : Kortti("Risti","Musta", [1,2,3,4,5,6,7,8,9,10,11,12,13])
}


def jako():
    kuinkaMonta = int(input("kuinka monta korttia jaetaan?: "))
    return kuinkaMonta

def kasi(x):
    m1 = kortit["Pata"]
    m2 = kortit["Hertta"]
    m3 = kortit["Ruutu"]
    m4 = kortit["Risti"]
    house = []
    for i in range(x):
        randomMaa = random.randrange(0,4)
        randomKortti = random.randrange(0,12)
        if randomMaa == 0:
            print(m1.maa +" "+ str(m1.numero[randomKortti]))
        if randomMaa == 1:
            print(m2.maa +" "+ str(m2.numero[randomKortti]))
        if randomMaa == 2:
            print(m3.maa +" "+ str(m3.numero[randomKortti]))
        if randomMaa == 3:
            print(m4.maa +" "+ str(m4.numero[randomKortti]))

#howMany = jako()
kasi(2)