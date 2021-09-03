def triplet(n):
    numeri = []
    for a in range(1,n):
        for b in range(a,n-a):
            c = n - a - b  #faccio la sottrazione e poi controllo in modo che se c è minore di a o di b so già che la "tripletta" dei numeri è sbagliata
            if c < b or c < a:  
                break
            if a**2 + b**2 == c**2:
                numeri.append([a,b,c])
    return numeri

def main():
    numero = int(input("inserire numero: "))

    print(triplet(numero))

    
if __name__=="__main__":
    main()
