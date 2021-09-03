def encode(parola):
    encoding = ""
    temp = ""
    cnt = 1

    if not parola: return ""

    for lettera in parola:
        if lettera != temp:
            if temp:
                encoding += str(cnt)+temp
            cnt = 1
            temp = lettera
        else:
            cnt += 1
    else:
        encoding += str(cnt)+temp
        return encoding

def main():
    parola = input("inserisci parola: ")
    print(encode(parola))

if __name__=="__main__":
    main()