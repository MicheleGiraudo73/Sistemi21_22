'''
Convert a phrase to its acronym.

Techies love their TLA (Three Letter Acronyms)!

Help generate some jargon by writing a program that converts a long name like Portable Network Graphics to its acronym (PNG).
'''

def convert(f):
    acronym = ""
    for k in range(len(f)):
        if k==0:
            acronym = f[k].upper()
        else:
            if f[k-1]== ' ':
                acronym+= f[k].upper()

    return acronym


def main():
    frase = input("inserire frase da convertire: ")

    print(convert(frase))



if __name__=="__main__":
    main()