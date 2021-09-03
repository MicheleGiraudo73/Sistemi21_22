def main():
    parola = input("inserisci parola: ")
    parolaInversa=''.join(reversed(parola))
    print(parolaInversa) 

if __name__=="__main__":
    main()