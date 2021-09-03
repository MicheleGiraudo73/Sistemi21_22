def equilatero(lati):
    if lati[0] == 0:
        return False
    if lati[2] > lati[1] + lati[0]:
        return False
    if lati[2] == lati[1] and lati[1] == lati[0]:
        return True
    else:
        return False
def isoscele(lati):
    if lati[2] > lati[1] + lati[0]:
        return False
    if lati[2] == lati[1] or lati[1] == lati[0]:
        return True
    else:
        return False

def scaleno(lati):
    if lati[2] > lati[1] + lati[0]:
        return False
    if lati[2] != lati[1] and lati[1] != lati[0]:
        return True
    else:
        return False

def main():
    lat1= int(input("inserire primo lato: "))
    lat2= int(input("inserire secondo lato: "))
    lat3= int(input("inserire terzo lato: "))

    lati=[]
    lati.append(lat1)
    lati.append(lat2)
    lati.append(lat3)

    if(equilatero(lati)):
        print("Triangolo equilatero")
        
    if(isoscele(lati)):
        print("Triangolo isoscele")
    if(scaleno(lati)):
        print("Triangolo scaleno")

if __name__=="__main__":
    main()