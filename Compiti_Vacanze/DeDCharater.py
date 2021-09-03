import math
import random

class Personaggio:
    def __init__(self):
        self.forza = self.abilità()
        self.destrezza = self.abilità()
        self.costituzione = self.abilità()
        self.intelligenza = self.abilità()
        self.saggezza = self.abilità()
        self.carisma = self.abilità()
        self.puntiVita = 10 + modificatore(self.costituzione)

    def abilità(self):
        l = []
        som = 0
        for _ in range(4):
            l.append(round(random.random() * 100) % 6 + 1)
        l.remove(min(l)) #rimuovo il minore
        for k in l:
            som+=k
        return som 


def modificatore(num):
    a = math.floor((num - 10) / 2)
    return a

def main():
    personaggio = Personaggio()

    print("Vita: ",personaggio.puntiVita)
    print("Forza: ",personaggio.forza)
    print("Destrezza: ",personaggio.destrezza)
    print("Costituzione: ",personaggio.costituzione)
    print("Intelligenza: ",personaggio.intelligenza)
    print("Saggezza: ",personaggio.saggezza)
    print("Carisma: ",personaggio.carisma)
    

    
if __name__=="__main__":
    main()