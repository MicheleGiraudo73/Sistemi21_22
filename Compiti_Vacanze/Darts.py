from math import sqrt


def score(x, y):
    dist = sqrt(x**2 + y**2)
    return 0 if dist > 10 else 1 if dist > 5 else 5 if dist > 1 else 10

def main():
    coordX = int(input("coordinata X: "))

    coordY = int(input("coordinata Y: "))

    print("Punteggio: ",score(coordX,coordY))

    
if __name__=="__main__":
    main()