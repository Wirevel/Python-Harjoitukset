looping = True
while looping == True:
    merkkiJono = input("Anna merkkijono, niin lasken sen merkkien määrän: ")
    print(merkkiJono, ": yhteensä ",len(merkkiJono),"merkkia")
    jatko=str(input("Haluatko antaa uuden merkkijonon? ei = return/Enter, kylla = mika tahansa merkkijono: "))
    if jatko == "ei":
        looping = False
    
print("ei sitten")