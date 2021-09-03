def sum_of_multiples(limite, multipli) -> int:
    som = 0
    for k in range(1, limite):
        for j in multipli:
            if j != 0 and k % j == 0:
                som += k
                break
    return som

def main():
    limite = int(input("Inserisci limite: "))
    n1 = int(input("Inserisci numero: "))
    n2 = int(input("Inserisci numero: "))
    x = []
    x.append(n1)
    x.append(n2)


    print(sum_of_multiples(limite, x))

if __name__=="__main__":
    main()