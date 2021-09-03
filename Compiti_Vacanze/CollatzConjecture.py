def step(n):
    if n <= 0:
        return "numero non valido"
    
    cnt = 0
    while n> 1:
        if n % 2 != 0:
            n = n * 3 + 1
            cnt += 1
        else:
            n =  n / 2
            cnt += 1
    
    return cnt

def main():
    numero = int(input("inserisci numero: "))
    print("Numero step per arrivare a 1: ",step(numero))

if __name__=="__main__":
    main()