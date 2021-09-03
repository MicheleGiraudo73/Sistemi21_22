def fattori(n):
    fat = []
    fac = 2
    while n > 1:
        while n % fac == 0:
            fat.append(fac)
            n /= fac
        fac += 1
    return fat

def main():
    num = int(input("Inserisci numero: "))

    print(fattori(60))

if __name__=="__main__":
    main()