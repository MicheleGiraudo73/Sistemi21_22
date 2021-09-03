def leap(anno):
    if anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0):
        return True
    return False

def main():
    anno = int(input("inserire anno: "))
    if(leap(anno)!= True):
        print("non è un leap year")
    else:
        print(" è un leap year")

if __name__=="__main__":
    main()