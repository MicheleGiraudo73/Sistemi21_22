m = ["M", "MM", "MMM"]
c = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
d = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
u = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
romani = []
indice = 0
def arabo_romano(numero):
    qm = int(numero / 1000) # migliaia
    qc = int((numero - qm * 1000) / 100) # centinaia
    qd = int((numero - qm * 1000 - qc * 100) / 10) # decine
    qu = int(numero - qm * 1000 - qc * 100 - qd * 10) # unità
    mm = m[qm]
    cc = c[qc]
    dd = d[qd]
    uu = u[qu]
    return (mm + cc + dd + uu)

def main():
    num = int(input("inserire num: "))

    print(arabo_romano(num))

if __name__=="__main__":
    main()