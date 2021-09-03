import secrets

def private(p):
    return secrets.choice(range(2, p))


def public(p, g, private):
    return (g**private) % p


def secret(p, public, private):
    return (public**private) % p

def main():
    numeri_primi = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    p  = secrets.choice(numeri_primi)

    g = secrets.choice(numeri_primi)

    Alice = []
    Bob = []
    p1 = private(p)
    p2 = private(p)

    Alice.append(p1)
    Bob.append(p2)

    public1 = public(p,g,p1)
    public2 = public(p,g,p2)

    Alice.append(public2)
    Bob.append(public1)

    s1 = secret(p,public2,p1)
    s2 = secret(p,public1,p2)

    Alice.append(s1)
    Bob.append(s2)

    print("Chiavi Alice: ",Alice)
    print("Chiavi Bob: ",Bob)



    

if __name__=="__main__":
    main()