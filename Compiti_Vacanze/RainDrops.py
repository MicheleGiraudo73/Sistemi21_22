a='Pling'
b='Plang'
c='Plong'

def rainDrops(number):
    song = ""

    if(number %3 != 0 and number %7 != 0 and number %7 != 0 ):
        song = number

    if( number % 3 == 0 ):
        song+=a
    if( number % 5 == 0 ):
        song+=b
    if( number % 7 == 0 ):
        song+=c  

    return song

def main():
    numero = int(input("inserire un numero"))

    print(rainDrops(numero))

if __name__=="__main__":
    main()