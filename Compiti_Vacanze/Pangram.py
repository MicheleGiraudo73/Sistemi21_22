import string 

alfabeto = string.ascii_lowercase

def pangram(f):
    for i in alfabeto:
        if i not in f.lower():
            return False  
    return True

def main():
    frase = input("Inserire parola: ")
    if(pangram(frase)):
        print("è un pangram")
    else:
        print("non è un pangram")

if __name__=="__main__":
    main()