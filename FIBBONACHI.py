def fibbonacci(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibbonacci(n-1)+fibbonacci(n-2)

print(fibbonacci(6))