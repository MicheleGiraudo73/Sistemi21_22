colori = {"nero":"0", "marrone":"1","rosso":"2","arancione":"3","giallo":"4","verde":"5","blu":"6","viola":"7","grigio":"8","bianco":"9"}

multi = {"nero":1, "marrone":10,"rosso":100,"arancione":1000,"giallo":10000,"verde":100000,"blu":1000000,"viola":10000000,"grigio":0.1,"bianco":0.01}

def calcolaResistore(b1,b2,b3):
    num = ""
    moltiplicatore = 0
    ohm = 0

    for x in colori.keys():
        
        if x == b1:
            num+=colori[x]
    for k in colori.keys():
        if k == b2:
            num+= colori[k]
    
    for j in multi.keys():
        if j == b3:
            moltiplicatore = multi[j]
    
    
    ohm = int(num)*moltiplicatore
    print(f"resistenza in ohm: {ohm}")

def main():
    print("colori delle bande scritti in minscolo\n")
    banda_1 = input("inserire colore prima banda: \n")
    banda_2 = input("inserire colore seconda banda: \n")
    banda_3 = input("inserire colore terza banda: \n")

    calcolaResistore(banda_1,banda_2,banda_3)
if __name__=="__main__":
    main()