
num = input ("Hei, kerro millaisen tulostuksen haluat, iloise=1, totisen = 2, viksun= 3:")
num = int(num)
määrä = int(input("Kerro myös montako kertaa haluat tulostaa?: "))
numberOfTimes = 0

if num == 1:
    while numberOfTimes < määrä:
        print("MyPythonRobot on iloinen")
        print("o   o")
        print("  #")
        print("(   )")
        print("\ -/")
        numberOfTimes +=1

if num == 2:
    while numberOfTimes < määrä:
        print("MyPythonRobot on totinen")
        print("o   o")
        print("  #")
        print("---")
        numberOfTimes +=1

if num == 3:
    while numberOfTimes < määrä:
        print("MyPythonRobot on viksu")
        print("o   o")
        print("  #")
        print("~   ~")
        print(" ~~~")
        numberOfTimes +=1

