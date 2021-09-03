def distance(rna1, rna2):
    if(len(rna1)!=len(rna2)):
        return "RNA non compatibili"
    
    dist = 0
    
    for i in range(0, len(rna1)):
        if (rna1[i] != rna2[i]):
            dist += 1
    
    return dist

def main():
    rna1 = input("inserisci RNA 1: ")
    rna2 = input("inserisci RNA 2: ")

    print("Distanza: ",distance(rna1,rna2))

if __name__=="__main__":
    main()