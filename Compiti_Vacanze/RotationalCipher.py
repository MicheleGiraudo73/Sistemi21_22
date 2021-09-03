import string
from typing import ChainMap

alphabet = string.ascii_lowercase

def rotate(parola,chiave):
    rot = ""
    for t in parola:
        if t in alphabet:
            rot += alphabet[alphabet.index(t)+chiave-26]
        else:
            rot += t
    return rot

def main():
    parola = input("inserire parola da convertire: ")
    chiave = int(input("inserire numero rot: "))
    print(rotate(parola,chiave))

if __name__=="__main__":
    main()