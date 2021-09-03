def luhn(nCard):
    appoggio = []

    for k in range(len(appoggio)):
        if(k % 2 == 0):
            appoggio.append(nCard[k]*2)
        else:
            appoggio.append(nCard[k])
    sum = 0
    
    for k in appoggio:
        sum += k
    
    if( sum / 10 == 0):
        return "card valid"
    else:
        return "card invalid"


def main():
    numberCard = input("inserire il numero della carta di credito: (senza spazi)")

    card = []
    nn = 0

    for k in range(len(numberCard)):
        nn +=1 
        card.append(numberCard[k])
    
    if(nn > 16 or nn < 16):
        print("numero carta non valido")
    else:
        print(luhn(card))

if __name__ == "__main__":
    main()