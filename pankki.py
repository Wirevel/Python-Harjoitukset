class pankkiTili(object):

    def __init__(self,tili,saldo,salasana):
        self.tili = tili
        self.saldo = saldo
        self.salasana = salasana
        

    def withdraw(self):
        nosto = int(input("paljonko nostetaan?: "))
        if nosto >= self.saldo:
            print(f"Nostit tilin tyhjäksi {self.saldo} jtn olet sitten PA.")
            self.saldo = self.saldo - self.saldo
            return self.saldo
        if nosto <= self.saldo:
            self.saldo = self.saldo - nosto
            print(f"nostit {nosto} tililtä ja tilille jäi {self.saldo}")
            return self.saldo

    def deposit(self):
        laitto = int(input("paljonko laitetaan?: "))
        if laitto < 100  and self.saldo == 0:
            print("liian vähän. Vähintään 100€")
            self.deposit()
        
            
        elif laitto:
            self.saldo = self.saldo + laitto
            print(f"tililläsi on {self.saldo}")
            return self.saldo
Tilit = {
    "tili1" : pankkiTili("tili1" ,0,"1234"),
    "tili2" : pankkiTili("tili2" ,200,"4321")
}

def main(self):
    condition = 1
    while condition == 1:
        print("valitsit tilin: "+ str(self.tili) + " Tiliin saldo on: "+ str(self.saldo))
        kumpi = str(input("Talletetaanko tilille vai nostetaanko? T/N lopetetaanko vai vaihdetaanko? L/V: "))

        if kumpi == "n" or kumpi == "N":
            self.withdraw()

        elif kumpi == "t" or kumpi == "T":
            self.deposit()
        if kumpi =="V" or kumpi == "v":
            password(choose())
            
        if kumpi =="L" or kumpi == "l":
            print("lopetetaan")
            break
        if self.saldo == 0:
            break


def choose():
    print("Löytyy nämä tilit: ")
    for x in Tilit:
        print(x)
    Mtili= str(input("mikä tili otetaan käyttöön? : ")) #Pyytää tilin nimen
    Ktili = Tilit.get(Mtili) #tarkistaa onko tiliä listassa ja tallentaa sen Ktili variableen

    if Ktili:
        return Tilit[Mtili]

    #if Mtili == str(Tilit[Mtili].tili):
        #print("valitsit tilin: "+ str(Tilit[Mtili].tili) + " Tiliin saldo on: "+ str(Tilit[Mtili].saldo))
    #    return Tilit[Mtili]

    else:
        print(str(Mtili)+" tiliä ei ole olemassa")
        choose()

def password(self):
    mSala = str(input("anna salasana: "))
    if mSala == self.salasana:
        print("salasana on oikein")
        main(self)
    else:
        print("salasana on väärin")
        password(self)



w = choose()
password(w)


#main(password(choose()))

#print(str(Tilit["tili1"].tili))


