def dec_to_frac(f):

    count = 2

    def simplify(num, denom):
        while True:
            temp = denom
            for divnum in range(2, denom):
                if num % divnum == 0 and denom % divnum == 0:
                    num = int(num/divnum)
                    denom = int(denom/divnum)
                    break
            if temp == denom:
                return num, denom

    while True:
        temp = f
        temp *= count
        if str(temp).split(".")[-1] != '0':
            count += 1
        else:
            break
        
    num, denom = simplify(int(f*count), count)
    return num, denom
