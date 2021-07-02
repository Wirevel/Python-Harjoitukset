class BankAccount:

    def __init__(self,saldo):
        self.saldo = saldo

    def withdraw(self):
        nosto = int(input("Paljonko nostetaan? "))
        if self.saldo > nosto:
            self.saldo = self.saldo - nosto
            print("Tämän hetkinen saldo: ", self.saldo)
        elif nosto >= self.saldo:
            print("Nostit tilin tyhjäksi eli saat",self.saldo,"\nOlet sitten PA")
            self.saldo = self.saldo - self.saldo
            print("Tämän hetkinen saldo: ", self.saldo)

    def deposit(self):
        talletus = int(input("Paljonko talletetaan? "))
        if talletus >= 100:
            self.saldo = self.saldo + talletus
            print("Tämän hetkinen saldo: ", self.saldo)
        elif talletus < 100:
            print("Liian vähän!")
            self.deposit()

käyttäjä = BankAccount(0)
käyttäjä.deposit()
#käyttäjä.withdraw()


condition =1
while condition == 1:
    kumpi= str(input("talletetaanko vai nostetaanko rahaa, valitse T tai N: "))

    if kumpi == "T" or kumpi =="t":
        käyttäjä.deposit()

    elif kumpi == "N" or kumpi =="n":
        käyttäjä.withdraw()

    if käyttäjä.saldo == 0:
        break
