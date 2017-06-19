def SumOfParts (n):
    if n == 0 :
        return 0
    else:
        return n + SumOfParts(n - 1)


print SumOfParts(50)