anni = [0.2408467,0.61519726,1.8808158, 11.862615,29.447498,84.016846,164.79132]

annoSullaTerra = 31557600

def anniSuiPianeti(secondi):
    anniT = secondi/annoSullaTerra
    print("anni sulla terra: ",round(anniT,2))

    for k in anni:
        print("anni suglia altri pianeti: \n",round(anniT/k,2))


def main():
    sec = int(input("inserire secondi: "))
    anniSuiPianeti(sec)

if __name__=="__main__":
    main()