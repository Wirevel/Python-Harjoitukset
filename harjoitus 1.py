import random


# luo korteille maan ja numeron
class Kortti(object):
    def __init__(self,maa,numero):
        self.maa = maa
        self.numero = numero
        
#ei vielä toimi pakasta löytyvien korttien yhtenäinen tulostus
#    def Kortit(self):
#        print(self[0].maa)
#Printtaa annetun kortin
#    def whatCard(self):
#        print("Maa on " + self.maa+ " ja sen numero on " + str(self.numero[randomKortti]))      

kortit = {
    "Pata" : Kortti("Pata", [1,2,3,4,5,6,7,8,9,10,11,12,13]),
    "Hertta" : Kortti("Hertta", [1,2,3,4,5,6,7,8,9,10,11,12,13]),
    "Ruutu" : Kortti("Ruutu", [1,2,3,4,5,6,7,8,9,10,11,12,13]),
    "Risti" : Kortti("Risti", [1,2,3,4,5,6,7,8,9,10,11,12,13])
}
#kortit.whatCard()
randomMaa = random.randrange(0,3)
randomKortti = random.randrange(0,12)
#deck = [m1,m2,m3,m4]
#deck[randomMaa].whatCard()
#deck.Kortit()
#for kortti in kortit.values():
#    print("maa on "+ kortti.maa + " ja sen numerot on "+ str(kortti.numero) )

def jako():
    kuinkaMonta = int(input("kuinka monta korttia jaetaan?: "))
    return kuinkaMonta

def kasi(x):
    m1 = kortit["Pata"]
    m2 = kortit["Hertta"]
    m3 = kortit["Ruutu"]
    m4 = kortit["Risti"]
    for i in range(x):
        if randomMaa == 0:
            print(m1.maa +" "+ str(m1.numero[randomKortti]))
        if randomMaa == 1:
            print(m2.maa +" "+ str(m2.numero[randomKortti]))
        if randomMaa == 2:
            print(m3.maa +" "+ str(m3.numero[randomKortti]))
        if randomMaa == 3:
            print(m4.maa +" "+ str(m4.numero[randomKortti]))
    

#whut = kortit["Pata"]
#print(str(whut.numero[randomKortti])+ " " + whut.maa)
howMany = jako()
kasi(howMany)


