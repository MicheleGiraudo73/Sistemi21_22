def protein(rna):
    proteine = []

    pro = {"AUG": "Methionine",
                   "UUU": "Phenylalanine",
                   "UUC": "Phenylalanine",
                   "UUA": "Leucine",
                   "UUG": "Leucine",
                   "UCU": "Serine",
                   "UCC": "Serine",
                   "UCA": "Serine",
                   "UCG": "Serine",
                   "UAU": "Tyrosine",
                   "UAC": "Tyrosine",
                   "UGU": "Cysteine",
                   "UGC": "Cysteine",
                   "UGG": "Tryptophan",
                   "UAA": "STOP",
                   "UAG": "STOP",
                   "UGA": "STOP"}

    n=3
    rna = [rna[i:i+n] for i in range(0, len(rna), n)]
    
    for p in rna:
        if pro[p]=="STOP":
            return proteine
        proteine.append(pro[p])
    return proteine

def main():
    rna = input("Inserisci rna: ")

    print(protein(rna))

if __name__=="__main__":
    main()