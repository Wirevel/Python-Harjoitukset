import random

def keraaTiedot():

    Etunimi = str(input("Anna etunimesi: "))
    Sukunimi = str(input("Anna sukunimesi: "))
    Ika = int(input("Anna ikäsi: "))
    Kotikaupunki= str(input("Anna kotikaupunkisi: "))
    kysymys = str(input("Pidätkö ohjelmoinnista? jos pidät, laita K, jos et, laita E "))
    minunTiedotDic = {'etunimi':Etunimi,'sukunimi':Sukunimi,'ika':Ika,'kotikaupunki':Kotikaupunki,'kysymys':kysymys}
    print("Kiitos... hieman tarkastelen mita vastasit :) ")
    print(minunTiedotDic, "\n")
   # minunTiedot = Etunimi,Sukunimi,Ika,Kotikaupunki,kysymys
    

    print(f"Saamani tiedon mukaan nimesi on {minunTiedotDic['etunimi']} {minunTiedotDic['sukunimi']} \nOlet jo {minunTiedotDic['ika']} vanha \nOlet kotoisin kaupungista {minunTiedotDic['kotikaupunki']}")

    if minunTiedotDic['kysymys'] == str("E") or minunTiedotDic['kysymys'] == str("e"):
        print("Ja jostain syystä et pidä ohjelmoinnista \n")

    else:
        print("Ja tottakai pidät ohjelmoinnista, kukapa ei :) \n")

    ennustus(minunTiedotDic['etunimi'],minunTiedotDic['sukunimi'],minunTiedotDic['ika'],minunTiedotDic['kysymys'])

def ennustus(enimi,snimi,ikä,vastaus):
    
    ikä +=5
    kaupunkiLista = ['Juupajoki','Pariisi','San Francisco','YläJepua','Singapore']

    print(f"Nyt omana Ennustajarobottinasi kerron tulevaisuudesta\nUudet tiedot {enimi} {snimi} ika {ikä} vuotta\nUusi koti {random.choice(kaupunkiLista)}")
    
    if vastaus == str("E") or vastaus == str("e"):
        print("Ja tottakai pidät ohjelmoinnista, kukapa ei :)")

    else:
        print("Ja tottakai pidät ohjelmoinnista, kukapa ei :)")


keraaTiedot()