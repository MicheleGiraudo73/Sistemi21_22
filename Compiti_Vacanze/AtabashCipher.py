PLAIN =  "abcdefghijklmnopqrstuvwxyz"
CIPHER = "zyxwvutsrqponmlkjihgfedcba"

p = list(PLAIN)
c = list(CIPHER)

def encode(st):
    enc = ""

    for k in st:
        for j in p:
            if k == j:
                ind=p.index(j)
                enc += c[ind]
    print(enc)

def decode(st):
    dec = ""

    for k in st:
        for j in c:
            if k == j:
                ind = c.index(j)
                dec += p[ind]
    print(dec)


def main():
    scelta = int(input("inserire 1 per encode 2 per decode: "))

    if scelta == 1:
        frase = input("inserire frase: ")
        encode(frase)
    else:
        frase = input("inserire frase: ")
        decode(frase)

if __name__=="__main__":
    main()