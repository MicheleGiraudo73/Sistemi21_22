def is_isogram(p):
    p = p.upper()
    for char in p:
        if p.count(char) > 1 and char != " " and char != "-": #.count restituisce il numero di volte che appare la lettera, se appare più volte ritorna false
            return False
    return True

def main():
    parola = input("inserire parola: ")
    if(is_isogram(parola)):
        print("è un isogramma la parola inserita")
    else:
        print("non è un isogramma la parola inserita")

if __name__=="__main__":
    main()