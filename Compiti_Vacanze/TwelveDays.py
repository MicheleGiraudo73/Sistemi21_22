regali = [
    " a Partridge in a Pear Tree.",
    " two Turtle Doves, and",
    " three French Hens,",
    " four Calling Birds,",
    " five Gold Rings,",
    " six Geese-a-Laying,",
    " seven Swans-a-Swimming,",
    " eight Maids-a-Milking,",
    " nine Ladies Dancing,",
    " ten Lords-a-Leaping,",
    " eleven Pipers Piping,",
    " twelve Drummers Drumming,",
]

giorni = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]

def song(verso1,verso2):
    canzone = []
    for giorno in range(verso1 - 1, verso2):
        frase = f"On the {giorni[giorno]} day of Christmas my true love gave to me:"
        for regalo in range(giorno, -1, -1):
            frase += regali[regalo]
        canzone.append(frase)
    return canzone

def main():
    verso1 = int(input("Inserisci verso inizio: "))
    verso2 = int(input("Inserisci verso fine: "))
    print(song(verso1,verso2))

if __name__=="__main__":
    main()

