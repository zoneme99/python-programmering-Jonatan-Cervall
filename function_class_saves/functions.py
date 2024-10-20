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

def derivative_func(func, x):
    """
    Derive a function with speicific x
    and return value
    
    Parameters
    ----------
    func : function
        The function to be derived
    example func:
    def func(x):
    return math.pow(x, 2)

    x : x value on x-axis
    
    Returns
    -------
    Value of function of specific x Value

    round_ints
    --------
    rounds if func value (dydx) has atleast
    4 zeroes or 4 nines in it's first 4 decimals
    rounds up with 4 nines and rounds down if 4 zeroes
    """
    h = 1e-5
    dydx = ((func(x+h) - func(x)) / h)

    def round_ints(dydx):
        count = 0
        first = None
        for char in str(dydx).split(".")[-1]:
            if char == '0' or char == '9':
                if first == None:
                    first = char
                elif first != char:
                    break    
                count += 1
            else:
                break
        if not count < 4 and first == '0':
            return int(dydx)
        elif not count < 4 and first == '9':
            return int(dydx)+1
        else:
            return dydx
 
    return round_ints(dydx)
    
