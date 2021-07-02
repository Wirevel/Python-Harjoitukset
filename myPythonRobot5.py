kellonAika = input("Anna kellonaika täystunteina 24h: ")
kellonAika = int(kellonAika)
öitä = [22,23,24,1,2,3,4,5,6]
huomenta = [7,8,9,10]
töitä = [11,12,13,14,15,16]
iltapala = [17,18,19,20,21]
väsyttää = input("Väsyttääkö? Y/N: ")
väysttää = str(väsyttää)

for i in öitä:
    if kellonAika == i and väsyttää== str("y"):
        print("nukun… krooh, krooh")
    if kellonAika == i and väsyttää == str("n"):
        print("Anna yöpalaa")


for i in huomenta:
    if kellonAika == i and väsyttää== str("y"):
        print("aamupalaa ja kaffea")
    if kellonAika == i and väsyttää == str("n"):
        print("aamupalaa, kiitos")
        print("o   o")
        print("  #")
        print("(   )")
        print(" -/")

for i in töitä:
    if kellonAika == i and väsyttää== str("y"):
        print("Töitä")
        print("o   o")
        print("  #")
        print("---")
    if kellonAika == i and väsyttää == str("n"):
        print("kulkee")
        print("o   o")
        print("  #")
        print("~   ~")
        print(" ~~~")

for i in iltapala:
    if kellonAika == i:
        print("iltapalaa jos saisi...")
if kellonAika >=int(25):
    print("Opetteles nyt antaa kellonaika täystunteina")