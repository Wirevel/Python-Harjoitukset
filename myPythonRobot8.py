print("Hei olen robotti, joka summailee numeroita 5 kertaa")
total = int(0)
anna = 0

while anna < 5:
    numero = int(input("Anna numero: "))
    total = numero + total
    print("nyt summa on: ", total)
    print("nyt menossa ", anna + 1 , " syöttökerta")
    anna +=1
print("Lopputulema on ", total)

