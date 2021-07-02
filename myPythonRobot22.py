class Robot:

    def __init__(self,nimi,väri,malli):
        self.nimi = nimi
        self.väri = väri
        self.malli = malli

    def printDescription(self):
        print("Olen "+self.nimi+" malliltani "+self.väri+" " + self.malli)
    
r2d2=Robot("R2D2","valkoinen","astromekaanikkodroidi")

r2d2.printDescription()
print(r2d2.nimi)