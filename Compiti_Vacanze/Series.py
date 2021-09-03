def slices(series, length):
    if length <= 0 or length > len(series):
        raise ValueError('length must be > 0 and < length of series')
    position = 0
    result = []
    while position <= len(series):
        if position + length <= len(series):
            ser = ''
            for x in range(length):
                ser += series[position+x]
            result.append(ser)
        position += 1
    return result

def main():
    serie = input("inserire serie: ")
    lunghezza = int(input("inserire lunghezza serie: "))

    print(slices(serie,lunghezza))

if __name__=="__main__":
    main()