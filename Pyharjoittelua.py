import random

def main():
    kuinkaMonta = int(input("Kuinka monta lottorivia arvotaan: "))
    return kuinkaMonta


def lottorivi(x):
    rivi = []
    monesko = 0
    for y in range(x): #toistaa luuppia halutun rivien määrä
       while monesko < x: #toistaa kunnes on saatu haluttumäärä rivejä
            for i in range(7): #hakee 7 random numeroa ja lisää listaan
                randomLotto = random.randrange(1,41) #hakee random numeron 1-40 väliltä
                rivi.append(randomLotto) #lisää numeron randomLottosta riviin
            rivi = list(dict.fromkeys(rivi))    #poistaa dublicated
            if len(rivi) == 7: #jos rivissä on 7 numeroa.
                monesko += 1 # +1 increase
                rivi.sort() #järjestää numerot suuruus järjestykseen
                print(monesko," rivi ",rivi)
            rivi.clear() #Tyhjentää rivistä numerot

howMany = main()
lottorivi(howMany)