import random


def main():
    Arvosana = [1,2,3,4,5]
    Ohjelmointikielet = ["Java","Python", "c#"]
    Opintopisteet = [3,5,6,10]
    i=1
    x=1
    
    print("Tervetuloa suorittamaan ohjelmointikursseja robotilla!")
    tulostaKielet(Ohjelmointikielet)# tulostaa kielet
    print("Hienoa, suoritit juuri ",random.choice(Ohjelmointikielet),", ",random.choice(Opintopisteet)," op, arvosanalla ",random.choice(Arvosana))
    while i<=x: # looppaa kunnes halutaan lopettaa
        
        jatko = str(input("""Iske "q" jos et halua lisaa, tai Return/Enter jatkaa: """))

        if jatko == "q": #katkasee loopin
            print("hienosti tehty, jatka samaan malliin")
            break

        else:
            i +=1
            x +=1
            print("Hienoa, suoritit juuri ",random.choice(Ohjelmointikielet),", ",random.choice(Opintopisteet)," op, arvosanalla ",random.choice(Arvosana))
            lisaaKielia(Ohjelmointikielet) #lisää kielen
            tulostaKielet(Ohjelmointikielet) # tulostaa kielet
           

def lisaaKielia(lista): #lisää kieli functio
    kieli = str(input("Syota uusi ohjelmointi kieli, jonka haluat lisata listalle: "))
    lista.append(kieli)
    return lista

def tulostaKielet(lista): #tulostaa lista functio
    print("Nyt seuraavat ohjelmointi kielet tarjolla:" )
    for u in lista:
        print(u)


main()

