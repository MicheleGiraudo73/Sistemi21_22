def sieve(n):
    prime_list = []
    for k in range(2, n+1):
        if k not in prime_list:
            print (k)
            for j in range(k*k, n+1, k):
                prime_list.append(j)

def main():
    n = int(input("Inserire numero: "))

    print(sieve(n))
if __name__=="__main__":
    main()