def isbnVerifier(isbn):
    listaNum = []
    somma = 0
    molti = 10

    for k in isbn:
        if k != "-":
            if k == "X":
                listaNum.append(10)
            else:
                listaNum.append(int(k))

    for i in listaNum:
        somma += i * molti
        molti-=1

    if somma % 11 == 0:
        print("ISBN valido")
    else:
        print("ISBN non valido")

def main():
    isbn = input("inserire isbn-10: ")
    isbnVerifier(isbn)

if __name__=="__main__":
    main() 