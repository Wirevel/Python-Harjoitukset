class Dog:

    def __init__(self,name,age,sound):
        self.name = name
        self.age = age
        self.sound = sound
    
    def setBreed(self,breed):
        self.breed = breed
    
    def printDescription(self):
        print(self.name+" on "+self.age+" vuotias "+self.breed+" erityispiirteenä: " +self.superPower)

    def setSuperPower(self,superPower):
        self.superPower = superPower
        
    def bark(self):
        print(self.sound)

doge1 = Dog("kala","9","how much is the fish!")
doge2 = Dog("kukko","20","Suck a COCK!")
doge1.setBreed("Siika")
doge1.setSuperPower("Dumbfounded")
doge2.setBreed("Lintu")
doge2.setSuperPower("joka aamuinen Kyssäys huuto")

doge1.printDescription()
doge1.bark()
doge2.printDescription()
doge2.bark()