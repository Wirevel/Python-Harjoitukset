käyttis = str(input("Toimiiko kayttis? Y/N: "))
verkko = str(input("Toimiiko verkko? Y/N: "))
sähkö = str(input("Onko meilla sahkoa? Y/N: "))

if sähkö ==  str("n"):
    print("heikottaa - anna sähköä")

if käyttis == str("n") or verkko == str("n") and sähkö ==  str("y"):
    print("Huoltoa tarvitaan")

if käyttis == str("y") and verkko == str("y") and sähkö ==  str("y"):
    print("Huoltoa ei tarvita")

