dna = ["A","C","G","T"]
rna = ["U","G","C","A"]

def makeRna(d):

    stringRNA = ""

    for k in d.upper():
        if k == dna[0]:
            stringRNA+=rna[0]
        
        if k == dna[1]:
            stringRNA+=rna[1]
        
        if k == dna[2]:
            stringRNA+=rna[2]

        if k == dna[3]:
            stringRNA+=rna[3]

    print(f"stringa rna:  {stringRNA}")


def main():
    input_dna = input("Inserire stringa dna: ") 
    makeRna(input_dna)   

    
if __name__=="__main__":
    main()