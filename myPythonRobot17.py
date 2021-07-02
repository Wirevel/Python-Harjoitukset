import random


def main():
    Arvosana = [1,2,3,4,5]
    Ohjelmointikielet = ["Java","Python", "c#"]
    Opintopisteet = [3,5,6,10]
    i=1
    x=1
    

    print("tervetuloa suorittamaan ohjelmointikursseja robotilla!\nNyt seuraavat ohjelmointi kielet tarjolla:" )
    for y in Ohjelmointikielet: #printtaa ohjelmointikielet
        print(y)

    while i<=x: # looppaa kunnes halutaan lopettaa
        jatko = str(input("""Iske "q" jos et halua lisaa, tai Return/Enter jatkaa: """))

        if jatko == "q": #katkasee loopin
            print("hienosti tehty, jatka samaan malliin")
            break

        else:
            #Ohjelmointikielet.append(input("Syota uusi ohjelmointi kieli, jonka haluat lisata listalle: "))
            #for y in Ohjelmointikielet:  #printtaa ohjelmointikielet
            #    print(y)
            i +=1
            x +=1
            print("Hienoa, suoritit juuri ",random.choice(Ohjelmointikielet),", ",random.choice(Opintopisteet)," op, arvosanalla ",random.choice(Arvosana))
            return Ohjelmointikielet
        


def lisaaKielia(lista):
    kieli = [str(input("Syota uusi ohjelmointi kieli, jonka haluat lisata listalle: "))]
    lista.append(kieli)
    for u in lista:
        print(u)
    return lista


""" 
Eli lisaakielia(lista,kieli) lista on mainista importattu ohjelmointikielet ja kieli on returnattu versio listasta joka siirretään takas mainiin 
"""
lista=main()
lisaaKielia(lista)
