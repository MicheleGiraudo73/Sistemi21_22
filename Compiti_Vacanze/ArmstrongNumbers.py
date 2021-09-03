def armstrong(number):
    potenza = len(str(number))
    somma = 0
    for k in str(number):
        somma += int(k)**potenza
    if somma == number:
        return True
    else:
        return False

def main():
    numero = int(input("inserire numero: "))
    if(armstrong(numero)):
        print("é un numero di armstrong")
    else:
        print("non é un numero di armstrong")

if __name__=="__main__":
    main()