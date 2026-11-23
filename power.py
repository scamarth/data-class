def power(n,x):
    if n == 1:
        return n
    else:
        if x % 2 == 0:
            return(power(n,x//2)*power(n,x//2))