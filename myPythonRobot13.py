def uusipaiva():
    pv = 'MaTiKeToPeLaSu'
    print("Mikä päivä ?")
    pvnumero = int(input("Valitse seuraavista 1 = Ma, 2 = Ti ...7 = Su : "))
    startIndex = (pvnumero-1) * 2
    endIndex = startIndex + 2
    return(pv[startIndex:endIndex])


def mikaPaiva(päivä):

    if päivä == "Ma":
        print("Ahaa maanantai, pitaako alkaa toihin?")
    if päivä == "Ti":
        print("Kylla, tiistai, ilman muuta aloitetaan homma!")
    if päivä == "Ke":
        print("Keskiviikko, mielenkiintoista, mita piti tehda?")
    if päivä == "To":
        print("Niin, siis torstai, ihanko totta?")
    if päivä == "Pe":
        print("Mika, perjantai? Kohta viikonloppu : )")
    if päivä == "La":
        print("Lauantai, saunaan suomalaiset")
    if päivä == "Su":
        print("Olen lepomoodissa, on naas sunnuntai")
    
    else:
        print("Olen lepomoodissa, on naas sunnuntai")
    

x=uusipaiva()
mikaPaiva(x)