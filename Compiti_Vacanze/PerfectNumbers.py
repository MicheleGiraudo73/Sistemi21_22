def perfect(num):
    sommaAliquota = 0

    if num < 1:
        print("Valore non valido")

    for k in range(1,num):
        if num % k == 0:
            sommaAliquota += k

    if sommaAliquota == num:
        print("Numero perfetto")
    elif sommaAliquota > num:
        print("Numero Abbondante")
    else: 
        print("Numero carente")

def main():
    numero = int(input("Inserire un numero: "))
    perfect(numero)

if __name__=="__main__":
    main()