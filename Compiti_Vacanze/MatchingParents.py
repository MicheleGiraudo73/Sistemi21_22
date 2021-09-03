def par(stringa):
    stack = []
    
    parentesi = {')' : '(', '}' : '{', ']': '['}
    for p in stringa:
        if p in parentesi.values():
            stack.append(p)
        elif p in parentesi:
            
            if not stack:
                return False
            if stack.pop() != parentesi[p]:
                
                return False
    return not stack

def main():
    string = input("inserire stringa delle parentesi: ")

    if(par(string)):
        print("sono giuste")
    else:
        print("non sono giuste")

if __name__=="__main__":
    main()