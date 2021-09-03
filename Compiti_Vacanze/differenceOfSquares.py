def quadratiDiSomme(number):
    tot = 0
    for k in range(number+1):
        tot = tot + k
    total = tot*tot    
    return total

def sommaDeiQuadrati(number):
    
    tot = 0
    for k in range(number+1):
        tot = tot + (k*k)
    return tot

def differenza(number):
    
    square_total = quadratiDiSomme(number)
    sum_total = sommaDeiQuadrati(number)

    return square_total-sum_total

def main():
    num = int(input("inserire numero: "))

    print(differenza(num))

if __name__=="__main__":
    main()